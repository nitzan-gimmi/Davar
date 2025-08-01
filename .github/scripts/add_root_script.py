# .github/scripts/add_root_script.py
import os
import google.generativeai as genai
import json
import base64
import requests
import sys

def main():
    # --- Get variables from environment ---
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY_SECRET')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN_SECRET')
    ISSUE_TITLE = os.getenv('ISSUE_TITLE')
    REPO_FULL_NAME = os.getenv('REPO_FULL_NAME')

    if not all([GEMINI_API_KEY, GITHUB_TOKEN, ISSUE_TITLE, REPO_FULL_NAME]):
        print("Error: Missing one or more environment variables.")
        sys.exit(1)

    # --- Extract root name from issue title ---
    try:
        root_name = ISSUE_TITLE.split(':', 1)[1].strip()
        if not root_name:
            raise IndexError
    except IndexError:
        print(f"Error: Could not extract root name from title: {ISSUE_TITLE}")
        sys.exit(1)

    # --- 1. Call Gemini to generate the JSON content ---
    print(f"Generating JSON for root: {root_name}...")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    # This is the improved prompt with a strict validation instruction
    prompt = f"""
    You are the primary expert for the "Davar" project.
    Your task is to generate the complete JSON file for the following root family: **{root_name}**.
    Ensure the file includes all relevant binyanim, with all inflections, niqqud, and relationships, according to the project's precise architecture.
    **CRITICAL: Before outputting, you must validate the entire JSON content to ensure it is perfectly valid and free of syntax errors (like missing commas or brackets).**
    Respond with ONLY the raw JSON content inside a single json code block. Do not include any other text.
    """
    try:
        response = model.generate_content(prompt)
        json_content_raw = response.text.strip()
        if json_content_raw.startswith('```json'):
            json_content_raw = json_content_raw[7:]
        if json_content_raw.endswith('```'):
            json_content_raw = json_content_raw[:-3]
        
        # Validate that the content is valid JSON
        json.loads(json_content_raw)
        print("Successfully generated and validated JSON content.")

    except Exception as e:
        print(f"Error processing content from Gemini: {e}")
        # Add the raw response to the output for better debugging
        print("--- Raw Gemini Response ---")
        print(response.text)
        print("---------------------------")
        sys.exit(1)

    # --- 2. Commit the new file to GitHub ---
    filepath_in_repo = f"data/roots/{root_name}.json"
    commit_message = f"feat(data): Automatically add full model for root {root_name}"
    api_url = f"https://api.github.com/repos/{REPO_FULL_NAME}/contents/{filepath_in_repo}"

    encoded_content = base64.b64encode(json_content_raw.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'message': commit_message,
        'content': encoded_content,
        'branch': 'main'
    }

    print(f"Committing file '{filepath_in_repo}' to repository...")
    res = requests.put(api_url, headers=headers, data=json.dumps(data))

    if res.status_code in [200, 201]:
        print("✅ Successfully committed to GitHub.")
        commit_url = res.json().get('commit', {}).get('html_url', 'N/A')
        with open(os.environ.get('GITHUB_OUTPUT', 'github_output.txt'), 'a') as f:
          f.write(f"commit_url={commit_url}")
    else:
        print(f"❌ Error committing to GitHub. Status: {res.status_code}")
        print(f"Response: {res.text}")
        sys.exit(1)

if __name__ == "__main__":
    main()

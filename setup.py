from setuptools import setup, find_packages

setup(
    name='rogum4-hfbt-resonance',
    version='0.7.0',
    author='Nitzan Banin / Ginnie-Gimmy',
    author_email='office@rogum4.org',
    description='HFBT: Hebrew Factor-Based Tokenization and Resonance Engine',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='[PLACEHOLDER_REPO_URL]',
    packages=find_packages(exclude=['tests', 'docs', 'reports']),
    install_requires=open('requirements.txt').read().splitlines(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
    ],
)
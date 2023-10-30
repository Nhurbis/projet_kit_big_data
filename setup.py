from setuptools import setup, find_packages

setup(
    name='project-big-data',
    version='0.1.0',
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'datetime==5.2',
        'pymongo==4.5.0',
        'gradio==3.50.2',
        'pytest==7.4.3',
        'pytest-cov==4.1.0',
        'sphinx==7.2.6',
        'mongomock==4.1.2',
        'argparse==1.4.0',
    ],
    author='Guillaume, Paul, Aleksander, Lucas, Guillaume',
    description='ToDo list du projet kit big data',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)

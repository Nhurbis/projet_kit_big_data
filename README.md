# To-Do List Python Library

## Overview

This project aims to to create a comprehensive Python library for personal tasks (To-Do List). 

## Features

The application will allow users to:

- Add a new task to the list with at least a name and a description.
- Mark a task as completed.
- Remove a task from the list.
- Display the list of ongoing tasks.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Poetry

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/todo-list-python.git
cd todo-list-python
```
2. Create docker build 

```docker build -t les_meures``` 

2. Set up a virtual environment and install dependencies:

```bash
poetry install
```

### Usage

```bash
# Add a new task
python task_manager_cli.py create_tasklist "Ma Liste de Tâches"
```

## Testing

We use pytest for unit testing. Run the tests using the following command:

```bash
pytest --cov=model tests/
```

## Documentation

The documentation for this project is generated using Sphinx. To build the documentation locally, run in the docs folder:

```bash
make html
```

Then, open `docs/_build/html/index.html` in a web browser.

## CI/CD

This project is set up with a CI/CD pipeline using GitHub Actions. 
Any push to the main branch triggers the pipeline, which runs tests, checks code coverage, and deploys the documentation.


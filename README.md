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

2. Set up a virtual environment and install dependencies:

```bash
poetry install
```

### Usage

```bash
# Add a new task
python main.py add "Task Name" "Task Description"

# Mark a task as completed
python main.py complete <task_id>

# Remove a task from the list
python main.py remove <task_id>

# Display the list of ongoing tasks
python main.py list
```

## Testing

We use pytest for unit testing. Run the tests using the following command:

```bash
pytest
```

## Documentation

The documentation for this project is generated using Sphinx. To build the documentation locally, run:

```bash
poetry run make -C docs html
```

Then, open `docs/_build/html/index.html` in a web browser.

## CI/CD

This project is set up with a CI/CD pipeline using GitHub Actions. 
Any push to the main branch triggers the pipeline, which runs tests, checks code coverage, and deploys the documentation.

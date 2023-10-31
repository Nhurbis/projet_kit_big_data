# To-Do List Python Library

## Overview

This project aims to create a comprehensive Python library for managing personal tasks (To-Do List).

## Features

The application allows users to:

- Add a new task to the list with at least a name and a description.
- Mark a task as completed.
- Remove a task from the list.
- Display the list of ongoing tasks.

## Getting Started

These instructions will get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Poetry

### Installation

#### Using Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/Nhurbis/projet_kit_big_data.git
   cd projet_kit_big_data
   ```

2. Build and run the Docker container:

   ```bash
   docker build -t les_meures .
   docker run -it -p 7860:7860 les_meures
   ```

3. Access the application in your web browser at: http://localhost:7860

#### Using Poetry

1. Clone the repository:

   ```bash
   git clone https://github.com/Nhurbis/projet_kit_big_data.git
   cd projet_kit_big_data
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   poetry install
   poetry run python main.py
   ```
3. Access the application in your web browser at: http://localhost:7860

### Task Manager CLI

The Task Manager CLI is a command-line tool for managing your tasks and task lists. Here is a guide on how to use it.

#### Installation

Ensure you have installed all the necessary dependencies and configured your Python environment correctly before running the application.

#### Commands

```bash
python task_manager_cli.py create_tasklist <title>
python task_manager_cli.py add_task <tasklist_id> <name> <description>
python task_manager_cli.py complete_task <tasklist_id> <task_id>
python task_manager_cli.py delete_task <tasklist_id> <task_id>
python task_manager_cli.py show_incomplete_tasks <tasklist_id>
```

Example Usage:

```bash
python task_manager_cli.py create_tasklist "My Task List"
python task_manager_cli.py add_task <tasklist_id> "Go Shopping" "Buy milk, eggs, and bread"
python task_manager_cli.py complete_task <tasklist_id> 1
python task_manager_cli.py show_incomplete_tasks <tasklist_id>
```

## Testing

We use pytest for unit testing. Run the tests using the following command:

```bash
pytest --cov=model tests/
```

## Documentation

The documentation for this project is generated using Sphinx. To build the documentation locally, run the following commands in the docs folder:

```bash
make html
```

Then, open `docs/_build/html/index.html` in a web browser.

## CI/CD

This project is set up with a CI/CD pipeline using GitHub Actions. Any push to the main branch triggers the pipeline, which runs tests, checks code coverage, and deploys the documentation.

## Security

As part of this project, and in order to facilitate the teacher's grading process, the decision was made to leave the database connection string visible in the code (instead of using environment variables). Additionally, we are directly returning the \_id values to facilitate the use of the very simplistic gradio interface. In a real production environment, these choices would not have been made.

## Creating a Python Package & Uploading to PyPI

```bash
python setup.py sdist bdist_wheel
twine upload dist/* -u __token__ -p $token_key
```

## Performance Optimization

When managing large amounts of data, it is crucial to optimize the library's performance to ensure a smooth and efficient user experience. Here are some strategies to achieve this, accompanied by examples of technologies and methods:

### 1. Database Indexing

- **Example**: Use MongoDB and create indexes on the most frequently searched fields to speed up queries.

### 2. Efficient Database Queries

- **Example**: Use SQLAlchemy (Python) to write optimized SQL queries and avoid unnecessary lazy loading.

### 3. Pagination

- **Example**: Use Django REST framework API to implement pagination in your API endpoints.

### 4. Caching

- **Example**: Use Redis to store the results of frequent queries and reduce response time.

### 5. Lazy Loading

- **Example**: Use Vue.js or React to load components on demand and improve client-side performance.

### 6. Parallelization

- **Example**: Use asyncio (Python) or CompletableFuture (Java) libraries to parallelize asynchronous operations.

### 7. Code Profiling and Optimization

- **Example**: Use tools like Py-Spy (Python) or VisualVM (Java) to profile your application and identify bottlenecks.

### 8. Efficient Memory Usage

- **Example**: Use tools like Valgrind to detect memory leaks and optimize memory usage.

### 9. Batch Processing

- **Example**: Use Apache Spark or Apache Flink for batch processing of large amounts of data.

### 10. Update Only When Necessary

- **Example**: Use a version control system like Git to track changes and avoid unnecessary updates.

### 11. Use Database Optimization Tools

- **Example**: Use tools like MySQL Workbench or MongoDB Compass to monitor and optimize database performance.

### 12. Data Compression

- **Example**: Use compression algorithms like Gzip to reduce the

size of data transferred over the network.

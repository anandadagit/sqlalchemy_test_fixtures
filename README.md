# pytest fixtures

This repository contains simple SQLAlchemy models and pytest tests. This compact README explains the test setup, basic fixture concepts, and how to run the test suite.

**Repository overview**
- `models/`: SQLAlchemy model definitions (`Owner`, `Car`).
- `tests/`: pytest test files and `conftest.py` which provides shared fixtures.
- `requirements.txt`: project dependencies.

**How to run tests**
- Create and activate virtual environment
- Windows: `python -m venv venv` and `venv\Scripts\activate`
- Mac/Linux: `python3 -m venv venv` and `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`.
- Run the full test suite: `pytest -v`.


**`conftest.py` in this project (high level)**
- `conftest.py` defines a `session` fixture used by tests that need database access.
- For each test the fixture creates an in-memory SQLite engine, initializes the database schema, provides a `Session` object to the test, and cleans up after the test.
- This yields fast, isolated tests because each test gets a fresh database.

Dependencies: `sqlalchemy`, `pytest`.



# fastapi-auth-setup
# Start the FastAPI application with hot-reloading enabled.
# Example: This will start the app, and any changes in your code will automatically reload the server.
uvicorn app.main:app --reload

# Create a new Alembic migration script by comparing the current database state 
# to the models defined in your SQLAlchemy models.
# Example: This command will generate a migration script with a message "create my table".
alembic revision --autogenerate -m "create my table"

# Apply the latest migrations to the database, updating it to the most recent version.
# Example: This will apply all pending migrations to your database.
alembic upgrade head

# Rollback the most recent migration, effectively undoing the last change made to the database.
# Example: If you made a mistake in the latest migration, this will revert it.
alembic downgrade -1

# Run all tests in the current directory (and subdirectories) with pytest, 
# and set the logging level to INFO to see detailed logs during the test run.
# Example: This will run all tests and print logs with INFO level during execution.
pytest --log-cli-level=INFO

# List the current migration history, showing applied and pending migrations.
# Example: This will show the list of migrations with their revision IDs and messages.
alembic history

# Show the details of a specific migration (replace `<revision>` with the specific revision ID).
alembic show <revision>
# Example: To see the details of a migration with revision ID 'abc123'.
alembic show abc123

# Generate a new secret key for FastAPI security settings, such as for JWT tokens.
# Example: This will output a 32-byte hex string that can be used as a secret key.
openssl rand -hex 32

# Run the FastAPI application specifying the host and port (e.g., for a specific environment).
# Example: This starts the app on all network interfaces (0.0.0.0) and port 8000.
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Apply a specific migration to a specific version.
alembic upgrade <revision>
# Example: To upgrade to a specific migration with revision ID 'def456'.
alembic upgrade def456

# Apply a downgrade to a specific version.
alembic downgrade <revision>
# Example: To downgrade to a specific migration with revision ID 'abc123'.
alembic downgrade abc123

# Run a specific test file or test case by specifying the path to the test file or the test case.
# Example: To run all tests in a specific file.
pytest tests/test_example.py
# Example: To run a specific test case within a test file.
pytest tests/test_example.py::test_specific_case

# Run the application in production mode with more workers (useful for better performance).
# Example: This runs the FastAPI application with 4 worker processes.
uvicorn app.main:app --workers 4


# ############################# Mailpit Setup ###########################

## 1. Install Mailpit

### Download and Install
1. Download Mailpit from the [official GitHub releases page](https://github.com/axllent/mailpit/releases).
2. Place the binary in your system's PATH or the project directory.
3. On Linux/macOS, give the binary execute permissions:

    chmod +x mailpit

4. Start Mailpit:

    ./mailpit

    This will start the SMTP server on `localhost:1025` and the web interface on `localhost:8025`.


## 2. Accessing Mailpit

To view the emails captured by Mailpit, open your browser and go to:

http://localhost:8025

This interface allows you to view, search, and manage the emails sent by the FastAPI application.


## 3. Useful Mailpit Commands

- **Start Mailpit**:
    ./mailpit

- **Specify a Different SMTP Port**:
    ./mailpit --smtp 2525

- **Specify a Different HTTP Port**:
    ./mailpit --http 8080

- **Verbose Output**:
    ./mailpit --verbose

- **Delete All Mails**:
    ./mailpit --delete-all
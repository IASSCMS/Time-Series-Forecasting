# Time-Series-Forecasting
This repository contains all necessary training methods, datasets, and works related to the development of Intelligent Demand Forecasting for Supply Chain Management.

## Running the Backend Service

The project includes a Makefile with the following commands to manage the Django backend service:

### Starting the Server
```bash
# Start the Django server with migrations
make run-server
```
This will:
1. Create migrations for the forecastApp
2. Apply migrations to the database
3. Start the Django server at  http://localhost:8000/

### Other Commands

#### Access Django Shell
```bash
make shell
```

#### Run Tests
```bash
make test
```

#### Clear and Recreate Migrations
```bash
make clear-migrations
```
This will delete all migration files (except `__init__.py`), then recreate and apply migrations.

#### Start Server with Fake Migrations
```bash
make run-server-fake
```
Use this when you need to run the server with `--fake-initial` flag for migrations.

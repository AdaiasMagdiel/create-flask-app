# Create Flask App

This project creates a folder system for a Flask application, which is useful when you want to gain productivity without losing quality.

## Folder Structure

```
├── app/
│   ├── __init__.py
│   ├── settings.py
│   └── routes/
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py
│       │
│       ├── site/
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── __init__.py
│       └── error_handler.py
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```

## Structure Description

- `app/` Directory
   - **__init__.py:** This file indicates that the 'app' directory should be treated as a Python package.
   - **settings.py:** Configuration settings for the application.
   - **routes/:** A subdirectory containing modules related to routing.
      - **api/:**
         - **__init__.py:** Marks the 'api' directory as a Python package.
         - **routes.py:** Defines API-specific routes.
      - **site/:**
         - **__init__.py:** Marks the 'site' directory as a Python package.
         - **routes.py:** Contains routes for the main site.
      - **__init__.py:** Marks the 'routes' directory as a Python package.
      - **error_handler.py:** Handles errors for the routes.

- `.env`: Configuration file used to store environment variables for the application.

- `.gitignore`: Specifies files and directories that should be ignored by version control.

- `main.py`: The main entry point for the application.

- `requirements.txt`: Lists the dependencies and their versions required for the project.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/AdaiasMagdiel/create-flask-app.git
   ```

## Usage

You can make a `.bat` or a `.sh` to run the project via cli. See a windows `create-flask-app.bat` example:

```cmd
@echo off

py path\to\this\project\main.py %*

```

Then, you can save this file in a folder thats is already in path and run:

```cmd
create-flask-app test-app
```

This will create a `test-app` folder with the project.

Feel free to modify and extend the application based on your requirements.

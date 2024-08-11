import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
)

project_name = 'my_project'

list_of_files = [
    # Backend
    f"backend/app/__init__.py",
    f"backend/app/main.py",
    f"backend/app/models.py",
    f"backend/app/schemas.py",
    f"backend/app/api/__init__.py",
    f"backend/app/api/v1/__init__.py",
    f"backend/app/api/v1/qa.py",
    f"backend/app/api/v1/config.py",
    f"backend/tests/__init__.py",
    f"backend/tests/test_qa.py",
    f"backend/tests/test_config.py",
    f"backend/Dockerfile",
    f"backend/requirements.txt",
    f"backend/README.md",
    
    # Frontend
    f"frontend/app.py",
    f"frontend/Dockerfile",
    f"frontend/requirements.txt",
    f"frontend/README.md",

    # Root
    ".gitignore",
    "README.md"
]

for path in list_of_files:
    file_path = Path(path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file {filename}")
    else:
        logging.info(f"File {filename} already exists")

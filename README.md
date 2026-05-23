# Async File Sorter

This script asynchronously sorts files from a source directory into subdirectories based on their file extensions.

## Option 1: Running Locally (Virtual Environment)

1. **Create a virtual environment:**
```
python3 -m venv .venv
```

2. Activate the virtual environment:
```
# On macOS and Linux
source .venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the script:
```
python3 main.py --source ./test_source --output ./test_output
```

## Option 2: Running via Docker Compose

This approach isolates the execution environment using Python 3.11, completely avoiding potential library incompatibility.

```
docker compose run --rm file-sorter
```

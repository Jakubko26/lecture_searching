from pathlib import Path
import json

def read_data(file_name, field):
    file_path = Path.cwd() / file_name

    if not file_path.exists():
        return None






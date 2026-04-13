from pathlib import Path
import json

def read_data(file_name, field):
    file_path = Path.cwd() / file_name

    if not file_path.exists():
        return None
    with open(file_path, "r", encoding="utf=8") as f:
        data = json.load(f)
    return data.get(field,None)





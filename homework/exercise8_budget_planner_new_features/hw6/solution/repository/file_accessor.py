import json
import os
from typing import Any, Dict


class JsonFileAccessor:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def read(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return {"items": []}

        try:
            with open(self.file_path, "r", encoding="utf-8") as file_obj:
                return json.load(file_obj)
        except (json.JSONDecodeError, FileNotFoundError):
            return {"items": []}

    def write(self, data: Dict[str, Any]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file_obj:
            json.dump(data, file_obj, indent=4, ensure_ascii=False)

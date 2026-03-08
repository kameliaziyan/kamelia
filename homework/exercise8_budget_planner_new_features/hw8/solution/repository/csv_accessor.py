import csv
import os
from typing import Any, Dict, List


class CsvFileAccessor:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def read(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", newline="", encoding="utf-8") as file_obj:
            reader = csv.DictReader(file_obj)
            return list(reader)

    def write(self, rows: List[Dict[str, Any]]) -> None:

        if not rows:
            with open(self.file_path, "w", encoding="utf-8"):
                return

        fieldnames = rows[0].keys()
        with open(self.file_path, "w", newline="", encoding="utf-8") as file_obj:
            writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

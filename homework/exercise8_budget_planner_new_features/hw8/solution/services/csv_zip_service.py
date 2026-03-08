from pathlib import Path
import zipfile


class CSVZipService:
    DATA_DIR = Path("data")

    REQUIRED_FILES = [
        "accounts.csv",
        "categories.csv",
        "transactions.csv",
        "transfers.csv",
    ]

    def export_data(self, zip_path: str) -> None:
        with zipfile.ZipFile(zip_path, "w") as archive:
            for file_name in self.REQUIRED_FILES:
                file_path = self.DATA_DIR / file_name

                if file_path.exists():
                    archive.write(file_path, arcname=file_name)

    def import_data(self,zip_path: str) ->None:
        with zipfile.ZipFile(zip_path, "r") as archive:
            files = archive.namelist()

            for required_file in self.REQUIRED_FILES:
                if required_file not in files:
                    raise ValueError(f"Missing file: {required_file}")
                
            archive.extractall(self.DATA_DIR)


            
    
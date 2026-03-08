from pathlib import Path
import zipfile


class CSVZipService:
    data_dir = Path("data")

    required_files= [
        "accounts.csv",
        "categories.csv",
        "transactions.csv",
        "transfers.csv",
    ]

    def export_data(self, zip_path: str) -> None:
        with zipfile.ZipFile(zip_path, "w") as archive:
            for file_name in self.required_files:
                file_path = self.data_dir / file_name

                if file_path.exists():
                    archive.write(file_path, arcname=file_name)

    def import_data(self, zip_path: str) -> None:
        with zipfile.ZipFile(zip_path, "r") as archive:
            files = archive.namelist()

            for required_file in self.required_files:
                if required_file not in files:
                    raise ValueError(f"Missing file: {required_file}")

            archive.extractall(self.data_dir)

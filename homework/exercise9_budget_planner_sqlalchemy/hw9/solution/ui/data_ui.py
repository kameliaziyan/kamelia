import requests

from solution.ui.http_client import BASE_URL, CONNECTION_ERROR, STATUS_OK, safe_get

KEY_MESSAGE = "message"

CANCEL_OPTION = "0"


def export_data() -> None:
    while True:

        path = input(
            "Enter file name to save backup (example: backup.zip)(0 to cancel): "
        ).strip()

        if path == CANCEL_OPTION:
            return

        if not path.endswith(".zip"):
            print("File must end with .zip")
            continue

        try:
            response = requests.get(f"{BASE_URL}/export")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return

        if response.status_code != STATUS_OK:
            print("Export faild. ")
            return

        try:
            with open(path, "wb") as file_obj:
                file_obj.write(response.content)

        except OSError:
            print("Faild to write file. ")
            return

        print(f"Backup saved successfully.")
        return


def import_data() -> None:

    print("\n ** Note - Importing data will replace all existing data.**")

    confirm = input("Continue? (y/n): ").strip().lower()

    if confirm != "y":
        print("Import cancelled.")
        return

    path = input("Enter path to zip file: ").strip()

    if not path:
        print("Invalid file path.")
        return

    try:
        with open(path, "rb") as file_obj:

            response = requests.post(
                f"{BASE_URL}/import",
                files={"file": file_obj},
            )
    except FileNotFoundError:
        print("File not found.")
        return
    except requests.exceptions.ConnectionError:
        print(CONNECTION_ERROR)
        return

    if response.status_code != STATUS_OK:
        print("Import failed.")
        return

    data = response.json()

    print(data.get(KEY_MESSAGE, "Import completed."))

from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from solution.services.csv_zip_service import CSVZipService
from starlette.background import BackgroundTask
import os

# KEY_MESSAGE = "message"
router = APIRouter()
service = CSVZipService()


@router.get("/export")
async def export_data() -> FileResponse:

    zip_path = "budget_backup.zip"
    service.export_data(zip_path)

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="budget_backup.zip",
        background=BackgroundTask(os.remove, zip_path),
    )


@router.post("/import")
async def import_data(file: UploadFile) -> dict:

    zip_path = "uploaded.zip"

    with open(zip_path, "wb") as buffer:
        buffer.write(await file.read())

    try:
        service.import_data(zip_path)
    except ValueError as error:
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return {"message": str(error)}

    if os.path.exists(zip_path):
        os.remove(zip_path)
    return {"message": "Data imported successfully"}

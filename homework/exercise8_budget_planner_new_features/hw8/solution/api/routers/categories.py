from dataclasses import dataclass

from fastapi import APIRouter

from solution.models.category import Category, CategoryType
from solution.services.category_services import CategoryService

KEY_MESSAGE = "message"
KEY_DATA = "data"
KEY_DETAILS = "details"
KEY_ID = "id"
KEY_NAME = "name"
KEY_TYPE = "type"

router = APIRouter()
category_service = CategoryService()


@dataclass
class CategoryRequest:
    name: str
    type: str


@router.post("/categories")
async def create_category(category_data: CategoryRequest) -> dict:

    category = Category(
        id=0,
        name=category_data.name,
        type=CategoryType(category_data.type),
    )

    created_category = category_service.add(category)

    return {
        KEY_MESSAGE: "Category created successfully",
        KEY_DETAILS: {
            KEY_ID: created_category.id,
            KEY_NAME: created_category.name,
            KEY_TYPE: str(created_category.type),
        },
    }


@router.get("/categories")
async def list_categories() -> dict:

    categories = category_service.categories or []

    return {
        KEY_MESSAGE: "Categories retrieved",
        KEY_DATA: [
            {
                KEY_ID: category.id,
                KEY_NAME: category.name,
                KEY_TYPE: category.type,
            }
            for category in categories
        ],
    }


@router.delete("/categories/{category_id}")
async def remove_category(category_id: int) -> dict:

    category_service.remove(category_id)
    return {KEY_MESSAGE: "Category removed successfully"}

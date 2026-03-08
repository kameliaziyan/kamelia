from fastapi import APIRouter

from solution.services.report_services import ReportService

KEY_MESSAGE = "message"
KEY_DATA = "data"
KEY_INCOME = "income"
KEY_EXPENSES = "expenses"
KEY_NET = "net_cash_flow"

router = APIRouter()

report_service = ReportService()


@router.get("/spending-by-category")
async def spending_by_category(year: int, month: int) -> dict:

    result = report_service.spending_by_category(year, month)

    return {
        KEY_MESSAGE: "Spending by category retrieved",
        KEY_DATA: {category: str(amount) for category, amount in result.items()},
    }


@router.get("/summary")
async def get_monthly_summary(year: int, month: int) -> dict:

    result = report_service.monthly_summary(year, month)

    return {
        KEY_MESSAGE: "Monthly summary retrieved",
        KEY_DATA: {
            KEY_INCOME: str(result["income"]),
            KEY_EXPENSES: str(result["expenses"]),
            KEY_NET: str(result["net_cash_flow"]),
        },
    }

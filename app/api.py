from typing import Annotated, List

from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request
from starlette import status

from calculator import repository
from calculator.rpn import Calculator
from config import settings

router = APIRouter()


# TODO: quick client identification by ip to be replaced (WebSocket or redis)
async def get_current_client_calculator(request: Request) -> Calculator:
    return repository.get_calculator(request.client.host)


@router.get("/operators")
async def allowed_operators() -> List[str]:
    return Calculator.OPERATORS


@router.get("/stack")
async def get_stack_operands(
    stack: Annotated[Calculator, Depends(get_current_client_calculator)]
) -> List[float]:
    return stack.get_elements()


@router.post("/stack/{operand}", status_code=status.HTTP_202_ACCEPTED)
async def add_operand_to_stack(
    operand: float,
    calculator: Annotated[Calculator, Depends(get_current_client_calculator)],
):
    try:
        calculator.add_operand(operand=operand)
        return "OK"
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        )


@router.get("/stack/compute")
async def compute_stack(
    operator: str,
    calculator: Annotated[Calculator, Depends(get_current_client_calculator)],
) -> float:
    try:
        return calculator.calculate(operator=operator)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        )


@router.delete("/stack/last", status_code=status.HTTP_204_NO_CONTENT)
async def remove_last_operand(
    calculator: Annotated[Calculator, Depends(get_current_client_calculator)]
):
    try:
        calculator.remove_last()
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        )


@router.delete("/stack", status_code=status.HTTP_204_NO_CONTENT)
async def clean_stack_operands(
    calculator: Annotated[Calculator, Depends(get_current_client_calculator)]
):
    try:
        calculator.clean_stack()
        return ""
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        )


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)
app.include_router(router, prefix=f"/{settings.PROJECT_VERSION}")

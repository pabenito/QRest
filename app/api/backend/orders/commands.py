from fastapi import APIRouter, status, HTTPException

from app.core.entities.order import Request, Order, RequestPost, Command
from app.core.use_cases.orders.commands import CommandUseCases
from app.core.use_cases.orders.compute_command import ComputeCommandUseCases
from app.db.repositories.mongo_repositories.orders.commands import MongoCommandRepository
from app.db.repositories.mongo_repositories.orders.current_requests import MongoCurrentRequestsRepository
from app.db.repositories.mongo_repositories.orders.processed_requests import MongoProcessedRequestsRepository
from app.core.exceptions.orders import OrderOperationFailedException

# Create router
router = APIRouter()

command_use_cases = CommandUseCases(repository=MongoCommandRepository())
compute_command_use_cases = ComputeCommandUseCases(
    commands_repository=MongoCommandRepository(),
    current_requests_repository=MongoCurrentRequestsRepository(),
    processed_requests_repository=MongoProcessedRequestsRepository())


@router.get("/{id}/commands",
            response_model=list[Command],
            response_model_exclude_unset=True,
            response_model_exclude_defaults=True)
def get_all_commands(order_id: str):
    return command_use_cases.get_all(order_id)


@router.post("/{id}/command",
             response_model=Command,
             response_model_exclude_unset=True,
             response_model_exclude_defaults=True)
def compute_command(order_id: str):
    try:
        command = compute_command_use_cases.process_current_requests_and_create_new_command(order_id)
    except OrderOperationFailedException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return command

import typing as t

from fastapi import APIRouter, Depends, Request, Query

from ... import deps
from ....database import models
from .......models.inbounds.easy_inbounds_builder import ProtocolsType

from .......database import crud
from .......database import schemas

router = APIRouter()


@router.get(
    "/", response_model=t.Optional[t.List[schemas.InboundsBase]],
)
@deps.limiter.limit('1/minute', per_method=True)
async def read_data(
        request: Request,
        user_id: t.Optional[int] = Query(None, title="User ID", description="User ID"),
        enabled: t.Optional[bool] = Query(None, title="Enabled", description="Enabled"),
        port: t.Optional[int] = Query(None, title="Port", description="Port"),
        protocol: t.Optional[ProtocolsType] = Query(None, title="Protocol", description="Protocol"),
        tag: t.Optional[str] = Query(None, title="Tag", description="Tag"),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve inbounds.
    """
    filters = schemas.InboundsOrderGetFilter(
        user_id=user_id,
        enable=enabled,
        port=port,
        protocol=protocol,
        tag=tag,
    )
    return await crud.inbounds.get_multi_filter(filters=filters, skip=skip, limit=limit)

# @router.put("/{data_id}", response_model=schemas.ReplacedOrder)
# @deps.limiter.limit('1/minute', per_method=True)
# async def update_data(
#         *,
#         request: Request,
#         db: AsyncSession = Depends(deps.get_db),
#         data_id: int,
#         data_in: schemas.ReplacedOrderUpdate,
#         current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update a Data.
#     """
#     data = await crud.replaced_order.get(db, id=data_id)
#
#     if not data:
#         raise HTTPException(
#             status_code=404,
#             detail="The data with this id does not exist in the system",
#         )
#
#     data = await crud.replaced_order.update(db, db_obj=data, obj_in=data_in)
#     return data

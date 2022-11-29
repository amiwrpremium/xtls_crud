import typing as t

from fastapi import APIRouter, Depends, Request, Query, HTTPException

from ... import deps
from ....database import models
from .......models.inbounds.easy_inbounds_builder import ProtocolsType
from .......models.inbounds.inbounds import PrettyInbound
from .......models.inbounds.easy_inbounds_builder import (
    EasyBuilderSchemaCreate
)
from .......utils.builders.inbounds_builder import (
    EasyInboundBuilder
)

from .......database import crud
from .......database import schemas

router = APIRouter()


@router.get(
    "/", response_model=t.Optional[t.List[PrettyInbound]],
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
    data = await crud.inbounds.get_multi_filter(filters=filters, skip=skip, limit=limit)

    result = []
    for item in data:
        try:
            pretty = PrettyInbound.from_orm(item)
            result.append(pretty)
        except Exception as e:
            print(e)

    return result


@router.post("/", response_model=PrettyInbound)
@deps.limiter.limit('10/minute', per_method=True)
async def add_new(
        *,
        obj_in: EasyBuilderSchemaCreate,
        request: Request,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Build a setting.
    """

    _ = EasyInboundBuilder().with_user_id(obj_in.user_id).with_up(obj_in.up).with_down(obj_in.down).with_total(
        obj_in.total).with_remark(obj_in.remark).with_enable(obj_in.enable).with_expiry_time(
        obj_in.expiry_time).with_listen(
        obj_in.listen).with_port(obj_in.port).with_protocol(obj_in.protocol).with_uuid(obj_in.uuid).with_network(
        obj_in.network).with_security(obj_in.security).with_server_name(obj_in.server_name).with_ws_path(
        obj_in.ws_path).with_tag(obj_in.tag).with_sniffing(obj_in.sniffing).build()

    result = await crud.inbounds.create(obj_in=_)

    return PrettyInbound.from_orm(result)

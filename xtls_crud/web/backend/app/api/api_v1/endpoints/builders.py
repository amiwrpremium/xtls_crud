import typing as t

from fastapi import APIRouter, Depends, Request

from ... import deps
from ....database import models

from .......utils.builders.inbounds_builder import (
    EasyInboundBuilder
)
from .......models.inbounds.easy_inbounds_builder import (
    EasyBuilderSchemaCreate
)

router = APIRouter()


@router.post("/", response_model=str)
@deps.limiter.limit('10/minute', per_method=True)
async def client_creator(
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

    return _.json()

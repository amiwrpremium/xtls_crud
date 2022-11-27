from typing import Any, Dict, Union, Optional
from sqlalchemy.future import select

from ..crud.base import CRUDBase
from ..models.inbounds import Inbounds
from ..schemas.inbounds import InboundsCreate, InboundsUpdate


class CRUDInbounds(CRUDBase[Inbounds, InboundsCreate, InboundsUpdate]):
    async def create(self, *, obj_in: InboundsCreate) -> Inbounds:
        db_obj = Inbounds(
            user_id=obj_in.user_id,
            up=obj_in.up,
            down=obj_in.down,
            total=obj_in.total,
            remark=obj_in.remark,
            enable=obj_in.enable,
            expiry_time=obj_in.expiry_time,
            listen=obj_in.listen,
            port=obj_in.port,
            protocol=obj_in.protocol,
            settings=obj_in.settings,
            stream_settings=obj_in.stream_settings,
            tag=obj_in.tag,
            sniffing=obj_in.sniffing,
        )

        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)

        return db_obj

    async def update(
            self, *, db_obj: Inbounds, obj_in: Union[InboundsUpdate, Dict[str, Any]]
    ):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for k, v in update_data.items():
            update_data[k] = v

        return await super().update(db_obj=db_obj, obj_in=update_data)

    async def get_by_user_id(self, *, user_id: int) -> Optional[Inbounds]:
        return (await self.session.execute(select(Inbounds).filter_by(user_id=user_id))).scalar_one_or_none()

    async def get_by_remark(self, *, remark: str) -> Optional[Inbounds]:
        return (await self.session.execute(select(Inbounds).filter_by(remark=remark))).scalar_one_or_none()

    async def get_by_tag(self, *, tag: str) -> Optional[Inbounds]:
        return (await self.session.execute(select(Inbounds).filter_by(tag=tag))).scalar_one_or_none()

    async def get_by_port(self, *, port: int) -> Optional[Inbounds]:
        return (await self.session.execute(select(Inbounds).filter_by(port=port))).scalar_one_or_none()

    async def get_by_protocol(self, *, protocol: str) -> Optional[Inbounds]:
        return (await self.session.execute(select(Inbounds).filter_by(protocol=protocol))).scalar_one_or_none()


inbounds = CRUDInbounds(Inbounds)

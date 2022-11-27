from sqlalchemy import Column, String, text, Boolean, Integer

from ..db.base_class import Base


class Inbounds(Base):
    __name__ = 'inbounds'

    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False,
        server_default=text("nextval('inbounds_id_seq'::regclass)"))
    user_id = Column(Integer)
    up = Column(Integer)
    down = Column(Integer)
    total = Column(Integer)
    remark = Column(String)
    enable = Column(Boolean)
    expiry_time = Column(Integer)
    listen = Column(String)
    port = Column(Integer, unique=True)
    protocol = Column(String)
    settings = Column(String)
    stream_settings = Column(String)
    tag = Column(String, unique=True)
    sniffing = Column(String)

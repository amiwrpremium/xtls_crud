### Create new record
    from uuid import uuid4

    from xtls_crud.utils.builders.inbounds_builder import EasyInboundBuilder
    from xtls_crud.database import crud


    async def main():
        builder = EasyInboundBuilder().with_user_id(1).with_up("1gb").with_down("1gb").with_total(
            0).with_remark("TEST").with_enable(True).with_expiry_time(
            "1D").with_listen(" ").with_port(1234).with_protocol("vmess").with_uuid(uuid4()).with_network(
            "ws").with_security("tls").with_server_name("v2ray.my-site.com").with_ws_path(
            "/test").with_tag("inbound-49428").with_sniffing(True).build()
        
        _ = await crud.inbounds.create(obj_in=builder)
        
        print(_)

        return _
    
    if __name__ == '__main__':
        import asyncio
        asyncio.run(main())

&nbsp;


### Get all records
Get all records from table.


    from uuid import uuid4

    from xtls_crud.database import crud


    async def main():
        _ = await crud.inbounds.get_multi()
        
        print(_)

        return _
    
    if __name__ == '__main__':
        import asyncio
        asyncio.run(main())

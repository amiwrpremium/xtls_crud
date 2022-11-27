# XTLS CRUD

XTLS CRUD is a CRUD App for [XTLS Xray-core](https://github.com/XTLS/Xray-core) written in Python.

## Features
- Inbounds table model using [SQLAlchemy](https://www.sqlalchemy.org/)
- Inbounds table schema using [Pydantic](https://pydantic-docs.helpmanual.io/)
- Full CRUD operations for inbounds table
- Full builders for each and every step of inbound creation (including Sniffing, StreamSettings, Settings and Inbound)
- Modeled schema for builders
- Async based
- Helpers for traffic allocation for each inbound
- Helpers for time allocation for each inbound

## Installation
Using Poetry:
```bash
poetry install
```


## build
```bash
poetry build
```

## Usage
```python
import asyncio
from xtls_crud.database.crud.crud_inbounds import inbounds


async def get_multi():
    data = await inbounds.get_multi()
    print(data)
    
    return data


if __name__ == "__main__":
    asyncio.run(get_multi())
```

## Environment Variables
- `DEBUG` - Set to `True` to enable debug mode. (Accepts `True`, `False`. Defaults to `False`)
- `ENVIRONMENT` - Set to `development` to enable development mode. (Accepts `dev`, `prod`, `local`. Defaults to `dev`)
- `DATABASE_URL` - Set to the database url. (Accepts any valid sqlite database url. If environment is set to `local` or `dev`, defaults is local sqlite database url, else defaults to `/etc/x-ui/x-ui.db`)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer
This project is not affiliated with XTLS Xray-core in any way.

## TODO
- [ ] Add API using [FastAPI](https://fastapi.tiangolo.com/)

## Changelog
```bash
git log --pretty=format:'%h - %an, %ar : %s' --graph 
```
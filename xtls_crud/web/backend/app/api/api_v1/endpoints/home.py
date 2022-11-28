from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/", include_in_schema=False)
async def home(request: Request):
    data = {
        'message': 'Hello, World!',
        'documentation': {
            'docs': str(request.url) + 'docs/',
            'redoc': str(request.url) + 'redoc/',
        },
        'info': {
            'name': 'XTLS CRUD',
            'description': "A CRUD app for XTLS",
            'version': '0.1.0',
            'author': 'AMiWR',
            'github': 'https://github.com/amiwrpremium/',
            'email': 'amiwrpremium@gmail.com',
        },
    }
    return data

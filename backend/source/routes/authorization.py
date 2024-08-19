from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from source.config.authorization import google_auth_config

oauth = OAuth()
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    client_id=google_auth_config.google_client_id,
    client_secret=google_auth_config.google_client_secret,
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile',
        'prompt': 'consent'
    }
)

router = APIRouter()

@router.get("/login")
async def login(request: Request):
    redirect_uri = 'http://127.0.0.1:8000/auth/callback'
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    id_token = token.get('id_token')

    if not id_token:
        raise HTTPException(status_code=400, detail="No ID token returned by Google")
    
    user = dict(token['userinfo'])
    user = {
        "email": user['email'],
        "name": user['name'],
        "picture": user['picture']
    }
    return JSONResponse(content=user)
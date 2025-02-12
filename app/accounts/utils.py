from typing import Annotated
from fastapi import Depends, Request, HTTPException
from appwrite.client import Client
from appwrite.services.account import Account
from app.config.config import settings
from appwrite.exception import AppwriteException

def get_session_token(request: Request):
    session_token =  request.cookies.get('session_token')
    if session_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        return session_token

async def get_current_user(
    session_token: Annotated[str, Depends(get_session_token)]
):
    client = Client()
    client.set_endpoint(settings.Appwrite_API_ENDPOINT)
    client.set_project(settings.APPWRITE_PROJECT_ID)
    client.set_session(session_token)

    account = Account(client)
    try:
        current_user = account.get()
        return current_user
    except AppwriteException as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.message)

async def get_admin_user(
    current_user: Annotated[any, Depends(get_current_user)],
):
    if 'admin' in current_user['labels']:
        return current_user
    raise HTTPException(status_code=401, detail="Unauthorized")

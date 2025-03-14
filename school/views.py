from django.shortcuts import redirect
from requests_oauthlib import OAuth2Session
from django.http import HttpResponse
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

CLIENT_ID = "7ZxGz6jVivneHJBcVtLwN6MDG1z0FFtvk52QZAOr"
CLIENT_SECRET = "rgR5c3bT0nD32pWiNjzHrbbmoaFwNtDVwxm4qcxqQpgC8HwJfaINC5lR8jOnaKNFwhmbPBZcEgITY1RZnJGJtCgaFn0OdGUNwa9vDt3JnJaJjFHy42fkLG2G1VgsBuUj"
AUTHORIZATION_BASE_URL = "http://localhost:8000/o/authorize/"
TOKEN_URL = "http://localhost:8000/o/token/"
REDIRECT_URI = "http://localhost:8001/oauth/callback/"


def home(request):
    return HttpResponse(
        "Добро пожаловать в School! <a href='/oauth/login/'>Войти через SSO</a>"
    )


def oauth_login(request):
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=["read"])
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
    request.session["oauth_state"] = state
    return redirect(authorization_url)


def oauth_callback(request):
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    token = oauth.fetch_token(
        TOKEN_URL,
        client_secret=CLIENT_SECRET,
        code=request.GET.get("code"),
        state=request.session.get("oauth_state"),
    )
    return HttpResponse("Токен получен: " + str(token))

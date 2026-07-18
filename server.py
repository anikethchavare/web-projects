# web-projects - server.py

"""
Copyright 2026 Aniketh Chavare (anikethchavare@zohomail.in)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Imports
import os
import secrets

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Constants
VERSION = "0.1.0"
SECURITY_HEADERS = {
    "X-Frame-Options": "SAMEORIGIN",
    "X-Content-Type-Options": "nosniff",
    "Permissions-Policy": "geolocation=(), camera=(), microphone=(), payment=(), autoplay=()",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    "Cross-Origin-Opener-Policy": "same-origin"
}

# Initializing the "app" FastAPI Server
app = FastAPI(
    title="web-projects",
    description="The central hub for my live web projects and games, built with FastAPI.",
    version=VERSION,
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0",
    },
    docs_url=None,
    redoc_url=None
)

# Initializing Jinja2
templates = Jinja2Templates(directory="templates")

# Configuring Middleware
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)

# Middleware 1: Security Headers (app)
@app.middleware("http")
async def middleware_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.update(SECURITY_HEADERS)

    return response

# Mounting Assets
app.mount("/js", StaticFiles(directory="templates/js"), name="/js")
app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/images", StaticFiles(directory="templates/images"), name="/images")

# Route 1: Index (app)
@app.get("/")
async def app_index(request: Request):
    return templates.TemplateResponse(request, "index.html", status_code=200)

# Route 2: Favicon (app)
@app.get("/favicon.ico")
async def app_favicon(request: Request):
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/media/favicon.png", status_code=200)

# Route 3: Robots (app)
@app.get("/robots.txt")
async def app_robots(request: Request):
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/robots.txt", status_code=200)

# Route 4: Sitemap (app)
@app.get("/sitemap.xml")
async def app_sitemap(request: Request):
    return FileResponse(os.getcwd().replace(os.sep, "/") + "/sitemap.xml", status_code=200)

# Route 5: About (app)
@app.get("/about")
async def app_about(request: Request):
    return templates.TemplateResponse(request, "about.html", status_code=200)

# Route 6: Tennis (app)
@app.get("/games/tennis")
async def app_games_tennis(request: Request):
    return templates.TemplateResponse(request, "tennis.html", context={
        "css_nonce": secrets.token_urlsafe(32),
        "js_nonce": secrets.token_urlsafe(32)
    }, status_code=200)

# Route 7: Rock Paper Scissors (app)
@app.get("/games/rps")
async def app_games_rps(request: Request):
    return templates.TemplateResponse(request, "rock-paper-scissors.html", context={
        "css_nonce": secrets.token_urlsafe(32),
        "js_nonce": secrets.token_urlsafe(32)
    }, status_code=200)

# Exception Handler 1: 404 (app)
@app.exception_handler(404)
async def app_exception_handler_404(request: Request, exc: HTTPException):
    return templates.TemplateResponse(request, "404.html", context={
        "css_nonce": secrets.token_urlsafe(32)
    }, status_code=404)
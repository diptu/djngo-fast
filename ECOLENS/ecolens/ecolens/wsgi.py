"""
WSGI config for ecolens project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Fast api related settings
# from fastapi import FastAPI

# from app.urls import router as main_router

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecolens.settings")

application = get_wsgi_application()

# Fast api related settings
# from fastapi import FastAPI

# from app.urls import router as main_router

# app = FastAPI(
#     title="fasttest",
#     description="Testing with django-fastapi fuse.",
#     version="We aren't doing versions yet. Point oh.",
# )

# app.include_router(main_router, prefix="/api")

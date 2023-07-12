import uvicorn
from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI(title='Auth Service')

app.include_router(auth_router)

uvicorn.run(app, host="0.0.0.0", port=9000)

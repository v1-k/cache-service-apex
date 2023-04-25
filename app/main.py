from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import cache, user, auth, protected

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(cache.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def root():
    return {"message": "Welcome to Cache service"}

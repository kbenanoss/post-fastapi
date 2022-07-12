from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from . import models

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="Post Project Api",
    description="User can login then view, add, update and delete posts",
    # version="1.0",
    openapi_url="/api/v1/openapi.json"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Posts
app.include_router(post.router)

# Users
app.include_router(user.router)

# Login Users
app.include_router(auth.router)

# Votes
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

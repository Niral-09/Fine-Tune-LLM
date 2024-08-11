from fastapi import FastAPI
from .api.v1 import qa, config

app = FastAPI()

# Include routers for the API
app.include_router(qa.router, prefix="/qa", tags=["qa"])
app.include_router(config.router, prefix="/config", tags=["config"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
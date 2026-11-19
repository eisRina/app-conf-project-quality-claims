
from fastapi import FastAPI

app = FastAPI(
    title="Project Name",
    description="Project description",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/version")
def get_version():
    return {
        "version": "0.1.0",
        "status": "development"
    }

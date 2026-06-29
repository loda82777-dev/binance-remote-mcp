from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/mcp")
def mcp():
    return {
        "name": "Binance Remote MCP",
        "status": "ok"
    }

from fastapi import FastAPI
import socket
import uvicorn

app = FastAPI()

@app.get("/")
async def get_server_info():
    """
    Returns the name of the Azure server
    """
    server_name = socket.gethostname()
    return {"server_name": server_name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

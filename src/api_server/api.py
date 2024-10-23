from fastapi import FastAPI
from pydantic import BaseModel
import websockets

app = FastAPI()

# WebSocket経由でPython WebSocketサーバーにコマンドを送信する関数
async def send_command_to_websocket(command: str, server: str) -> str:
    urls = []
    if server == "":
        urls.append("ws://login_server:8765")  # WebSocketサーバーのURI
        urls.append("ws://game_server:8765")  # WebSocketサーバーのURI
    else:
        urls.append(f"ws://{server}:8765")  # WebSocketサーバーのURI
    response = []
    for url in urls:
        async with websockets.connect(url) as websocket:
            await websocket.send(command)
            response.append(await websocket.recv())
    return response

# APIエンドポイント
@app.get("/api/v1/commands/")
async def send_command(cmd: str, srv: str = ""):
    # WebSocket経由でコマンドを送信し、レスポンスを取得
    response = await send_command_to_websocket(cmd, srv)
    return {"result": response}
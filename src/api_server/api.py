from fastapi import FastAPI
from pydantic import BaseModel
import websockets

app = FastAPI()

# コマンドデータモデル
class Command(BaseModel):
    command: str

# WebSocket経由でPython WebSocketサーバーにコマンドを送信する関数
async def send_command_to_websocket(command: str) -> str:
    uri = "ws://rs_server:8765"  # WebSocketサーバーのURI
    async with websockets.connect(uri) as websocket:
        await websocket.send(command)
        response = await websocket.recv()  # サーバーからのレスポンスを受け取る
        return response

# APIエンドポイント
@app.get("/api/cmd")
async def send_command(cmd: str):
    # WebSocket経由でコマンドを送信し、レスポンスを取得
    response = await send_command_to_websocket(cmd)
    return {"result": response}
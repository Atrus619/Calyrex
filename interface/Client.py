import websockets


class Client:

    websocket = None
    address = None

    @classmethod
    async def create(cls):
        self = Client()
        self.address = "ws://localhost:8000/showdown/websocket"
        self.websocket = await websockets.connect(self.address)
        return self

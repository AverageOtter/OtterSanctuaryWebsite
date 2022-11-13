import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_js = json.loads(text_data)
        message = text_data_js["message"]
        user = text_data_js["user"]
        timenowH = text_data_js["timenowH"]
        timenowM = text_data_js["timenowM"]
        timenowS = text_data_js["timenowS"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": user,
                "timenowH": timenowH,
                "timenowM": timenowM,
                "timenowS": timenowS,
            },
        )

    def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        timenowH = event["timenowH"]
        timenowM = event["timenowM"]
        timenowS = event["timenowS"]
        self.send(
            text_data=json.dumps(
                {
                    "type": "chat",
                    "message": message,
                    "user": user,
                    "timenowH": timenowH,
                    "timenowM": timenowM,
                    "timenowS": timenowS,
                }
            )
        )
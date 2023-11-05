import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class BannerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.room_name = "banner_changer"
        self.room_group_name = "banner_changer_group"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.send(json.dumps({"message": "Connected to the banner websocket"}))

    def receive(self, text_data=None):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "banner_ads_socket",
                "value": f"{text_data}"
            }
        )

    def disconnect(self, code):
        print("DISCONNECTED")

    def banner_ads_socket(self, event):
        self.send(json.dumps({
            "type": "banner_changer",
            "data": event["value"]
        }))

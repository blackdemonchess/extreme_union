from iqoptionapi.ws.chanels.base import Base


class CreateAlert(Base):
    name = "sendMessage"

    def __call__(self, active_id, instrument_type, price, permanent, request_id=''):
        data = {"name": "create-alert", "version": "1.0",
                "body": {"asset_id": active_id,
                         "instrument_type": instrument_type,
                         "type": "price", "value": price,
                         "activations": permanent}}
        self.send_websocket_request(self.name, data, request_id)


class UpdateAlert(Base):
    name = "sendMessage"

    def __call__(self, active_id, alert_id, price, permanent, request_id=''):
        data = {"name": "update-alert", "version": "1.0",
                "body": {"id": alert_id,
                         "asset_id": active_id,
                         "type": "price", "value": price,
                         "activations": permanent}}
        self.send_websocket_request(self.name, data, request_id)


class DeleteAlert(Base):
    name = "sendMessage"

    def __call__(self, alert_id, request_id=''):
        data = {"name": "delete-alert",
                "version": "1.0",
                "body": {"id": alert_id}}
        self.send_websocket_request(self.name, data, request_id)


class SubscribeAlerts(Base):
    name = "sendMessage"

    def __call__(self, request_id=''):
        data = {"name": "get-subscriptions", "version": "1.0",
                "body": {"locale": self.api.profile.locale, "transport": "push"}}
        self.send_websocket_request(self.name, data, request_id)


class GetAlerts(Base):
    name = "sendMessage"

    def __call__(self, asset_id=None, request_id=''):
        # {"name":"sendMessage","request_id":"57","local_time":20179,"msg":{"name":"get-alerts",
        # "version":"1.0","body":{"asset_id":0,"type":""}}}
        data = {"name": "get-alerts", "version": "1.0",
                "body": {"type": ""}}
        if asset_id:
            data["body"]["asset_id"] = asset_id
        self.send_websocket_request(self.name, data, request_id)

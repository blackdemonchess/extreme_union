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

# {"request_id":"122","name":"alert",
# "msg":{"id":183850365,"user_id":54198723,
# "asset_id":1,"instrument_type":"digital-option",
# "type":"price","value":1.18314,"activations":1,
# "timeout":300,"deadline":1606272122,"created_at":1598496122},
# "status":2000}

# {"request_id":"201","name":"alert",
# "msg":{"id":183850365,"user_id":54198723,
# "asset_id":1,"instrument_type":"digital-option",
# "type":"price","value":1.18314,"activations":1,
# "timeout":300,"deadline":1606272122,"created_at":1598496122},
# "status":2000}

# {"name":"alert-changed","microserviceName":"user-alerts",
# "msg":{"reason":"created","id":183850365,"user_id":54198723,
# "asset_id":1,"instrument_type":"digital-option","type":"price",
# "value":1.18314,"activations":1,"timeout":300,"deadline":1606272122,
# "created_at":1598496122}}

# {"name":"alert-triggered","microserviceName":"user-alerts",
# "msg":{"id":190180219,"timestamp":1598496659,"user_id":54198723,
# "asset_id":1,"instrument_type":"digital-option","type":"price",
# "value":1.18266}}

# {"name":"sendMessage","request_id":"1047"
# "msg":{"name":"create-alert","version":"1.0",
# "body":{"asset_id":1,"instrument_type":"turbo","type":"price",
# "value":1.18288,"activations":1}}}

# {"name":"sendMessage","request_id":"1107"
# "msg":{"name":"create-alert","version":"1.0","body":
# {"asset_id":1,"instrument_type":"binary","type":"price",
# "value":1.18376,"activations":1}}}

# {"name":"sendMessage","request_id":"1413"
# "msg":{"name":"update-alert","version":"1.0",
# "body":{"id":183855321,"asset_id":1,"instrument_type":"binary"
# ,"type":"price","value":1.18436,"activations":1}}}

# {"request_id":"1413","name":"alert"
# "msg":{"id":183855321,"user_id":54198723,"asset_id":1,
# "instrument_type":"binary","type":"price","value":1.18436,
# "activations":1,"timeout":300,"deadline":1606273385,"created_at":1598497076},
# "status":2000}

# {"name":"sendMessage","request_id":"1507",
# "msg":{"name":"update-alert","version":"1.0",
# "body":{"id":183855321,"asset_id":1,"instrument_type":"binary",
# "type":"price","value":1.18436,"activations":0}}}

# {"name":"alert-changed","microserviceName":"user-alerts",
# "msg":{"reason":"updated","id":183855321,"user_id":54198723,
# "asset_id":1,"instrument_type":"binary","type":"price","value":1.18436,
# "activations":0,"timeout":300,"deadline":1606273478,"created_at":1598497076}}

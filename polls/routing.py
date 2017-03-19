from channels.staticfiles import StaticFilesConsumer
from . import consumers

channel_routing = {
    'http.request': StaticFilesConsumer(),
    'websocket.connect': consumers.ws_connect,
    'websocket.disconnect': consumers.ws_disconnect,
}
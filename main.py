import json
import os
from handlers.base import MainHandler
from tornado import web, ioloop

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "open_id_certs_url": "https://192.171.139.54.xip.io/auth/realms/master/protocol/openid-connect/certs"
}


def make_app():
    return web.Application([
        (r"/", MainHandler),
    ], **settings)


if __name__ == "__main__":
    print("Starting localhost:6000")
    app = make_app()
    print("App created")
    app.listen(6000)
    print("Listening to 6000")
    ioloop.IOLoop.current().start()
    print("localhost:6000 started")

from tornado import web
from .auth import AuthenticatedRequestHandler


class MainHandler(AuthenticatedRequestHandler):
    def data_received(self, chunk):
        pass

    @web.authenticated
    def get(self):
        self.write('Hi ' + self.current_user['preferred_username'])

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Credentials', True)
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, '
                        'Access-Control-Allow-Methods')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()

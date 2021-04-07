# tornado 作为 wsgi (web server gateway interface)

from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from main import app
from tornado.ioloop import IOLoop


if __name__ == '__main__':
    svr = HTTPServer(WSGIContainer(app))
    svr.listen(9900)
    IOLoop.current().start()

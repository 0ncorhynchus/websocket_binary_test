# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket


class RecieveHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print '[Recieve] opened'

    def on_message(self, message):
        print '[Revieve] %s' % message.decode('zlib')

    def on_close(self):
        print '[Revieve] closing...'


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/recieve', RecieveHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()

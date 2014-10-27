# -*- coding: utf-8 -*-

import websocket

host = 'localhost'
port_ws = '5000'

ws = websocket.create_connection('ws://%s:%s/recieve' % (host, port_ws))
message = 'message in binary'.encode('zlib')
print 'Length of message is %d' % len(message)
print message
ws.send_binary(message)


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

authorizer = DummyAuthorizer()
#authorizer.add_user("user", "12345", "/", perm="elradfmw")
authorizer.add_user("test", "test", "C:\\Users\\yalin.ates\\Desktop\\ftp", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
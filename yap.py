import SocketServer
import socket
import sys

# 0.0.0.0:1157
class EarLobe(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        print "Heard: %s" % self.data

class ThreadedListener(ThreadingMixIn, TCPServer): pass

class Ear:
    def listen(self):
        server = SocketServer.ThreadedListener(('0.0.0.0', 1157), EarLobe)
        server.serve_forever()

class Mouth:
    def talkTo(self, addr):
        self.toEar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.toEar.connect((addr, 1157))

    def say(self, msg):
        self.toEar.sendall(msg + "\n")

    def stopListening(self):
        self.toEar.close()

def talk():
    e = Ear()
    m = Mouth()
    return (e, m)

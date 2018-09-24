from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

     def datagramReceived(self, data, address):
       print("received %r from %s" % (data, address))

# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()

from errors import TcpConnectionError


class DisconnectedState:
    # BEGIN (write your solution here)
    def __init__(self, net):
        self.net = net

    def connect(self):
        self.net.state = self.net.states['connect'](self.net)

    def disconnect(self):
        raise TcpConnectionError('Connection already disconnected')

    def get_current_state(self):
        return "disconnected"

    def write(self, data):
        raise TcpConnectionError('It is not possible write to closed connection')
    # END

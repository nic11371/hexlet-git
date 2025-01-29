from errors import TcpConnectionError


class ConnectedState:
    # BEGIN (write your solution here)
    def __init__(self, net):
        self.net = net

    def get_current_state(self):
        return "connected"

    def connect(self):
        raise TcpConnectionError('Connection already connected')

    def disconnect(self):
        self.net.state = self.net.states['disconnect'](self.net)

    def write(self, data):
        self.net.buffer.append(data)
    # END

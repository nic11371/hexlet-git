from states.connected import ConnectedState
from states.disconnected import DisconnectedState


class TcpConnection:
    # BEGIN
    def __init__(self, ip, port):
        self.states = {
            'disconnected': DisconnectedState,
            'connected': ConnectedState,
        }
        self.ip = ip
        self.port = port
        self.buffer = []
        self.set_state('disconnected')

    def get_current_state(self):
        return self.state.get_name()

    def connect(self):
        self.state.connect()

    def disconnect(self):
        self.state.disconnect()

    def write(self, data):
        self.state.write(data)

    def set_state(self, name):
        self.state = self.states[name](self)
    # END
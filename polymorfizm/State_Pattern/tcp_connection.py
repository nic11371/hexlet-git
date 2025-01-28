from polymorfizm.State_Pattern.states.connected import ConnectedState
from polymorfizm.State_Pattern.states.disconnected import DisconnectedState


class TcpConnection:
    # BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.states = {
            'connect': ConnectedState,
            'disconnect': DisconnectedState
        }
        self.buffer = []
        self.state = self.states['disconnect'](self)

    def connect(self):
        self.state.connect()

    def disconnect(self):
        self.state.disconnect()

    def get_current_state(self):
        return self.state.get_current_state()

    def write(self, data):
        self.state.write(data)
    # END

from errors import TcpConnectionError


class DisconnectedState:
    # BEGIN
    def __init__(self, connection):
        self.connection = connection

    def get_name(self):
        return 'disconnected'

    def connect(self):
        self.connection.set_state('connected')

    def disconnect(self):
        raise TcpConnectionError('Connection already disconnected')

    def write(self, data):
        raise TcpConnectionError('It is not possible write to closed connection')
    # END

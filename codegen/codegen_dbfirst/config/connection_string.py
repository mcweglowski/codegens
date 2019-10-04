class connection_string(object):
    def __init__(self, server, database, connection_mode, user, password):
        self.server          = server
        self.database        = database
        self.connection_mode = connection_mode
        self.user            = user
        self.password        = password


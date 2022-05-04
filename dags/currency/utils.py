import psycopg2


class PQConnect:

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def __enter__(self):
        self.connection = psycopg2.connect(
            user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute_commit(self, command, result=None):
        with self as conn:
            cursor = conn.cursor()
            cursor.execute(command, result)
            conn.commit()

import mysql.connector


class UseDatabase:
    def __init__(self, config: dict) -> None:  # Dict we get from outside
        """Initializes dict as attr"""
        # self.host = host
        # self.user = user
        # self.password = password
        # self.database = database
        # dbparam = {}
        # dbparam['host'] = self.host
        # dbparam['user'] = self.user
        # dbparam['password'] = self.password
        # dbparam['database'] = self.database
        # return dbparam
        self.configuration = config  # Save dict as attr

    def __enter__(self) -> 'Cursor as cur':
        """Create connector and cursor as attr"""
        self.conn = mysql.connector.connect(**self.configuration)  # **say us about params to connection gives us as
        # one dictionary
        self.cur = self.conn.cursor()  # Create cursor
        return self.cur  # Return cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """Close cursor and connector"""
        self.conn.commit()
        self.cur.close()
        self.conn.close()

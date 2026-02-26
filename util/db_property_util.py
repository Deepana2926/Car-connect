class DBPropertyUtil:
    @staticmethod
    def get_property(key):
        props = {
            "db.driver": "SQL Server",
            "db.server": "LAPTOP-C3S3TQVJ\SQLEXPRESS",
            "db.name": "CARCONNECT",
        }
        return props.get(key)

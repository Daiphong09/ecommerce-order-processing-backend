from app.db.connection import get_connection
class UnitOfWork:
    def __enter__(self):
        self.conn = get_connection()
        cursor = self.conn.cursor()
        self.cursor = cursor
        return self
    def commit(self):
        conn = self.conn
        conn.commit()
    def __exit__(self,exc_type, exc_value, traceback):
        conn = self.conn
        cursor = self.cursor
        try:
            conn.rollback()
        finally:
            try:
                cursor.close()
            finally:
                conn.close()
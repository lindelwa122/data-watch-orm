import sqlite3
from helpers.helper import first

class Manager:
    def __init__(self, model, db_path=':memory:'):
        """
        Initialize the Manager with a model and database path.
        
        :param model: The model class this manager is associated with
        :param db_path: Path to the SQLite database file, defaults to in-memory database
        """
        self._model = model
        self._db_path = db_path
        self._conn = None
        self._cursor = None

    def _ensure_connection(self):
        """
        Ensure that a database connection exists, creating one if it doesn't.
        This lazy initialization helps in resource management.
        """
        if not self._conn:
            self._conn = sqlite3.connect(self._db_path)
            self._cursor = self._conn.cursor()

    def all(self):
        # todo
        pass

    def delete(self):
        # todo
        pass

    def get(self):
        # todo
        pass

    def contains(self):
        # todo
        pass
    
    def count(self):
        # todo
        pass

    def create(self):
        # todo
        pass

    def distinct(self):
        # todo
        pass

    def exists(self):
        # todo
        pass

    def get_or_create(self):
        # todo
        pass

    def earliest(self):
        # todo
        pass

    def latest(self):
        # todo
        pass

    def last(self):
        # todo
        pass

    def first(self):
        self._ensure_connection()
        
        table_name = self._model.__name__.lower()
        row = first(self._cursor, table_name)
        if row:
            column_dict = dict(zip([column[0] for column in self._cursor.description], row))
            return self._model(**column_dict)
        return None

    def order_by(self):
        # todo
        pass

    def reverse(self):
        # todo
        pass

    def update(self):
        # todo
        pass

    def create(self):
        # todo
        pass

    def save(self):
        # todo
        pass

    def __del__(self):
        """
        Destructor to ensure the database connection is closed when the Manager instance is deleted.
        """
        if self._conn:
            self._conn.close()

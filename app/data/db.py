import sqlite3
from pathlib import Path

# Define paths relative to the project structure
DATA_DIR = Path("DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    """
    Connect to the SQLite database.
    Creates the database file if it doesn't exist.
    """
    return sqlite3.connect(str(db_path))

# The connection function is simple and only concerns itself with path and connection.

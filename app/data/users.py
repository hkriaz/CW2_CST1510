import sqlite3
import pandas as pd

def insert_user(conn: sqlite3.Connection, username: str, password_hash: str, role: str = 'user'):
    """Insert a new user (used by registration/migration)."""
    cursor = conn.cursor()
    sql = "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)"
    cursor.execute(sql, (username, password_hash, role))
    conn.commit()
    return cursor.lastrowid

def get_user_by_username(conn: sqlite3.Connection, username: str):
    """Retrieve a single user by username (used by login)."""
    query = "SELECT * FROM users WHERE username = ?"
    # Use pandas or fetchone to get the result
    df = pd.read_sql_query(query, conn, params=(username,))
    if not df.empty:
        # Return as a dictionary or a Pandas Series object
        return df.iloc[0].to_dict()
    return None

def update_user_role(conn: sqlite3.Connection, user_id: int, new_role: str):
    """Update a user's role."""
    cursor = conn.cursor()
    sql = "UPDATE users SET role = ? WHERE id = ?"
    cursor.execute(sql, (new_role, user_id))
    conn.commit()
    return cursor.rowcount

# Add more CRUD functions (e.g., get_all_users, delete_user) as needed.

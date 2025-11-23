import pandas as pd
from app.data.db import connect_database 

def insert_incident(conn, date, incident_type, severity, status, description, reported_by=None):
    """
    Insert a new cyber incident into the database. (CREATE)
    """
    cursor = conn.cursor()
    
    # Use parameterized query (CRITICAL for security)
    insert_sql = """
        INSERT INTO cyber_incidents 
        (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    params = (date, incident_type, severity, status, description, reported_by)
    
    cursor.execute(insert_sql, params)
    conn.commit()
    return cursor.lastrowid

def get_all_incidents(conn):
    """
    Retrieve all incidents from the database. (READ)
    """
    # Use pandas for easy data retrieval as a DataFrame
    query = "SELECT * FROM cyber_incidents ORDER BY id DESC"
    df = pd.read_sql_query(query, conn)
    return df

def update_incident_status(conn, incident_id, new_status):
    """
    Update the status of an incident. (UPDATE)
    """
    cursor = conn.cursor()
    # Use parameterized query
    update_sql = "UPDATE cyber_incidents SET status = ? WHERE id = ?"
    params = (new_status, incident_id)
    
    cursor.execute(update_sql, params)
    conn.commit()
    return cursor.rowcount # Returns the number of rows updated

def delete_incident(conn, incident_id):
    """
    Delete an incident from the database. (DELETE)
    """
    cursor = conn.cursor()
    # Use parameterized query
    delete_sql = "DELETE FROM cyber_incidents WHERE id = ?"
    params = (incident_id,)
    
    cursor.execute(delete_sql, params)
    conn.commit()
    return cursor.rowcount # Returns the number of rows deleted

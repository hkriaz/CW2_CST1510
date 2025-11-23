import bcrypt
from pathlib import Path
from app.data.db import connect_database
from app.data.users import get_user_by_username, insert_user 

# The complete implementations for register_user and login_user were provided in the lab.
# The migration function is implemented here.

DATA_DIR = Path("DATA") # Re-define/import DATA_DIR for file access

def migrate_users_from_file(conn, filepath=DATA_DIR / "users.txt"):
    """
    Migrate users from users.txt to the database.
    """
    if not filepath.exists():
        print(f"File not found: {filepath}")
        print("   No users to migrate.")
        return 0
    
    cursor = conn.cursor()
    migrated_count = 0
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Parse line: username,password_hash,role (only use first two for safety)
            parts = line.split(',')
            if len(parts) >= 2:
                username = parts[0]
                password_hash = parts[1]
                role = parts[2] if len(parts) > 2 else 'user' # Safely get role
                
                # Insert user (ignore if already exists)
                try:
                    cursor.execute(
                        "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                        (username, password_hash, role)
                    )
                    if cursor.rowcount > 0:
                        migrated_count += 1
                except Exception as e:
                    print(f"Error migrating user {username}: {e}")
    
    conn.commit()
    print(f"Migrated {migrated_count} users from {filepath.name}")
    return migrated_count

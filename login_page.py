import streamlit as st
import bcrypt
import sqlite3

DB_PATH = "DATA/intelligence_platform.db"

def authenticate_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT password_hash FROM intelligence_platform WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()

    if row is None:
        return False  # user not found

    stored_hash = row[0].encode("utf-8")
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash)


def add_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    try:
        c.execute("INSERT INTO intelligence_platform (username, password_hash) VALUES (?, ?)",
                  (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        return False  # username exists
    finally:
        conn.close()

    return True


st.title("WELCOME!")
st.set_page_config(page_title='CST1510 CW2',
                   page_icon="img/mdi.jpg"
                    )

st.write("Login or sign up to access the latest confidential tech related details :)")

col1, col2 = st.columns(2)

with col1:
    with st.expander("Login"):
        username = st.text_input("Username: ")
        password = st.text_input("Password: ", type="password")

        if st.button("LOGIN"):
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                st.switch_page("pages/home.py")
            else:
                st.write("Incorrect username or password. Try again.")

with col2:
    with st.expander("Sign up"):
        username = st.text_input("Username: ")
        password = st.text_input("Password: ", type="password")
        add_user(username, password)
        st.session_state.logged_in = True
        st.switch_page("pages/home.py")

import streamlit as st
import sqlite3

st.title("TEST")
con = sqlite3.connect('data.db')
cur = con.cursor()
st.write(cur.execute("SELECT name FROM addresses").fetchall())
cur.close()
con.close()
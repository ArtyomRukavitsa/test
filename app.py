import streamlit as st
import sqlite3
import os

st.title("TEST")
con = sqlite3.connect('data.db')
cur = con.cursor()
st.write(cur.execute("SELECT name FROM addresses").fetchall())
st.write(os.environ['SOMETHING'])
cur.close()
con.close()
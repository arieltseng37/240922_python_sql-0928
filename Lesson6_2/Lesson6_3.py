
import streamlit as st
import psycopg2
#  connection = psycopg2.connect(host='piRobert0301.local',database='mydatabase_a30',user='a30',password='raspberry')
#  cursor = connection.cursor()
#  cursor.execute("SELECT version();")
# # db_version = cursor.fetchone()
# # print(db_version)

Connection = psycopg2.connect(
    database="mydatabase_a30",
    user="a30",
    password="raspberry",
    host="piRobert0301.local",  # 通常是 '127.0.0.1' 或 'localhost'
    port="5432")

cursor = Connection.cursor()
cursor.execute("SELECT * FROM stations;")
rows = cursor.fetchall()
names = []
for row in rows:
    names.append(row[2])
    
st.write(names)


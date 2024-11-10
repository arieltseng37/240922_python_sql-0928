import streamlit as st


#連Ariel新加坡的server
import psycopg2
conn = psycopg2.connect(host='dpg-csc90lg8fa8c73frl8kg-a.singapore-postgres.render.com',
     database='render_1028',user='render_1028_user',password='uISe6pSOqtBVPboj2NbgeZRpqUqb49Tl')

cur = conn.cursor()
cur.execute("SELECT * FROM stations;")
rows = cur.fetchall()
names = []
for row in rows:
    names.append(row[2])
#st.write(names)

option = st.selectbox(
    "請選擇您最愛的車站?",
    names
)

st.write("您最愛的是:", option)


import psycopg2

conn = psycopg2.connect("""
    host=rc1a-72x7dd2xeqw4ztpl.mdb.yandexcloud.net
    port=6432
    dbname=db
    user=user
    password=kopkop99
    target_session_attrs=read-write
""")

q = conn.cursor()
q.execute('SELECT version()')  # select * from holiday

print(q.fetchone())

conn.close()

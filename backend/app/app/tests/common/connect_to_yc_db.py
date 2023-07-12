import psycopg2

conn = psycopg2.connect("""
    host=rc1b-zmsljuukbng2apja.mdb.yandexcloud.net
    port=6432
    sslmode=verify-full
    dbname=db
    user=user
    password=kopkop99
    target_session_attrs=read-write
""")

q = conn.cursor()
q.execute('SELECT version()')

print(q.fetchone())

conn.close()
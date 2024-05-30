from psycopg import connect

conn = connect("postgresql://admin:password@127.0.0.1:5432/bn")

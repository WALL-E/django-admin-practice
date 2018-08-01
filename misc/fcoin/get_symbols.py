#!/usr/bin/env python3.6


import fcoin
import MySQLdb


db = MySQLdb.connect("127.0.0.1", "root", "123456", "qos", charset='utf8' )
cursor = db.cursor()

sql = "select a.key, a.secret from app_certification a, app_account b where a.id = b.certification_id order by b.updated_at limit 1"
cursor.execute(sql)
key, secret = cursor.fetchone()
api = fcoin.authorize(key, secret)

symbols = api.symbols()

print(symbols)

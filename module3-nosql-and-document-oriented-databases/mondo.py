import sqlite3
import pymongo

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# extract character list
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

dict = {'characters':characters}

client = pymongo.MongoClient("mongodb://admin:IN2R8P5hwmVS9qhU@cluster0-shard-00-00-ooj9o.mongodb.net:27017,cluster0-shard-00-01-ooj9o.mongodb.net:27017,cluster0-shard-00-02-ooj9o.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db.test.insert_one(dict)

list(db.test.find())
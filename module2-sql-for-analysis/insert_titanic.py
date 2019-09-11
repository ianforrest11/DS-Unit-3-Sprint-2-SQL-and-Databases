import psycopg2
import wget
import pandas as pd
import sqlite3

# define user, dbname, password, and host (from ElephantSQL)

dbname = 'ceforqty'

user = 'ceforqty'

password = 'GYh0O6sCjsdPPgZXg4DRYzL3Y9LDC5gl'

host = 'salt.db.elephantsql.com'


# establish connection to elephantsql
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)


# create cursor
pg_curs = pg_conn.cursor()


# create dataframe
df = pd.read_csv('titanic.csv')
df.columns = ('survived', 'pclass', 'name', 'sex', 'age', 'sib_sp_aboard', 'par_ch_aboard', 'fare')
df['name'] = df['name'].str.replace("'", "")


# establish connection
t_conn = sqlite3.connect('Titanic.sqlite3')
df.to_sql('Titanic', con=t_conn)


# PRAGMA
t_curs.execute('PRAGMA table_info(Titanic);').fetchall()


# create table
create_titanic_table = """
  CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    sex TEXT,
    age REAL,
    sib_sp_aboard INT,
    par_ch_aboard INT,
    Fare REAL
  );
"""


# execute creation of table
pg_curs.execute(create_titanic_table)


# extract people list
people = t_curs.execute('SELECT * FROM Titanic;').fetchall()


# How do we do this for all characters? Loops!
for person in people:
  insert_person = """
    INSERT INTO Titanic
    (survived, pclass, name, sex, age, sib_sp_aboard, par_ch_aboard, fare)
    VALUES """ + str(person[1:]) + ';'
# print(insert_person)
  pg_curs.execute(insert_person)


pg_curs.close()
pg_conn.commit()
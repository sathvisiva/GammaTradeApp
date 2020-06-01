import sqlite3
from pandas import DataFrame

conn = sqlite3.connect('TestDB2.db')
c = conn.cursor()

create_command = 'CREATE TABLE CARS (Brand text, Price number)'

tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='CARS'"
if not conn.execute(tb_exists).fetchone():
    c.execute(create_command)

conn.commit()

Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = DataFrame(Cars, columns= ['Brand', 'Price'])
df.to_sql('CARS', conn, if_exists='replace', index = False)

print (df)

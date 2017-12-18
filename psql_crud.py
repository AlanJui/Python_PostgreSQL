import psycopg2
from sqlalchemy import create_engine

def list_all_records(table_name):
    result_set = db.execute("SELECT * FROM " + table_name)
    for row in result_set:
        print(row)
    print('=================================================\n\n')


# db_string = 'postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose'
db_string = 'postgres://my_project_user:Passw0rd@localhost:5432/my_project'

db = create_engine(db_string)

# Create table if not exist
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

# Create
# db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")
# db.execute("INSERT INTO films (title, director, year) VALUES ('So this is Christmas', 'Celine Dion', '2011')")
db.execute("INSERT INTO films (title, director, year) VALUES ('To Be Deleted', 'Alan Jui', '2017')")

# Read
list_all_records('films')

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
list_all_records('films')

# Delete
db.execute("DELETE FROM films WHERE title='To Be Deleted'")
list_all_records('films')

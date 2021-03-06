"""
Create, Read, Update, and Delete using the SQL ORM
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://my_project_user:Passw0rd@localhost:5432/my_project"

db = create_engine(db_string)
base = declarative_base()

class Film(base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
session.add(doctor_strange)
youtube_video = Film(title="So this is Christmas", director="Celine Dion", year="2011")
session.add(youtube_video)
session.commit()

# Read
films = session.query(Film)
for film in films:
    print(film.title)

# Update
doctor_strange.title = "Some2016Film"
session.commit()

# Delete
session.delete(doctor_strange)
session.commit()
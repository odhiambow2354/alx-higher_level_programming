#!/usr/bin/python3
"""
Lists State objects containing the letter 'a' from the database using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create a session class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Query and print State objects containing 'a'
    s_tate = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()

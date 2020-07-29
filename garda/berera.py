import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql://root:Abigail20!@localhost/berera")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)

    for origin, destination, duration in reader:
        # print(list(reader))
        db.execute("INSERT into erkab values(:origin, :destination, :duration)",
                   {"origin": origin, "destination": destination, "duration": duration})
        
        print(f"Added flights from {origin} to {destination} with a duration of {duration} minutes")
        db.commit()
    
    
if __name__ == "__main__":
    main()

































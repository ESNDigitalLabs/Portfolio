from connect import *
 
def insert_films():
    try:
 
        # filmID", "title", "yearReleased", "rating", "duration", "genre"
        # filmID is auto increment field no data is required as an input
        fID = input("Enter film ID: ")
        fTitle = input("Enter film Title: ")
        fYearReleased = input("Enter film Release Year: ")
        fRating = input("Enter film Rating: ")
        fDuration = input("Enter film duration in minutes: ")
        fGenre = input("Enter film Genre: ")
 
        dbCursor.execute("INSERT INTO tblfilms VALUES(NULL,?,?,?)", (fID, fTitle, fYearReleased, fRating, fDuration, fGenre))
        # dbCursor.execute("INSERT INTO tblfilms (filmID, title, yearreleased, rating, duration, genre) VALUES(NULL,?,?)", (fID, fTitle, fYearReleased, fRating, fDuration, fGenre))
        dbCon.commit()
        print(f"{fTitle} inserted in the film table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    except sql.Error as er:
        print(f"This error occurs: {er}")
if __name__ == "__main__":   
    insert_films()
 

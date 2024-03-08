
from connect import *
 
def all_films():
    try:
        # try to execute the sql statement below
        # dbCursor.execute("SELECT * FROM songs")
 
        allfilms = dbCursor.execute("SELECT * FROM tblfilms").fetchall()
 
        # fetch all selected data(rows)
        # allsongs = dbCursor.fetchall() # Fetchall fetches all the rows from the table
        allfilms = dbCursor.execute("SELECT * FROM tblfilms").fetchall()
        if allfilms:
            # format output
            #          0       1       2            3           4       5
            print("filmID | title | yearReleased | rating | duration | genre")
            print("*" * 60)
 
            for aFilm in allfilms:
                print(f"{aFilm[0]:<7} | {aFilm[1]:<10} | {aFilm[2]:<7} | {aFilm[3]:<5} | {aFilm[4]:<5} | {aFilm[5]:<10}")
        else:
            print("No films found in the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")
if __name__ == "__main__":
    all_films()
 
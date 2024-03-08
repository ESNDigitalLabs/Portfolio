from connect import *
def search_films():
        try:
                #ask for the field to search by
            field = input("Search by filmID, Title, Rating, Genre: ")

            if field == "filmID":
                # search by filmID
                idInput = int(input("Enter filmID: "))
                dbCursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (idInput,))
                row = dbCursor.fetchone()

                if row is None:
                    # if the filmID entered is not in the table 
                    print(f"No record with filmID {idInput} exists")
                else:
                    # if the filmID entered is exiata in the table 
                    for aFilm in row:
                        print(aFilm)

            elif field in ["Title", "Rating", "Genre"]:
                # search by Title, Ratingt, Genre
                strInput= input(f"Enter the value for the field {field}: ")
                #SELECT * FROM tblfilms WHERE "Title", "Rating", "Genre"  LIKE "Stepfather II" or "18" or "Horror|Thriller"?
                


                dbCursor.execute(f"SELECT * FROM tblfilms WHERE {field} LIKE '%{strInput}%'")
                # dbCursor.execute(f"SELECT * FROM tblfilms WHERE {field} LIKE '", (f"'%{strInput}%"))
                rows = dbCursor.fetchall()
                for aRecord in rows:
                    
                    print(aRecord)

                if not rows:
                    print(f"No record with field {field} matching {strInput} ")

            else: # where the search input is not  filmID, Title, Rating, Genre
                print(f"Search field {field} invalid !")
        except sql.OperationalError as e:
            print(f"Failed because: {e}")
        except sql.ProgrammingError as pe:
            print(f"Not working because: {pe}")
        finally:
            print("DB operation performed")
if __name__ == "__main__":
    search_films()
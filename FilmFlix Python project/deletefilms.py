from connect import *
 
def delete_aFilm():
    try:
        #check if the film id exists
        filmID  = int(input("Enter the filmID to delete a film : "))
        dbCursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {filmID}")
 
        row = dbCursor.fetchone()
 
        if row == None:
            print(f"filmID {filmID} does not exits")
        else:
            dbCursor.execute("DELETE FROM tblfilms WHERE filmID = ?", (filmID,))
            dbCon.commit()
            print(f"The film {filmID} deleted from the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed. ")
if __name__ == "__main__":   
    delete_aFilm()
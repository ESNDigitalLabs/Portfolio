from connect import *
from readfilms import *
 
def dump_data():
    # open the file
    with open("Python/FilmFlix Python project/tblfilms.sql") as dumpfile:
        # read the open file(dumpfile) and save it contents to sqlInsertScript variable
        sqlInsertScript = dumpfile.read()
 
        # write the content found/stored in the sqlInsertScript variable
        dbCursor.executescript(sqlInsertScript)
        # now call the all_songs function from the readsongs file to display updated records
        # all_films()
 
dump_data()
     
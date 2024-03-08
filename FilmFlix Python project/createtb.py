from connect import *   # import all variables/functions from the connect.py file

dbCursor.execute("""
create table "tblfilms" (
	"filmID" VARCHAR(7) NOT NULL,
	"title" VARCHAR(50),
	"yearReleased" INTEGER,
	"rating" VARCHAR(3),
	"duration" INTEGER,
	"genre" VARCHAR(50),
    PRIMARY KEY("filmID")
)""")
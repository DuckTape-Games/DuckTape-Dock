###############
### IMPORTS ###
###############

import sqlite3 as sql #Database used for the project
from utils.helpers import resource_path #Used for pyinstaller to get the true path


#######################
### DATABASE SETUP ####
#######################

#Connects database.db
database = sql.connect(resource_path("database/database.db"))

#Creates a cursor object that executes sql code
cursor = database.cursor()


###########################
### STARTS THE DATABASE ###
###########################
def initialize_database():
    #Enables foreign keys
    database.execute("PRAGMA foreign_keys = on;")


    ######################
    ### CREATES TABLES ###
    ######################

    #Creates the Apps Table
    cursor.execute("""--sql
    CREATE TABLE IF NOT EXISTS Apps(
        appID INTEGER PRIMARY KEY AUTOINCREMENT,
        appName TEXT NOT NULL,
        appCommand TEXT NOT NULL,
        appIcon TEXT,
        appType TEXT,
        appSortIndex INTEGER
    );""")

    #Creates the Groups Table
    cursor.execute("""--sql
    CREATE TABLE IF NOT EXISTS Groups(
        groupID INTEGER PRIMARY KEY AUTOINCREMENT,
        groupName TEXT NOT NULL,
        groupSortIndex INTEGER              
    );""")

    #Creates the AppGroups Table
    #This is the junction table between apps and groups
    cursor.execute("""--sql
    CREATE TABLE IF NOT EXISTS AppGroups(
        appID INTEGER NOT NULL,
        groupID INTEGER NOT NULL,
        appGroupSortIndex INTEGER,
                
        PRIMARY KEY (appID, groupID),

        FOREIGN KEY (appID) REFERENCES Apps (appID) ON DELETE CASCADE,
        FOREIGN KEY (groupID) REFERENCES Groups (groupID) ON DELETE CASCADE
    );""")

    #Saves the changes to the database
    database.commit()


###################
### ADD QUERIES ###
###################

#Add App
def add_app(appName, appCommand, appIcon, appType, appSortIndex):
    query = """INSERT INTO Apps (appName, appCommand, appIcon, appType, appSortIndex) VALUES (?,?,?,?,?);"""
    cursor.execute(query, (appName, appCommand, appIcon, appType, appSortIndex))
    database.commit()
    return cursor.lastrowid

#Add Group
def add_group(groupName, groupSortIndex):
    query = """INSERT INTO Groups (groupName, groupSortIndex) VALUES (?,?);"""
    cursor.execute(query, (groupName, groupSortIndex))
    database.commit()
    return cursor.lastrowid

#Add AppGroup
def add_app_group(appID, groupID, appGroupSortIndex):
    query = """INSERT INTO AppGroups (appID, groupID, appGroupSortIndex) VALUES (?,?,?);"""
    cursor.execute(query, (appID, groupID, appGroupSortIndex))
    database.commit()


########################
### SELECT FUNCTIONS ###
########################

#Returns all Apps
def get_all_apps():
    query = """SELECT * FROM Apps;"""
    cursor.execute(query)
    return cursor.fetchall()

#Returns all groups
def get_all_groups():
    query = """SELECT * FROM Groups;"""
    cursor.execute(query)
    return cursor.fetchall()

#Returns all AppGroups
def get_all_app_groups():
    query = """SELECT * FROM AppGroups;"""
    cursor.execute(query)
    return cursor.fetchall()

#Returns all apps in a specific group
def get_apps_in_group(groupID):
    query = """--sql
    SELECT Apps.* FROM Apps
    JOIN AppGroups ON Apps.appID = AppGroups.appID
    WHERE AppGroups.groupID = ?
    ORDER BY AppGroups.appGroupSortIndex;
    """
    cursor.execute(query, (groupID,))
    return cursor.fetchall()


########################
### DELETE FUNCTIONS ###
########################

#Deletes an app based on the appID
def delete_app(appID):
    query = """DELETE FROM Apps WHERE appID = ?;"""
    cursor.execute(query, (appID,))
    database.commit()

#Deletes a group based on the groupID
def delete_group(groupID):
    query = """DELETE FROM Groups WHERE groupID = ?;"""
    cursor.execute(query, (groupID,))
    database.commit()

#Deletes an appGroup based on both the appID and the groupID
def delete_app_group(appID, groupID):
    query = """DELETE FROM AppGroups WHERE appID = ? AND groupID = ?;"""
    cursor.execute(query, (appID, groupID))
    database.commit()


########################
### UPDATE FUNCTIONS ###
########################

#Updates an app
def update_app(appID, appName, appCommand, appIcon, appType, appSortIndex):
    query = """--sql
    UPDATE Apps SET
        appName = ?,
        appCommand = ?,
        appIcon = ?,
        appType = ?,
        appSortIndex = ?
    WHERE appID = ?;
    """
    cursor.execute(query, (appName, appCommand, appIcon, appType, appSortIndex, appID))
    database.commit()

#Updates a group
def update_group(groupID, groupName, groupSortIndex):
    query = """--sql
    UPDATE Groups SET
        groupName = ?,
        groupSortIndex = ?
    WHERE groupID = ?;
    """
    cursor.execute(query, (groupName, groupSortIndex, groupID))
    database.commit()

#Updates an appGroup
def update_app_group(appID, groupID, appGroupSortIndex):
    query = """--sql
    UPDATE AppGroups SET appGroupSortIndex = ?
    WHERE appID = ? AND groupID = ?;    
    """
    cursor.execute(query, (appGroupSortIndex, appID, groupID))
    database.commit()


###########################
### CLOSES THE DATABASE ###
###########################

def close_database():
    database.commit()
    database.close()
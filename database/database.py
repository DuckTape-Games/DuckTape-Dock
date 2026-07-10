###############
### IMPORTS ###
###############

import sqlite3 as sql #Database used for the project
from utils.helpers import resource_path #Used for pyinstaller to get the true path
from utils.helpers import load_query #Used to load sql queries from the database/queries directory

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
    cursor.execute(load_query("create_apps_table.sql"))

    #Creates the Groups Table
    cursor.execute(load_query("create_groups_table.sql"))

    #Creates the AppGroups Table
    #This is the junction table between apps and groups
    cursor.execute(load_query("create_app_groups_table.sql"))

    #Saves the changes to the database
    database.commit()


###################
### ADD QUERIES ###
###################

#Add App
def add_app(appName, appCommand, appIcon, appType, appSortIndex):
    query = load_query("add_app.sql")
    cursor.execute(query, (appName, appCommand, appIcon, appType, appSortIndex))
    database.commit()
    return cursor.lastrowid

#Add Group
def add_group(groupName, groupSortIndex):
    query = load_query("add_group.sql")
    cursor.execute(query, (groupName, groupSortIndex))
    database.commit()
    return cursor.lastrowid

#Add AppGroup
def add_app_group(appID, groupID, appGroupSortIndex):
    query = load_query("add_app_group.sql")
    cursor.execute(query, (appID, groupID, appGroupSortIndex))
    database.commit()


########################
### SELECT FUNCTIONS ###
########################

#Returns all Apps
def get_all_apps():
    query = load_query("get_all_apps.sql")
    cursor.execute(query)
    return cursor.fetchall()

#Returns all groups
def get_all_groups():
    query = load_query("get_all_groups.sql")
    cursor.execute(query)
    return cursor.fetchall()

#Returns all AppGroups
def get_all_app_groups():
    query = load_query("get_all_app_groups.sql")
    cursor.execute(query)
    return cursor.fetchall()

#Returns all apps in a specific group
def get_apps_in_group(groupID):
    query = load_query("get_apps_in_group.sql")
    cursor.execute(query, (groupID,))
    return cursor.fetchall()


########################
### DELETE FUNCTIONS ###
########################

#Deletes an app based on the appID
def delete_app(appID):
    query = load_query("delete_app.sql")
    cursor.execute(query, (appID,))
    database.commit()

#Deletes a group based on the groupID
def delete_group(groupID):
    query = load_query("delete_group.sql")
    cursor.execute(query, (groupID,))
    database.commit()

#Deletes an appGroup based on both the appID and the groupID
def delete_app_group(appID, groupID):
    query = load_query("delete_app_group.sql")
    cursor.execute(query, (appID, groupID))
    database.commit()


########################
### UPDATE FUNCTIONS ###
########################

#Updates an app
def update_app(appID, appName, appCommand, appIcon, appType, appSortIndex):
    query = load_query("update_app.sql")
    cursor.execute(query, (appName, appCommand, appIcon, appType, appSortIndex, appID))
    database.commit()

#Updates a group
def update_group(groupID, groupName, groupSortIndex):
    query = load_query("update_group.sql")
    cursor.execute(query, (groupName, groupSortIndex, groupID))
    database.commit()

#Updates an appGroup
def update_app_group(appID, groupID, appGroupSortIndex):
    query = load_query("update_app_group.sql")
    cursor.execute(query, (appGroupSortIndex, appID, groupID))
    database.commit()


###########################
### CLOSES THE DATABASE ###
###########################

def close_database():
    database.commit()
    database.close()
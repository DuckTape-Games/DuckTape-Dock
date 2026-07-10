CREATE TABLE IF NOT EXISTS AppGroups(
    appID INTEGER NOT NULL,
    groupID INTEGER NOT NULL,
    appGroupSortIndex INTEGER,
            
    PRIMARY KEY (appID, groupID),

    FOREIGN KEY (appID) REFERENCES Apps (appID) ON DELETE CASCADE,
    FOREIGN KEY (groupID) REFERENCES Groups (groupID) ON DELETE CASCADE
);
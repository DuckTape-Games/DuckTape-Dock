CREATE TABLE IF NOT EXISTS Apps(
    appID INTEGER PRIMARY KEY AUTOINCREMENT,
    appName TEXT NOT NULL,
    appCommand TEXT NOT NULL,
    appIcon TEXT,
    appType TEXT,
    appSortIndex INTEGER
);
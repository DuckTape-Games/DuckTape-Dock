UPDATE Apps SET
    appName = ?,
    appCommand = ?,
    appIcon = ?,
    appType = ?,
    appSortIndex = ?
WHERE appID = ?;
SELECT Apps.* FROM Apps
JOIN AppGroups ON Apps.appID = AppGroups.appID
WHERE AppGroups.groupID = ?
ORDER BY AppGroups.appGroupSortIndex;
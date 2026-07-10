SELECT * FROM AppGroups
JOIN Apps ON Apps.appID = AppGroups.appID
JOIN Groups ON Groups.groupID = AppGroups.groupID
ORDER BY Groups.groupSortIndex ASC, AppGroups.appGroupSortIndex ASC;
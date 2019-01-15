SELECT Request_at as Day,
       ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
      AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Request_at;


SELECT Request_at as Day,
    ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(id), 2) as 'Cancellation Rate'
FROM Trips
JOIN Users ON trips.client_id = users.users_id AND banned = 'No'
WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at;

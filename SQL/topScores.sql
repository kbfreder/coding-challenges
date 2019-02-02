/* https://www.hackerrank.com/challenges/contest-leaderboard/problem

The total score of a hacker is the sum of their maximum scores for all of the challenges.
Write a query to print the hacker_id, name, and total score of the hackers
ordered by the descending score. If more than one hacker achieved the same total score,
then sort the result by ascending hacker_id. Exclude all hackers with a total
score of 0 from your result.

*/

SELECT x.hacker_id, h.name, SUM(max_score) as total_score
FROM (
    SELECT challenge_id, hacker_id, MAX(score) as max_score
    FROM submissions
    GROUP BY challenge_id, hacker_id) AS x
JOIN hackers as h on x.hacker_id = h.hacker_id
GROUP BY x.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, x.hacker_id ASC

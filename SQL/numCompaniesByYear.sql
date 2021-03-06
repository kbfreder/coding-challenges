/*
https://mode.com/sql-tutorial/sql-datetime-format/
https://modeanalytics.com/editor/kbfreder/reports/c755d90a1c4c

Write a query that counts the number of companies acquired within 3 years, 5 years,
and 10 years of being founded (in 3 separate columns). Include a column for total
companies acquired as well. Group by category and limit to only rows with a founding date.

*/


SELECT CASE WHEN x.category_code IS NULL THEN 'No category' ELSE x.category_code END,
  COUNT(*) AS total_companies,
  SUM(CASE WHEN x.time_delta > INTERVAL '3 years' THEN 1 ELSE 0 END) AS years_3,
  SUM(CASE WHEN x.time_delta > INTERVAL '5 years' THEN 1 ELSE 0 END) AS years_5,
  SUM(CASE WHEN x.time_delta > INTERVAL '10 years' THEN 1 ELSE 0 END) AS years_10
FROM (
  SELECT c.category_code, acquired_at_cleaned - founded_at_clean::timestamp AS time_delta
  FROM tutorial.crunchbase_acquisitions_clean_date AS a
  JOIN tutorial.crunchbase_companies_clean_date AS c
  ON a.company_permalink = c.permalink
  WHERE c.founded_at_clean IS NOT NULL
  ) AS x
GROUP BY x.category_code
ORDER BY total_companies DESC

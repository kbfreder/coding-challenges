SQL problems

- Given table:

  Test (

  ​	num INTEGER(4)

  );

  write a SQL statements that returns the max value of *num* without using an aggregate (e.g. MAX, MIN) or `ORDER BY`.









answers:

- Self-join where b < a, and select DISTINCT num NOT IN result
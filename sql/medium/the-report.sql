-- https://www.hackerrank.com/challenges/the-report/problem

SELECT CASE WHEN grade<8 THEN "NULL" ELSE name END AS name, grade, marks from (
SELECT name,marks,(SELECT grade FROM grades WHERE s.marks BETWEEN min_mark and max_mark) AS grade FROM students s
) AS ss
ORDER BY grade DESC, name
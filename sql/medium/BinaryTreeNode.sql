

WITH RECURSIVE cte AS
(
  SELECT n,p, 1 lvl FROM bst WHERE p IS NULL
  UNION ALL
  SELECT b.n,b.p, lvl+1 FROM bst b INNER JOIN cte c ON b.p = c.n
)
SELECT
n,
CASE
    WHEN lvl = 1  THEN "Root"
    WHEN lvl < (SELECT MAX(lvl) FROM cte) THEN "Inner"
    ELSE "Leaf"
    END as type
FROM cte  ORDER BY n  ;
-- /
SELECT
    N AS node,
    CASE
            WHEN P IS NULL THEN 'Root'
            WHEN N IN (SELECT P FROM BST) THEN 'Inner'
            ELSE 'Leaf'
            END AS type
FROM BST
ORDER BY node;
-- The first column is an alphabetically ordered list of Doctor names.
-- The second column is an alphabetically ordered list of Professor names.
-- The third column is an alphabetically ordered list of Singer names.
-- The fourth column is an alphabetically ordered list of Actor names.
-- The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with NULL values.

SELECT MAX(CASE WHEN Occupation = "Doctor" THEN Name END) as "Doctor", MAX(CASE WHEN Occupation = "Professor" THEN Name END) as "Professor", MAX(CASE WHEN Occupation = "Singer" THEN Name END) as "Singer", MAX(CASE WHEN Occupation = "Actor" THEN Name END) as "Actor" FROM(
SELECT Name, Occupation, Rank() OVER(Partition By Occupation Order By Name) as rnumber FROM OCCUPATIONS
) as temp
GROUP BY temp.rnumber
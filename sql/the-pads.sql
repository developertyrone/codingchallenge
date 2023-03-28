(SELECT CONCAT(name, "(", SUBSTRING(occupation, 1, 1),")") FROM occupations ORDER BY name LIMIT 1000)
UNION
(SELECT CONCAT("There are a total of ",parsed.count," ",parsed.occu,"s.") FROM(
SELECT LOWER(occupation) occu, COUNT(*) count FROM occupations GROUP BY occupation ORDER BY COUNT(*), occu) parsed );
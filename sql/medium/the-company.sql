-- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

/*
Enter your query here.
*/

SELECT
company_code,
founder,
(SELECT COUNT(DISTINCT lead_manager_code) FROM lead_manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT senior_manager_code) FROM senior_manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT manager_code) FROM manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT employee_code) FROM employee WHERE company_code = c.company_code)
FROM
company c ORDER BY company_code;

-------------------
SELECT
    company_code,
    founder,
    COUNT(DISTINCT lead_manager_code),
    COUNT(DISTINCT senior_manager_code),
    COUNT(DISTINCT manager_code),
    COUNT(DISTINCT employee_code)
FROM company NATURAL RIGHT JOIN employee
GROUP BY company_code, founder
ORDER BY company_code;
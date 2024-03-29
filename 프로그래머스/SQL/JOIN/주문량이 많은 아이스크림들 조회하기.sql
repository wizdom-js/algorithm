SELECT F.FLAVOR
FROM FIRST_HALF AS F JOIN JULY AS J
ON F.FLAVOR = J.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;

WITH A AS (
    SELECT * FROM FIRST_HALF
    UNION ALL
    SELECT * FROM JULY)

SELECT FLAVOR FROM A
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3;
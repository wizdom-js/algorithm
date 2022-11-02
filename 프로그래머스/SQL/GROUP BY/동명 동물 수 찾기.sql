SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME HAVING COUNT >= 2
ORDER BY NAME;

-- COUNT(특정컬럼)는 null을 세지 않는다. 그런데 Count(*)는 null값을 포함하여 count한다.
-- 따라서 문제에서 이름이 null인 데이터가 있으므로,  count(*)를 사용하려면 where 절로 null 처리 해줘야한다.
SET @TIME := -1;

SELECT (@TIME := @TIME + 1) AS HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @TIME) AS COUNT
FROM ANIMAL_OUTS
WHERE @TIME < 23;
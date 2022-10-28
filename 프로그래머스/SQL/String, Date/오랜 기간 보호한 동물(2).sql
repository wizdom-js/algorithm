SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A INNER JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(B.DATETIME, A.DATETIME) DESC
LIMIT 2

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY TIMESTAMPDIFF(DAY, I.DATETIME, O.DATETIME) DESC
LIMIT 2;

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2;
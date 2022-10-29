SELECT P.PRODUCT_ID, P.PRODUCT_NAME,
    (P.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT AS P JOIN
    (SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
    FROM FOOD_ORDER
    WHERE PRODUCE_DATE LIKE '2022-05%'
    GROUP BY PRODUCT_ID) AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;

SELECT P.PRODUCT_ID, P.PRODUCT_NAME,
    SUM(P.PRICE * O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT AS P JOIN FOOD_ORDER AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY P.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;
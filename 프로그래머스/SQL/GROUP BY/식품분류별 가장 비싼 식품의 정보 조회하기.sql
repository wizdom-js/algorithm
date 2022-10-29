SELECT A.CATEGORY, A.PRICE AS MAX_PRICE, A.PRODUCT_NAME
FROM FOOD_PRODUCT AS A JOIN
    (SELECT CATEGORY, MAX(PRICE) AS PRICE
     FROM FOOD_PRODUCT
     GROUP BY CATEGORY
    ) AS B
ON A.CATEGORY = B.CATEGORY AND A.PRICE = B.PRICE
WHERE A.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;
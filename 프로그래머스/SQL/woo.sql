-- A는 사람정보 테이블, B는 송금정보 테이블
SELECT A.NAME
FROM TEMP1 AS A
-- 해당 날짜에 구름이한테 송금한 사람만 가져오기
LEFT JOIN
    (SELECT SEND_FROM
    FROM TEMP2
    WHERE SEND_TO = (SELECT USER_ID FROM TEMP1 WHERE NAME = "구름이")
    AND 날짜 = "2000-00-00"
    ) AS B
-- 보낸사람 기준으로 맞춰서 조인했음
ON A.USER_ID = B.SEND_FROM
-- 구름이가 다시 돌려준 사람들의 아이디를 조회, 거기에 들어있지 않는 사람이 오류난 사람들이 됨
WHERE B.SEND_FROM NOT IN
    (SELECT SEND_TO
    FROM TEMP2
    WHERE SEND_FROM = (SELECT USER_ID FROM TEMP1 WHERE NAME = "구름이")
    AND SEND_FROM NOT NULL
    AND 날짜 = "2000-00-00"
    )
ORDER BY USER_ID
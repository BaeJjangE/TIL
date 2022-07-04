# My SQL 기본 사용법

## 추천 사이트

```mysql
1. 얄팍한 코딩사전
https://www.yalco.kr/@sql/1-1/
```

## 기본

```mysql
1. ;
- 쿼리문 끝에 ';' 적어줘야 쿼리문이 끝났다는 뜻

2. *(에스터리스크)
- 전체를 뜻함

3 .쿼리문 블럭씌우면 그것만 실행가능

4. as 원하는이름
- 컬럼 이름 설정

5. 주석달기
-- 주석달기
긴 주석 달기
/*
내용1
내용2
*/

```

## 조회

```mysql
# SHOW DATABASES
- 현재 서버에 어떤 DB가 있는지 보기

# USE DB이름
- DB를 사용하겠다고 명시
- or 원하는 DB 더블클릭해줘도됨

# SHOW TABLES
- 데이터베이스의 테이블 이름 보기

# SHOW TABLE STATUS
- 테이블의 정보 보기

# DESCRIBE(DESC) 테이블명
- 컬럼이름, 컬럼들의 타입, 각각의 열에대한 정보

# SELECT 컬럼이름(전체: *) FROM 테이블이름
- 테이블로부터 원하는 컬럼들을 다 보여달라

# ★SELECT CASE WHEN
- 가공해서 조회
ex)
select case when 컬럼명 <= 100000 then '10만이하'
			when 컬럼명 <= 200000 then '20만이하'
			else '20만 초과' end as P2, 붙이고싶은컬럼명(보통같은컬럼)
from city;

# ★substr()
- 글자 추출
ex)
select 
substr(컬럼이름, 1) as 이름1, -- 첫글자부터 추출
substr(컬럼이름, -1) as 이름_1, -- 맨 끝 글자 추출
substr(컬럼이름, 2, 1) as 이름2, -- 2번째글자부터 1개
substr(컬럼이름, 2, 2) as 이름3 -- 2번째글자부터 2개
from 테이블명;

# concat
- 컬럼 value값, 직접 입력값 합치기
ex) 2개 컬럼 합치기
select 
concat(컬럼이름1, 컬럼이름2) as 생성할컬럼이름
from 테이블;
ex) 3개 합치기
select 
concat(Name, CountryCode) as 이름이랑코드,
concat(Name, '원하는텍스트', CountryCode) as 3개넣기
from city;

# WHERE
SELECT 컬럼이름 FROM 테이블이름 WHERE 조건
- 조회한 결과에 특정한 조건으로 원하는 데이터만 보고 싶을 때 사용
ex)
select *
FROM city
where Population > 8000000;
- 관계, 조건 연산자 사용 가능
 - OR, AND NOT, >, <, =, != 등
ex)
select *
FROM city
where Population < 8000000
AND Population > 7000000;

# between
ex)
select *
FROM city
where Population between 7000000 and 8000000;

# IN
ex) Name 컬럼 안에 있는 'seoul', 'New York', 'Tokyo' 만 볼래
select *
FROM city
where Name IN('seoul', 'New York', 'Tokyo')

# LIKE
- 문자열의 내용 검색하기 위해 사용
ex) '_'사용: 모든 문자열 중 하나 검색
select *
FROM city
where CountryCode LIKE 'KO_'
ex) '%'사용: 어떤 것이든 올 수 있음
select *
FROM city
where CountryCode LIKE 'K%'
    				
# Order by
- 결과가 출력되는 순서를 조절하는 구문
- 디폴트: 오름차순 열이름 뒤에 ASC(생략가능)
- 내림차순: 열 이름 뒤에 DESC 적어줄것
ex)
SELECT *
From city
order by CountryCode ASC, Population DESC

# DISTINCT
- 중복된 것은 1개씩만 보여주면서 출력
- 테이블의 크기가 클수록 효율적
- GROUP BY 와 달리 집계함수가 사용되지 않습니다.
- GROUP BY 와 달리 정렬하지 않으므로 더 빠릅니다.
ex)
SELECT DISTINCT Country, City -- 두 컬럼도 사용 가능
FROM Customers
ORDER BY Country, City;

# LIMIT
- 출력 개수를 제한
- 상위의 N개만 출력하는 'LIMIT N' 구문
- 서버의 처리량을 많이 사용해 서버의 전반적인 성능을 나쁘게하는 악성 쿼리문 개선할 때 사용
ex)
select *
from city
order by Population Desc
Limit 0, 10 -- 0부터 10개까지, 만약 30, 10으로 쓰면 30부터 10개 출력

# GROUP BY
- 그룹으로 묶어주는 역할
- '집계함수'를 함께 사용: NULL값 제외
 - AVG()
 - MIN()
 - MAX()
 - COUNT(): 행의 개수
 - COUNT(DISTINCT): 중복 제외 행의 개수
 - stddev(): 표준 편차
 - variance(): 분산
- 효율적인 데이터 그룹화
- 읽기 좋게 하기 위해 별칭 사용
ex) as로 컬럼값 Average로 변경도 가능
select CountryCode,  max(Population) as 'Average'
from city
group by CountryCode

# HAVING
- WHERE는 그룹하기 전 데이터, HAVING은 그룹 후 집계에 사용
- 집계 함수에 대해서 조건 제한하는 편리한 개념
- HAVING절은 반드시 GROUP BY절 다음에 나와야함
ex)
select CountryCode, MAX(Population)
from city
group by CountryCode
Having MAX(Population) > 8000000

# WITH ROLLUP
- 총합 또는 중간합계가 필요할 경우 사용
- GROUP BY절과 함께 WITH ROLLUP문 사용
- ★ ORDER BY 와는 함께 사용될 수 없습니다.
ex)
select CountryCode, Name,sum(Population)
from city
group by CountryCode, Name WITH rollup

# JOIN
- 데이터베이스 내의 여러 테이블에서 가져온 레코드를 조합하여 하나의 테이블이나 결과 집합으로 표현
- 기본: "inner"
ex)city테이블 기준으로 inner, city.CountryCode = country.Code가 같은 것을 기준으로 조인
select *
from city
join country ON city.CountryCode = country.Code;
ex)3개 합치기
select * 
from city
join country on city.CountryCode = country.Code
join countrylanguage on city.CountryCode = countrylanguage.CountryCode;
ex)
SELECT C.CategoryID, C.CategoryName, P.ProductName
FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID; 
  
# UNION
- 중복을 제거한 집합
ex) 두 테이블을 합치는 데, 4개 컬럼으로 만들어서 열방향으로 합침
SELECT CustomerName AS Name, City, Country, 'CUSTOMER'
FROM Customers
UNION
SELECT SupplierName AS Name, City, Country, 'SUPPLIER'
FROM Suppliers
ORDER BY Name;
ex) 합집합: 중복제거
SELECT CategoryID AS ID FROM Categories
WHERE CategoryID > 4
UNION (이 자리에 ALL 을 넣어주면 중복포함)
SELECT EmployeeID AS ID FROM Employees
WHERE EmployeeID % 2 = 0;

-- UNION ALL로 바꿔볼 것
# UNION ALL
- 중복을 제거하지 않은 집합
```

### 서브쿼리

```mysql
- 쿼리문 안에 또 쿼리문이 들어 있는 것

# 비상관 서브쿼리
- 메인 쿼리와 내부 쿼리들이 독자적으로 실행하는 것
- 서브 쿼리의 결과가 둘 이상이 되면 에러 발생
ex) Name 컬럼에 'seoul'인건 알겠는 데,
	그게 CountryCode가 뭐지 했을 때
select *
FROM city
where CountryCode = (	
    select CountryCode
	From city
    where name = 'seoul');
ex)
SELECT
  CategoryID, CategoryName, Description
FROM Categories
WHERE
  CategoryID =
  (SELECT CategoryID FROM Products
  WHERE ProductName = 'Chais');
ex)
SELECT
  CategoryID, CategoryName, Description
FROM Categories
WHERE
  CategoryID IN
  (SELECT CategoryID FROM Products
  WHERE Price > 50);

# ANY
- 서브쿼리의 여러 개의 결과 중 '한 가지만' 만족해도 가능
- ~ ANY	서브쿼리의 하나 이상의 결과에 대해 ~하다
- SOME은 ANY와 동일한 의미로 사용
- =ANY 구문은 IN과 동일한 의미
ex) any 안에 있는 어떠한 값보다 작을 경우
select *
FROM city
where Population < any (	select Population
							From city
							where District = 'New York'	);
							
# ALL
- 서브쿼리의 여러 개의 결과를 '모두' 만족 해야함
- ~ ALL	서브쿼리의 모든 결과에 대해 ~하다
ex) ALL 안에서 가장 높은 값보다 위인 경우
select *
FROM city
where Population > ALL (	select Population
							From city
							where District = 'New York'	);	
							
# 상관 서브쿼리
- 메인쿼리와 내부쿼리가 맞물려져서 돌아감
ex)
SELECT
  ProductID, ProductName,
  (
    SELECT CategoryName FROM Categories C(원하는이름)
    WHERE C.CategoryID = P.CategoryID
  ) AS CategoryName
FROM Products P(원하는이름);

# EXIST / NOT EXISTS 연산자
- 존재하는 값 추출
ex)
SELECT
  CategoryID, CategoryName
   ,(SELECT MAX(P.Price) FROM Products P
   WHERE P.CategoryID = C.CategoryID
  ) AS MaxPrice
FROM Categories C
WHERE EXISTS (
  SELECT * FROM Products P
  WHERE P.CategoryID = C.CategoryID
  AND P.Price > 80
);
```

## MySQL 내장 함수

### 문자열

```mysql
# length(): 전달받은 문자열의 바이트 길이를 반환, CHAR_LENGTH():문자열의 문자 길이
ex)
SELECT
  LENGTH('안녕하세요'), -- 15
  CHAR_LENGTH('안녕하세요'), -- 5
  CHARACTER_LENGTH('안녕하세요'); -- 5

# concat()
- 전달받은 문자열을 모두 결합하여 하나의 문자열로 반환
- 전달받은 문자열 중 하나라도 null이 존재하면 null 반환
ex)
CONCAT('HELLO', ' ', 'THIS IS ', 2021)
-- HELLO THIS IS 2021
ex)
SELECT CONCAT('원하는문자열 ', 컬럼명) FROM 테이블명;
-- 원하는문자열 컬럼내용

CONCAT_WS(S, ...): 괄호 안의 내용 S로 이어붙임
ex)
CONCAT_WS('-', 2021, 8, 15, 'AM')
-- 2021-8-15-AM
ex)
SELECT
  CONCAT_WS(' ', FirstName, LastName) AS FullName
FROM Employees;
/* FullName
Nancy Davolio
Andrew Fuller
Janet Leverling
*/

# locate()
- 문자열 내에서 찾는 문자열이 처음으로 나타나는 위치를 찾아서 해당 위치를 반환
- 찾는 문자열이 문자열 내에 존재하지 않으면 0 반환
- MySQL에서는 문자열의 시작 인덱스를 1부터 계산
ex) abc가 어느 위치에 있는 지
select locate('abc', 'asdfsdabc');

# left(), right(), SUBSTR()
- 문자열의 왼쪽 또는 오른쪽부터 지정한 개수만큼의 문자를 반환
ex)
select left(컬럼명, 5),
right(컬럼명, 5);
ex)
SELECT
  SUBSTR('ABCDEFG', 3),
  SUBSTR('ABCDEFG', 3, 2),
  SUBSTR('ABCDEFG', -4),
  SUBSTR('ABCDEFG', -4, 2);
-- CDEFG, CD, DEFG, DE
ex)
SELECT
  OrderDate,
  LEFT(OrderDate, 4) AS Year,
  SUBSTR(OrderDate, 6, 2) AS Month,
  RIGHT(OrderDate, 2) AS Day
FROM Orders;
/*
OrderDate	Year	Month	Day
1996-07-04	1996	07	    04
1996-07-05	1996	07	    05
*/


# LOWER(), UPPER()
- 문자열의 문자를 모두 소문자 또는 대문자로 변경
ex)
select lower('Left On Route'),
upper('Left On Route');

# replace()
- 문자열에서 특정 문자열을 대체 문자열로 교체
ex)Description 컬럼에서 ', '를 ' and '로 변경
SELECT
  REPLACE(Description, ', ', ' and ')
FROM Categories;
/*
REPLACE(Description, ', ', ' and ')
Soft drinks and coffees and teas and beers and ales
*/

# trim(), 
- 문자열의 앞이나 뒤, 또는 양쪽 모두에 있는 특정 문자를 제거
- trim() 함수에서 사용할 수 있는 지정자
 - both: 전달받은 문자열의 양 끝에 존재하는 특정문자를 제거(디폴트)
 - leading: 전달받은 문자열 앞에 존재하는 특정문자를 제거
 - trailing: 전달받은 문자열 뒤에 존재하는 특정문자를 제거
-제거할 문자를 명시하지 않으면, 공백을 제거
ex)
select trim('             MySQL           '),
trim(leading '#' from '###MySQL###'),
trim(trailing '#' from '###MySQL###');
# LTRIM(): 왼쪽 공백 제거, RTRIM(): 오른쪽 공백 제거
ex)
SELECT
  CONCAT('|', ' HELLO ', '|'), -- | HELLO |
  CONCAT('|', LTRIM(' HELLO '), '|'), -- |HELLO |
  CONCAT('|', RTRIM(' HELLO '), '|'), -- | HELLO|
  CONCAT('|', TRIM(' HELLO '), '|'); -- |HELLO|
  
#LPAD(S, N, P): S가 N글자가 될 때까지 P를 이어붙임 
#RPAD(S, N, P): S가 N글자가 될 때까지 P를 이어붙임
ex)
SELECT
  LPAD(SupplierID, 5, 0),
  RPAD(Price, 6, 0)
FROM Products;
/*
LPAD(SupplierID, 5, 0)	RPAD(Price, 6, 0)
00001					18.000
00001					19.000
*/

# INSTR(S, s): S중 s의 첫 위치 반환, 없을 시 0
ex)
SELECT
  INSTR('ABCDE', 'ABC'), -- 1
  INSTR('ABCDE', 'BCDE'), -- 2
  INSTR('ABCDE', 'C'), -- 3
  INSTR('ABCDE', 'DE'), -- 4
  INSTR('ABCDE', 'F'); -- 0
  
# CAST(A, T): A를 T 자료형으로 변환(dtype변경)
ex)
SELECT
  '01' = '1',
  CONVERT('01', DECIMAL) = CONVERT('1', DECIMAL);
/*
'01' = '1'	CONVERT('01', DECIMAL) = CONVERT('1', DECIMAL)
     0	                           1
*/

# 더 많은 문자열 함수
https://dev.mysql.com/doc/refman/8.0/en/string-functions.html
```

### 수학

```mysql
# format()
- 숫자 타입의 데이터를 세 자리마다 쉼표(,)를 사용하는 '#, ###, ###.##' 형식으로 변환
- 반환되는 데이터의 형식은 문자열 타입
- 두 번째 인수는 반올림할 소수 부분의 자릿수
ex)
select format(123123123123123.123123, 6);

# floor(), ceil(), round()
- 내림, 올림, 반올림
ex) select floor(10.95), ceil(10.95), round(10.95);

# sqrt(), pow(), exp(), log()
- sqrt(): 양의 제곱근
- pow(): 첫 번째 인수로는 밑수를 전달하고, 두 번째 인수로는 지수를 전달하여 거듭제곱 계산
- exp(): 인수로 지수를 전달받아, e의 거듭제곱을 계산
- log(): 자연로그 값을 계산
ex) select sqrt(4), pow(2, 3), exp(3), log(3);

# sin(), cos(), tan()
- 사인값, 코사인값, 탄젠트값 반환
ex) select sin(pi()/2), cos(pi()), tan(pi()/4);

# abs(), rand()
- abs(): 절대값 반환
- rand(): 0.0 <= x < 1인 실수 x를 랜덤으로 반환
ex) select abs(-3), rand(), round(rand()*100, 0);

# GREATEST, LEAST
- (괄호 안에서)가장 큰 값, (괄호 안에서)가장 작은 값 반환
ex)
SELECT 
  GREATEST(1, 2, 3), -- 3 반환
  LEAST(1, 2, 3, 4, 5); -- 1 반환
ex) 컬럼들 중에서 가장 큰 값, 가장 작은 값 반환
SELECT
  컬럼1, 컬럼2, 컬럼3, -- 비교 해보기 위해 삽입
  GREATEST(컬럼1, 컬럼2, 컬럼3),
  LEAST(컬럼1, 컬럼2, 컬럼3)
FROM 테이블명;

# 그룹 함수 - 조건에 따라 집계된 값을 가져옴
MAX	가장 큰 값
MIN	가장 작은 값
COUNT 개수(NULL값 제외)
SUM	총합
AVG	평균 값
ex)
SELECT
  MAX(컬럼명),
  MIN(컬럼명),
  COUNT(컬럼명),
  SUM(컬럼명),
  AVG(컬럼명)
FROM 테이블명
WHERE 컬럼명 BETWEEN 20 AND 30; -- 이 부분은 없어도 됨: 이 구간 내에서 구해달라할 때 사용

POW(A, B), POWER(A, B)	A를 B만큼 제곱
SQRT 제곱근
ex)
SELECT
  POW(2, 3),
  POWER(5, 2),
  SQRT(16);
  
TRUNCATE(N, n)	N을 소숫점 n자리까지 선택
- n에 음수를 넣으면 그 수 만큼 0을 넣음
ex)
SELECT 컬럼명 FROM 테이블명
WHERE TRUNCATE(컬럼명, 0) = 12;

# 더 많은 숫자 함수
https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html
```

### 날짜

```mysql
# now(), curdate(), curtime()
- now(): 현재 날짜 + 시간
- curdate(): 현재 날짜
- curtime(): 현재 시간
ex) select now(), curdate(), curtime();

# date(), time(), year(), month(), day(), hour(), minute(), second()
# monthname(), weekday(), dayname()
DATE: 문자열에 따라 날짜 생성
TIME: 문자열에 따라 시간 생성
ex)
SELECT
  '2021-6-1' = '2021-06-01', -- 0
  DATE('2021.6.1') = DATE('2021-06-01'), -- 1
  '1:2:3' = '01:02:03', -- 0
  TIME('1:2:3') = TIME('01:02:03'); -- 1
ex)
SELECT * FROM Orders
WHERE
  OrderDate BETWEEN DATE('1997-1-1') AND DATE('1997-1-31');

YEAR: 주어진 DATETIME값의 년도 반환
MONTHNAME: 주어진 DATETIME값의 월(영문) 반환
MONTH: 주어진 DATETIME값의 월 반환
WEEKDAY: 주어진 DATETIME값의 요일값 반환(월요일: 0)
DAYNAME: 주어진 DATETIME값의 요일명 반환
DAY: 주어진 DATETIME값의 날짜(일) 반환
ex)
SELECT
  OrderDate,
  YEAR(OrderDate) AS YEAR,
  MONTHNAME(OrderDate) AS MONTHNAME,
  MONTH(OrderDate) AS MONTH,
  WEEKDAY(OrderDate) AS WEEKDAY,
  DAYNAME(OrderDate) AS DAYNAME,
  DAY(OrderDate) AS DAY
FROM Orders;
/*
OrderDate	YEAR	MONTHNAME	MONTH	WEEKDAY	 DAYNAME	DAY
1996-07-04	1996	July	    7	    3	    Thursday    4
*/
ex) 조건문으로도 사용가능
SELECT * FROM Orders
WHERE WEEKDAY(OrderDate) = 0; -- 월요일만 뽑기

HOUR	주어진 DATETIME의 시 반환
MINUTE	주어진 DATETIME의 분 반환
SECOND	주어진 DATETIME의 초 반환
ex) 현재 시간, 분, 초 반환
SELECT
  HOUR(NOW()), MINUTE(NOW()), SECOND(NOW());

# dayofweek(), dayofmonth(), dayofyear()
- 1~7(일~토요일),    0~31    , 1~366 반환
ex)
select
dayofweek(now()),
dayofmonth(now()),
dayofyear(now());

# ADDDATE, SUBDATE
ADDDATE, DATE_ADD: 시간/날짜 더하기
SUBDATE, DATE_SUB: 시간/날짜 빼기
ex)
SELECT 
  ADDDATE('2021-06-20', INTERVAL 1 YEAR), -- 2022-06-20 1년 후
  ADDDATE('2021-06-20', INTERVAL -2 MONTH), -- 2021-04-20 2달 전
  ADDDATE('2021-06-20', INTERVAL 3 WEEK), -- 2021-07-11	3주 후
  ADDDATE('2021-06-20', INTERVAL -4 DAY), -- 2021-06-16	4일 전
  ADDDATE('2021-06-20', INTERVAL -5 MINUTE), -- 2021-06-19 5분 전
  ADDDATE('2021-06-20 13:01:12', INTERVAL 6 SECOND); -- 23:55:00 2021-06-20 13:01:18
  
# DATE_DIFF, TIME_DIFF
DATE_DIFF: 두 시간/날짜 간 일수차
TIME_DIFF: 두 시간/날짜 간 시간차
ex)
SELECT
  OrderDate,
  NOW(),
  DATEDIFF(OrderDate, NOW()) -- 위치바꾸면 양수로 출력 or ABS() 넣으면 양수로 출력
FROM Orders;
/*
OrderDate	NOW()	            DATEDIFF(OrderDate, NOW())
1996-07-04	2022-06-26 01:48:47	-9488 -- 9488일 차이 난다 /
*/

# LAST_DAY:	해당 달의 마지막 날짜
ex)
SELECT
  OrderDate, -- 1996-07-04
  LAST_DAY(OrderDate), -- 1996-07-31
  DAY(LAST_DAY(OrderDate)), -- 31
  DATEDIFF(LAST_DAY(OrderDate), OrderDate) -- 27
FROM Orders;

#★ date_format()
- 전달받은 형식에 맞춰 날짜와 시간 정보를 문자열로 반환
형식	설명
%Y	 년도 4자리
%y   년도 2자리
%M	월 영문
%m	월 숫자
%D	일 영문(1st, 2nd, 3rd...)
%d, %e	일 숫자 (01 ~ 31)
%T	hh:mm:ss
%r	hh:mm:ss AM/PM
%H, %k	시 (~23)
%h, %l	시 (~12)
%i	분
%S, %s	초
%p	AM/PM
ex)
SELECT
  DATE_FORMAT(NOW(), '%M %D, %Y %T'), -- June 26th, 2022 02:01:05	
  DATE_FORMAT(NOW(), '%y-%m-%d %h:%i:%s %p'), -- 22-06-26 02:01:05 AM	
  DATE_FORMAT(NOW(), '%Y년 %m월 %d일 %p %h시 %i분 %s초'); -- 2022년 06월 26일 AM 02시 01분 05초
ex) 응용
SELECT REPLACE(
  REPLACE(
    DATE_FORMAT(NOW(), '%Y년 %m월 %d일 %p %h시 %i분 %초'),
    'AM', '오전'
  ),
  'PM', '오후'
)
-- 2022년 06월 26일 오전 02시 03분 초

# TR _ TO _ DATE(S, F): S를 F형식으로 해석하여 시간/날짜 생성
ex)
SELECT
  STR_TO_DATE('1997-01-01 13:24:35', '%Y-%m-%d %T')
-- 1997-01-01 13:24:35

# 더 많은 날짜 함수
https://dev.mysql.com/doc/refman/8.0/en/string-functions.html
```

### 기타 함수

```mysql
# IF, CASE
IF(조건, T, F): 조건이 참이라면 T, 거짓이면 F 반환
CASE: 좀 더 복잡한 조건문
ex)
SELECT
  Price, -- 18.00
  IF (Price > 30, 'Expensive', 'Cheap'),  -- Cheap
  CASE
    WHEN Price < 20 THEN '저가'
    WHEN Price BETWEEN 20 AND 30 THEN '일반'
    ELSE '고가'
  END -- 저가
FROM Products;

#
ex)IFNULL(A, B): A가 NULL일 시 B 출력, 아니면 A 출력
SELECT
  IFNULL('A', 'B'), -- A
  IFNULL(NULL, 'B'); -- B
```

## SQL 고급

```mysql
# create database
- 새로운 데이터베이스를 생성
ex) create database 원하는이름

# create table 원하는테이블이름 as select * from 복사할테이블
- 똑같은 테이블 복사해서 만들기
ex)
create table city2 as select * from city;
- 만들어진 것 확인은 새로고침 해주면 됨
- 직접 만드는 방법
ex)
create table test2 (
	id int not null primary key,
	col1 int null,
	col2 float null,
	col3 varchar(45) null
    );
    
# alter table 테이블이름
- 테이블 수정
ex) col4 컬럼 더하기
alter table test2
add col4 int null;
ex) col4 컬럼 타입 수정
alter table test2
modify col4 varchar(20) null;
ex) col4 컬럼 삭제
alter table test2
drop col4;
```

### 인덱스

```mysql
# 인덱스
- 테이블에서 원하는 데이터를 빠르게 찾기 위해 사용
- 수정보다는 검색이 자주 사용되는 테이블에서 사용하는 것이 좋음

# create index
- index 만들기
ex)
create index col1dx
on test2 (col1);

# show index from 테이블

# create unique index
- 중복 값을 허용하지 않는 인덱스
ex)
create unique index col2dx
on test2 (col2);

# fulltext index
- 일반적인 인덱스와는 달리 매우 빠르게 테이블의 모든 텍스트 컬럼을 검색
ex)
alter table test2
add fulltext col3idx(col3);

# 인덱스 삭제
ex) 그냥 삭제
drop index 인덱스명 on 테이블명
ex) alter table 이용
alter table test2
drop index 인덱스명;
```

### VIEW

```mysql
# 뷰
- 데이터베이스에 존재하는 가상테이블
- 저장되지않고 보여주는 역할만 수행
확인
- select * from 뷰이름

# create view
- 뷰 생성
ex)
create view 만들뷰이름 as
select 컬럼1, 컬럼2
from 테이블;

# alter view
- 뷰 수정
ex)
alter view testview as
select col1, col2, col3
from test2;

# drop view
- 뷰 삭제
ex) drop view testview
```

### 수정, 삭제 등

```mysql
# insert
- 값 넣기
- 테이블 이름 다음에 나오는 열 생략 가능
- 생략할 경우에 value 다음에 나오는 값들의 순서 및 개수가 테이블이 컬럼 수와 같아야함
ex)
insert into 테이블명(컬럼이름1, 컬럼이름2, ..., 컬럼이름n)
value(값1, 값2, 값3, 값4);
- workbench에서는 직접 표에 값넣고 apply 버튼 눌러줘도 됨

# insert into select
- test 테이블에 있는 내용을 test2 테이블에 삽입
ex)
insert into test2 select * from test;

# update
- 기존에 입력되어 있는 값을 변경
- 중요!! where절 생략 가능하나 테이블의 전체 행의 내용 변경
ex) 컬럼 값 기준으로
update test2
set col1=1, col2=9999, col3='test2'
where 컬럼 = 값;

# delete
- 행 단위로 데이터 삭제
- 중요!! where을 써야 전체가 삭제안됨
- 휴지통 개념으로 살리기 가능하므로 용량이 줄어들지 않음
ex)
delete from test2
where id = 1;

# truncate
- 용량이 줄어들고 모두 삭제
- 되돌릴 수 없음
ex)
truncate table test2;

# drop table
- 테이블 전체를 삭제, 공간, 객체를 삭제
- 되돌리기 불가능

# drop database
- 데이터베이스 삭제
```




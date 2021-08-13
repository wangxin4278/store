CREATE DATABASE it CHARACTER SET utf8;
CREATE TABLE person(
	username VARCHAR(20),
	age INT,
	sex VARCHAR(10),
	salary DOUBLE(10,2),
	id VARCHAR(10)
)
INSERT INTO person VALUES("jason",56,"男",5000.36,1)
DELETE FROM person username>=6

DELETE FROM person WHERE age>=60 AND age<=10


UPDATE person SET age = age +10
DELETE FROM person WHERE username="孙策"

UPDATE person SET username="曹操" WHERE age>=60 
UPDATE person SET username="刘备" WHERE age=age<=55
UPDATE person SET username="关羽" WHERE age= age<=46 
UPDATE person SET username="张飞" WHERE age<=43 
UPDATE person SET username="孙策" WHERE age<=55 AND age>=46
SELECT * FROM person WHERE age>40
SELECT * FROM person WHERE username LIKE "%孙%"
SELECT * FROM person WHERE username username LIKE "__"
SELECT * FROM t_employees WHERE comm=0 OR comm IS NULL
SELECT ename,dname 
FROM t_employees,t_dept 
WHERE  t_employees.`deptno` =  t_dept.`deptno`

SELECT ename ,dname 
FROM t_employees JOIN t_dept ON t_employees.`deptno` = t_dept.`deptno`

SELECT ename,dname FROM t_employees,t_dept WHERE t_employees.`deptno`=t_dept.`deptno`

SELECT ename ,dname FROM t_employees JOIN t_dept ON t_employees.`deptno` = t_dept.`deptno`

SELECT t1.ename,t2.ename
FROM t_employees  t1  , t_employees t2
WHERE t1.MGR  = t2.empno

SELECT t1.ename,t2.ename
FROM t_employees t1  JOIN t_employees t2
ON t1.MGR = t2.empno
SELECT COUNT(ename) FROM t_employees;
SELECT SUM(sal) FROM t_employees;
SELECT AVG(sal) FROM t_employees;
SELECT * FROM t_employees ORDER BY  sal DESC LIMIT 4;

--company数据库

CREATE TABLE dept(
	deptno INT,
	dname VARCHAR(50),
	loc VARCHAR(50)
)
CREATE TABLE employees(
	empno INT,
	ename VARCHAR(50),
	job VARCHAR(50),
	MGR VARCHAR(50),
	hiredate DATETIME,
	sal DOUBLE(10,2),
	comm DOUBLE(10,2),
	deptno VARCHAR(10)
)
--单表查询
--查询出部门编号为30的所有员工
SELECT * FROM employees WHERE deptno = 30;
--所有销售员的姓名、编号和部门编号。
SELECT ename,empno,deptno FROM employees;
--找出奖金高于工资的员工
SELECT ename FROM employees WHERE comm > sal;
--找出奖金高于工资60%的员工
SELECT ename FROM employees WHERE comm > sal * 0.6;
--找出部门编号为10中所有经理，和部门编号为20中所有销售员的详细资料
SELECT * FROM employees WHERE job="经理" AND deptno=10 OR job="销售员" AND deptno=20;
--找出部门编号为10中所有经理，部门编号为20中所有销售员，
--还有即不是经理又不是销售员但其工资大或等于20000的所有员工详细资料
SELECT * FROM employees WHERE deptno = 10 AND job = '经理' OR 
deptno = 20 AND job ='销售员' OR job !='经理' AND job != '销售员' AND sal >=20000;
--无奖金或奖金低于1000的员工
SELECT * FROM employees WHERE comm<1000 OR comm IS NULL;
--查询名字由三个字组成的员工
SELECT ename FROM employees WHERE ename LIKE"___";
--查询2000年入职的员工
SELECT * FROM employees WHERE hiredate LIKE "%200%"
--查询所有员工详细信息，用编号升序排序
SELECT * FROM employees ORDER BY deptno;
--查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT * FROM employees ORDER BY sal DESC ,hiredate ASC;
--查询每个部门的平均工资
SELECT AVG(sal)FROM employees; 
--查询每个部门的雇员数量。
SELECT COUNT(ename) FROM employees;
--查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal),MIN(sal),COUNT(*) FROM t_employees;

--多表查询
--查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数
SELECT d.deptno,d.dname,d.loc,COUNT(*) FROM dept d,employees e
WHERE e.deptno=d.deptno;

--列出所有员工的姓名及其直接上级的姓名
SELECT t1.ename,t2.ename FROM employees t1,employees t2 WHERE t1.MGR=t2.empno;
--列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称
SELECT e.empno,e.ename,e.deptno FROM employees e,employees m
WHERE e.MGR=m.empno AND e.hiredate<m.hiredate;

--列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门
SELECT * FROM employees e RIGHT OUTER JOIN dept d ON e.deptno=d.deptno

--列出最低薪金大于15000的各种工作及从事此工作的员工人数。
SELECT job,COUNT(*) FROM employees e GROUP BY job HAVING MIN(sal)>15000
--列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
SELECT *
FROM employees e
WHERE e.deptno=(SELECT deptno FROM dept WHERE dname='acountint')
--列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。


--列出与clack从事相同工作的所有员工及部门名称
SELECT e.*,d.dname FROM employees e, dept d WHERE e.deptno=d.deptno AND job=(SELECT job FROM employees WHERE ename="荀彧")
--列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称
SELECT e.ename, e.sal, d.dname
FROM employees e, dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM employees WHERE deptno=30)
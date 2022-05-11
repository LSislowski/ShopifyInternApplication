# SpotifyInternApplication
This Repo Includes the Fall 2022 Spotify Data Science Intern Challenge

Fall 2022 Data Science Intern Challenge 

Please complete the following questions, and provide your thought process/work. You can attach your work in a text file, link, etc. on the application page. Please ensure answers are easily visible for reviewers!

<br>
<br>
<b>
Question 1: Given some sample data, write a program to answer the following: <a href= "https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/edit#gid=0">click here</a> to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
What metric would you report for this dataset?
What is its value?</b>
<br>
<br>

~~~
When we are looking at the calculation for the Mean of sales amounts, this is an inaccurate value to use since the distribution of the sales amounts are right skewed.  Looking through the exploratory Jupyter Notebook, we can see that the largest buyer of shoes spent over $11mm over the 30 day window.  This drastically affected the Average Order Value.  The Median Order Value (MOV) in this instance is $284 which seems to be a more accurate value to describe what types of purchases are generally being made for shoes in this dataset.
~~~

<br>
<br>
<b>Question 2: For this question you’ll need to use SQL. Follow <a href= "https://www.w3schools.com/SQL/TRYSQL.ASP?FILENAME=TRYSQL_SELECT_ALL">this link</a> to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

<br>
How many orders were shipped by Speedy Express in total?
</b>
<br>
<br>

~~~
54
~~~

~~~
SELECT COUNT(DISTINCT(ORDERID)) FROM SHIPPERS S
JOIN ORDERS O ON S.SHIPPERID = O.SHIPPERID
WHERE S.SHIPPERID IS 1;
~~~

<br>
<b>
What is the last name of the employee with the most orders?
</b>
<br>
<br>

~~~	
PEACOCK - 40 Orders
~~~

~~~
SELECT COUNT(DISTINCT(ORDERID)), LASTNAME FROM EMPLOYEES E
JOIN ORDERS O ON O.EMPLOYEEID = E.EMPLOYEEID
GROUP BY E.LASTNAME
ORDER BY COUNT(DISTINCT(O.ORDERID)) DESC;
~~~

<br>
<b>
What product was ordered the most by customers in Germany?
</b>
<br>
<br>

~~~
There was a total of 50 Boston Crab Meats Ordered
~~~

~~~
SELECT P.PRODUCTNAME, P.PRODUCTID, OD.QUANTITY, C.COUNTRY FROM CUSTOMERS C 
JOIN ORDERS O ON O.CUSTOMERID = C.CUSTOMERID 
JOIN ORDERDETAILS OD ON OD.ORDERID = O.ORDERID
JOIN PRODUCTS P ON P.PRODUCTID = OD.PRODUCTID
GROUP BY OD.PRODUCTID
HAVING C.COUNTRY LIKE 'Germany'
ORDER BY OD.QUANTITY DESC;
~~~









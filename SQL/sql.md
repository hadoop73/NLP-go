


[SQL 教程](http://www.runoob.com/sql/sql-tutorial.html)

##  Group BY

group by 主要用于对与表中的列进行按照元素不同取值进行聚类统计

**形式如下:**
```
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;
```


##  Order BY

对结果进行按一列或多列进行排序

**形式如下:**
```
SELECT column_name,column_name
FROM table_name
ORDER BY column_name,column_name ASC|DESC;
```

##  Join 

用于两张表进行连接

**形式如下:**
```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name=table2.column_name;
```

##  HAVING 
HAVING 用来连接聚合函数,相当于 where 的条件作用

![enter description here][1]

![enter description here][2]

**现在我们想要查找总访问量大于 200 的网站。**

```
SELECT Websites.name, Websites.url, SUM(access_log.count) AS nums FROM (access_log
INNER JOIN Websites
ON access_log.site_id=Websites.id)
GROUP BY Websites.name
HAVING SUM(access_log.count) > 200;
```


##  SQL 实例

[数据库面试常问的一些基本概念](http://blog.csdn.net/u013142781/article/details/50844643)

[SQL实例整理](http://blog.csdn.net/u013142781/article/details/50836476)



  [1]: ./images/1491203141881.jpg "1491203141881.jpg"
  [2]: ./images/1491203159103.jpg "1491203159103.jpg"

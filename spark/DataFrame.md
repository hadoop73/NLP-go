

#  DataFrame 操作

##  DataFrame 初始化

```python
os.environ["SPARK_HOME"] = "/home/hadoop/spark-2.0.1-bin-hadoop2.7"   #KeyError: 'SPARK_HOME'
conf = SparkConf()
conf.set("spark.hadoop.validateOutputSpecs", "false")
conf.setMaster('spark://master:7077')
sc=SparkContext(appName='p1-sample',conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.format('com.databricks.spark.csv')\
    .options(header='true', charset="utf-8")\
    .load('hdfs://192.168.1.116:9000/home/hadoop/data2/JData34.csv') 
```

写入文件
```
# 保存到 hdfs
data.write.csv("/home/hadoop/data2/{}.csv".format(path),header=True,mode="overwrite")
# 保存到本地文件系统
data.toPandas().to_csv("../data2/{}.csv".format(TESTSku),index=None)
```


**返回列名**
```python
>>> df.columns
['age', 'name']
```

**返回行数**
```python
>>> df.count()
2
```

**DataFrame 统计信息**
describe(*cols)

```python
>>> df.describe().show()
+-------+------------------+
|summary|               age|
+-------+------------------+
|  count|                 2|
|   mean|               3.5|
| stddev|2.1213203435596424|
|    min|                 2|
|    max|                 5|
+-------+------------------+
>>> df.describe(['age', 'name']).show()
+-------+------------------+-----+
|summary|               age| name|
+-------+------------------+-----+
|  count|                 2|    2|
|   mean|               3.5| null|
| stddev|2.1213203435596424| null|
|    min|                 2|Alice|
|    max|                 5|  Bob|
+-------+------------------+-----+
```

**去重**
```python
df.distinct() # 返回没有重复行的 dataframe
df.dropDuplicates(['name','age']) # 删除特定列相同的行
```

**删除列**
```python
df.drop(col)
```

**处理空值**

- dropna(how='any', thresh=None, subset=None)
Returns a new DataFrame omitting rows with null values. DataFrame.dropna() and DataFrameNaFunctions.drop() are aliases of each other.

**Parameters:**	
    
     how – ‘any’ or ‘all’. If ‘any’, drop a row if it contains any nulls. If ‘all’, drop a row only if all its values are null.
     thresh – int, default None If specified, drop rows that have less than thresh non-null values. This overwrites the how parameter.
     subset – optional list of column names to consider.


- fillna(value, subset=None)
Replace null values, alias for na.fill(). DataFrame.fillna() and DataFrameNaFunctions.fill() are aliases of each other.

Parameters:	

     value – int, long, float, string, or dict. Value to replace null values with. If the value is a dict, then subset is ignored and value must be a mapping from column name (string) to replacement value. The replacement value must be an int, long, float, or string.
     subset – optional list of column names to consider. Columns specified in subset that do not have matching data type are ignored. For example, if value is a string, and subset contains a non-string column, then the non-string column is simply ignored.

```python
>>> df4.na.fill({'age': 50, 'name': 'unknown'}).show()
+---+------+-------+
|age|height|   name|
+---+------+-------+
| 10|    80|  Alice|
|  5|  null|    Bob|
| 50|  null|    Tom|
| 50|  null|unknown|
+---+------+-------+
```


**条件筛选子集**
行筛选
- filter(condition)
    Filters rows using the given condition.

    where() is an alias for filter().

列筛选
select(*cols)
```
>>> df.select('*').collect()
[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')]
>>> df.select('name', 'age').collect()
[Row(name=u'Alice', age=2), Row(name=u'Bob', age=5)]
>>> df.select(df.name, (df.age + 10).alias('age')).collect()
[Row(name=u'Alice', age=12), Row(name=u'Bob', age=15)]
```

**聚集**

groupby(*cols)

```python
>>> df.groupBy().avg().collect()
[Row(avg(age)=3.5)]
>>> df.groupBy('name').agg({'age': 'mean'}).collect()
[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]
>>> df.groupBy(df.name).avg().collect()
[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)]
>>> df.groupBy(['name', df.age]).count().collect()
[Row(name=u'Bob', age=5, count=1), Row(name=u'Alice', age=2, count=1)]
```

head(n=None) 返回前 n 行数据

```python
>>> df.head()
Row(age=2, name=u'Alice')
>>> df.head(1)
[Row(age=2, name=u'Alice')]
```

**合并 DataFrame**

join(other, on=None, how=None)

Parameters:	
    other – Right side of the join
    on – a string for join column name, a list of column names, , a join expression (Column) or a list of Columns. If on is a string or a list of string indicating the name of the join column(s), the column(s) must exist on both sides, and this performs an equi-join.
    how – str, default ‘inner’. One of inner, outer, left_outer, right_outer, leftsemi.


**替换**

replace(to_replace, value, subset=None)

```python
>>> df4.na.replace(['Alice', 'Bob'], ['A', 'B'], 'name').show()
+----+------+----+
| age|height|name|
+----+------+----+
|  10|    80|   A|
|   5|  null|   B|
|null|  null| Tom|
|null|  null|null|
+----+------+----+
```

**抽样**

sample(withReplacement, fraction, seed=None)
```
>>> df.sample(False, 0.5, 42).count()
2
```

**排序**
sort(*cols, **kwargs)

Parameters:	
    cols – list of Column or column names to sort by.
    ascending – boolean or list of boolean (default True). Sort ascending vs. descending. Specify list for multiple sort orders. If a list is specified, length of the list must equal length of the cols.
```
>>> df.sort(df.age.desc()).collect()
[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')]
>>> df.sort("age", ascending=False).collect()
[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')]
>>> df.orderBy(df.age.desc()).collect()
[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')]
>>> from pyspark.sql.functions import *
>>> df.sort(asc("age")).collect()
[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')]
>>> df.orderBy(desc("age"), "name").collect()
[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')]
>>> df.orderBy(["age", "name"], ascending=[0, 1]).collect()
[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')]
```

**更换列名**

toDF(*cols)

Parameters:	cols – list of new column names (string)
```
>>> df.toDF('f1', 'f2').collect()
[Row(f1=2, f2=u'Alice'), Row(f1=5, f2=u'Bob')]
```

withColumnRenamed(existing, new)
    Returns a new DataFrame by renaming an existing column.

Parameters:	
    existing – string, name of the existing column to rename.
    col – string, new name of the column.
```
>>> df.withColumnRenamed('age', 'age2').collect()
[Row(age2=2, name=u'Alice'), Row(age2=5, name=u'Bob')]
```

toPandas()
Returns the contents of this DataFrame as Pandas pandas.DataFrame.
```
>>> df.toPandas()  
   age   name
0    2  Alice
1    5    Bob
```

withColumn(colName, col)
    Returns a new DataFrame by adding a column or replacing the existing column that has the same name.

Parameters:	
    colName – string, name of the new column.
    col – a Column expression for the new column.
```
>>> df.withColumn('age2', df.age + 2).collect()
[Row(age=2, name=u'Alice', age2=4), Row(age=5, name=u'Bob', age2=7)]
```

##  pivot

pivot(pivot_col, values=None)
Pivots a column of the current DataFrame and perform the specified aggregation. There are two versions of pivot function: one that requires the caller to specify the list of distinct values to pivot on, and one that does not. The latter is more concise but less efficient, because Spark needs to first compute the list of distinct values internally.
Parameters:	
    pivot_col – Name of the column to pivot.
    values – List of values that will be translated to columns in the output DataFrame.
```
>>> df4.groupBy(“year”).pivot(“course”, [“dotNET”, “Java”]).sum(“earnings”).collect() 
[Row(year=2012, dotNET=15000, Java=20000), Row(year=2013, dotNET=48000, Java=30000)]

// Or without specifying column values (less efficient) 
>>> df4.groupBy(“year”).pivot(“course”).sum(“earnings”).collect() 
[Row(year=2012, Java=20000, dotNET=15000), Row(year=2013, Java=30000, dotNET=48000)]
```


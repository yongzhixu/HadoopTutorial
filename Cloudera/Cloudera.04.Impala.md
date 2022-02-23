[TOC]



## Hive Metastore (HMS)

[Introduction to Hive metastore](https://docs.cloudera.com/runtime/7.2.7/hive-hms-overview/topics/hive-hms-introduction.html)

[Hive Metastore And Impala Metastore: An Important Guide In 2021](https://www.jigsawacademy.com/blogs/tutorial/hive-metastore/)



## Using Apache Kudu with Apache Impala

[Using Apache Kudu with Apache Impala](https://kudu.apache.org/docs/kudu_impala_integration.html)

> ### [Optimizing Performance for Evaluating SQL Predicates](https://kudu.apache.org/docs/kudu_impala_integration.html#_optimizing_performance_for_evaluating_sql_predicates)
>
> If the `WHERE` clause of your query includes comparisons with the operators `=`, `<=`, '\<', '\>', `>=`, `BETWEEN`, or `IN`, Kudu evaluates the condition directly and only returns the relevant results. This provides optimum performance, because Kudu only returns the relevant results to Impala. For predicates `!=`, `LIKE`, or any other predicate type supported by Impala, Kudu does not evaluate the predicates directly, but returns all results to Impala and relies on Impala to evaluate the remaining predicates and filter the results accordingly. This may cause differences in performance, depending on the delta of the result set before and after evaluating the `WHERE` clause.




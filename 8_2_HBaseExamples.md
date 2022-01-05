[TOC] 

## Access to Hbase via RestApi

- Start Hbase RestApi server

```sh
/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8010
```

- stop server

```sh
/usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest -p 8010
```



## Access via HBase Shell

```sh
enter shell >> hbase shell
create hbase table >> create 'users',　'userinfo'
-- userinfo represent column family
double check >> list

exit
import data using pig into hbase table 'users' >> pig hbase.pig

enter shell >> hbase shell
double check >> scan 'users'

clean table >> disbable 'users'
clean table >> drop 'users'
```



[tutorial point](https://www.tutorialspoint.com/hbase/hbase_scan.htm)


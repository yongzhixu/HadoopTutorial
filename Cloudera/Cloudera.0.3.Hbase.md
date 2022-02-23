[TOC]





# Bugs

## Permission denied

### Explained

> Permission denied: user=hbase, access=WRITE, inode="/hbase/MasterProcWALs":cloudera:hbase:drwxr-xr-x

### Solution

> Have you run "Create Root Directory" from HBase's available actions in Cloudera Manager?
>
> This will create the "/hbase" (default value) directory in hdfs that will belong to user hbase and group hbase.
>
> If it is created then check permissions
>
> sudo -u hdfs hdfs dfs -ls /
>
> 
>
> If not, create it (you can do it using Cloudera Manager as mentioned above):
>
> sudo -u hdfs hdfs dfs -mkdir /hbase
>
> sudo -u hdfs hdfs dfs -chown hbase:hbase /hbase
>
> sudo -u hdfs hdfs dfs -chown hbase:hbase /hbase/*



## Master failed to complete initialization

### Explained

> master.HMaster: Master failed to complete initialization after 900000ms. Please consider submitting a bug report including a thread dump of this process.
>
> HMaster: hbase:meta,,1.1588230740 is NOT online; 

### Solution

> 在zookeeper中删除/hbase即可
>
> ```sh
> # go to zookeeper server dir
> # find / -name "zkCli.sh"
> ./zkCli.sh
> # list dir
> ls /
> deleteall /hbase
> # exit zk client shell
> quit
> 
> 
> restart hbase cluster
> ```






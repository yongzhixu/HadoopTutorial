## Installing Cassandra

if python is not on python 2.7

- install it first

```
yum install scl-utils
yum install centos-release-scl-rh
yum install python27
scl enable python27
python --version
```

- install cassandra

```sh

cd /etc/yum.repos.d
vim datastax.repo

-- save the following content
[datastax]
name = Datastax Repo for Apache Cassandra
baseurl = http://rpm.datastax.com/community
enabled = 1
gpgcheck = 0

-- disconnect vpn if failed
yum install dsc30
pip install cqlsh
service cassandra start

cqlsh --cqlversion="installed version"

-- create a keyspace (like database for mysql)
CREATE KEYSPACE movielens WITH replication = {'class':'SimpleStrategy', 'replication_factor':'1'} AND durable_with = true;

USE movielens;

```


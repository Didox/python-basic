# install
# $ python -m pip install cassandra-driver

"""
CREATE TABLE cities (
 id int,
 name text,
 country text,
 PRIMARY KEY(id)
);

INSERT INTO cities(id,name,country) VALUES (1,'Karachi','Pakistan');
INSERT INTO cities(id,name,country) VALUES (2,'Lahore','Pakistan');
INSERT INTO cities(id,name,country) VALUES (3,'Dubai','UAE');
INSERT INTO cities(id,name,country) VALUES (4,'Berlin','Germany');


CREATE TABLE users (
 username text,
 name text,
 age int,
 PRIMARY KEY(username)
);

INSERT INTO users(username,name,age) VALUES ('aali24','Ali Amin',34);
INSERT INTO users(username,name,age) VALUES ('jack01','Jack David',23);
INSERT INTO users(username,name,age) VALUES ('ninopk','Nina Rehman',34);

CREATE TABLE users_by_cities (
 username text,
 name text,
 city text,
 age int,
 PRIMARY KEY(city,age)
);

INSERT INTO users_by_cities(username,name,city,age) VALUES ('aali24','Ali Amin','Karachi',34);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('jack01','Jack David','Berlin',23);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('ninopk','Nina Rehman','Lahore',34);

BEGIN BATCH
INSERT into users(username,name,age) VALUES('raziz12','Rashid Aziz',34);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('raziz12','Rashid Aziz','Karachi',30);
APPLY BATCH;

select token(username) from users;
select token(username),username,city from users_by_cities;
select * from users_by_cities where city = 'Karachi';

"""

from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'],port=9042)
session = cluster.connect('app_data_danilo', wait_for_all_pools=True)
session.execute("insert into users(name, username, age)values('Leandro','Santos',22)")
# session.execute('USE app_data_danilo')
rows = session.execute('SELECT * FROM users')
for row in rows:
    print(row.age,row.name,row.username)
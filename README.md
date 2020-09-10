# mysql2mongodb

Instructions

clone this repo

Install mysql client and mongodb client for shell access on the host machine

```
cd mysql2mongodb

docker-compose up -d

#Load the sample.sql into mysql

# password is your password. provide when prompted
mysql -h127.0.0.1 -uroot -p < sample.sql

```

On your browser goto localhost:5000

you should see a hello world

goto localhost:5000/migrate
You should see 4 rows got migrated to mongodb

you can verify by logging into mongodb by running the following

```
use itsyourskills
c = db.employees
c.find()
```

You should now see the inserted mysqldb entries appear on mongodb

You can also see the logs by issuing the following

`docker ps` and copy the container id
`docker logs <container_id>`
Now you should see all the flask logs

Finally shutdown all the dockers by issuing `docker-compose down`



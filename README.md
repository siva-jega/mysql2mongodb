# mysql2mongodb

### Instructions

### Pre-requests
1. MySQL Client (to upload the `sample.sql` file)
2. Mongodb Client to verify the inserted data through shell
3. docker
4. docker-compose

On ubuntu run the following to get the clients installed

```
sudo apt-get install mongodb-clients -y
sudo apt-get install mysql-client -y

```

To install `docker` and `docker-compose` find the relevant documents on google

clone this repo and run the below on the shell

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



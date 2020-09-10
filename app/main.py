from flask import Flask  # noqa
from MySQLdb import _mysql as mysqlclient
from pymongo import MongoClient

app = Flask(__name__)

mysqldb = mysqlclient.connect(
    host="mysql", port=3306, user="root", passwd="password", db="skills"
)

mongodb = MongoClient("mongo", 27017)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/migrate")
def migrate():
    try:
        mysqldb.query(
            """SELECT e.name, s.salary FROM employee e JOIN salary s ON e.id = s.employee_id"""
        )
    except Exception as err:
        return f"{err}"
    res = mysqldb.store_result()

    row = res.fetch_row(maxrows=0, how=1)
    db = mongodb.itsyourskills
    coll = db.employees

    count = 0
    for r in row:
        temp = {k: v.decode("ascii") for k, v in r.items()}
        print(f"Inserting row {temp}")
        id = coll.insert_one(temp).inserted_id
        print(f"done -> {id}")
        count += 1

    return f"Migration done for {count} rows"


if __name__ == "__main__":
    app.run()

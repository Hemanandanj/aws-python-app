from flask import Flask, render_template, request
import pymysql

app - Flask(__name__)

db_config = {
    'host': '172.31.19.240',
    'user': 'app_user',
    'password': 'HEma12#$',
    'database': 'app_db',


}

@app.route('/')
def index():
    return render_template("index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')

    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() ass cursor:
            sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
            curson.execute(sql, (name,age))
        connection.commit()
        connection.close()
        return f"<h1>Success!</h1><p>Registered {name}, age {age}.</p><a href='/'>Go Back</a>"
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)</p>}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
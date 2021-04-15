from flask import Flask, request, redirect
from flask import render_template
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY"

mydb = mysql.connector.connect(
    host="freedb.tech",
    user="freedbtech_stavin",
   password="bro",
   database="freedbtech_prayer"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Prayers (point VARCHAR(255), tag VARCHAR(255))")

@app.route('/')
def main():
    mycursor.execute("SELECT * FROM Prayers")
    myresult = mycursor.fetchall()
    return render_template('index.html', myresult=myresult)


@app.route('/input', methods=['GET', 'POST'])
def inputs():
    if request.method=='POST':
        point = request.form['point']
        tag = request.form['tag']
        sql = "INSERT INTO Prayers (point, tag) VALUES (%s, %s)"
        val = (point, tag)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/")
    # print(mycursor.rowcount, "record inserted.")
    return render_template('input.html')

if __name__ == "__main__":
    app.run(debug=True)
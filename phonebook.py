from flask import Flask, render_template, request
import mysql.connector

app = Flask("MyApp")

conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='demo')

cur = conn.cursor()

@app.route("/")
def home():
    query = ("SELECT id, name, about FROM pb1")
    cur.execute(query)
    list = cur.fetchall()
    # q=request.args.get('q')
    return render_template("phonebook.html", friend_list=list, title="Friend List")

@app.route("/new_friend")
def new_friend():
     return render_template("new_friend.html")

@app.route("/submit_new_friend", methods=['POST'])
def submit_new_friend():
    name=request.form.get('name')
    email=request.form.get('email')
    website=request.form.get('website')
    about=request.form.get('about')
    query = "insert into pb1 (name,website,email,about) values ('%s','%s','%s', '%s')" % (name,website,email,about)
    cur.execute(query)
    conn.commit()
    return render_template("submit_new_friend.html", name=name, website=website, email=email, about=about)


if __name__ == "__main__":
    app.run(debug=True)

cur.close()
conn.close()

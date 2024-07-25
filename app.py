import psycopg2
from psycopg2 import OperationalError
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Register")



# For handling post request form we can get the form
# inputs value by using POST attribute.
# this values after submitting you will never see in the urls.
@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        passwordConfirm = request.form['passwordconfirm']
        age = request.form['age']
        validated = validate_input(username, password, passwordConfirm, email, age)
        if validated:
            if age == "":
                age = -1
            user = [email, password, username, age]


            insert_query = (
                f"INSERT INTO registered_users (email, password, username, age) VALUES {email, password, username, age}"
            )
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(insert_query, user)
            
            return '<h1>Welcome!!!</h1>'
        else:
            return render_template("index.html", title="Register")
        
        
        
    else:
        return render_template('index.html')
    

def validate_input(Username, Password, PasswordConfirm, Email, Age):
    z = 1
    while z == 1:
        if len(Username) < 21: z = 2
    y = 1
    while y == 1: 
        if len(Password) > 7 and len(Password) < 21 and any(x.isupper() for x in Password) and any(not x.isalnum() for x in Password): y = 2
    e = 1
    while e == 1:
        if Age == "": e = 2
        elif int(Age) > 0: e = 2
    h = 1
    while h == 1:
        if Email.endswith("@gmail.com" or "@hotmail.com" or "@outlook.com" or "@yahoo.com" or "@icloud.com"): h = 2
    if PasswordConfirm == Password:
        if z == 2 and y == 2 and e == 2 and h == 2:
            return True
    
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
    "blog_app", "postgres", "abc123", "127.0.0.1", "5432"
)

if __name__ == "__main__":
    app.run(debug=True)

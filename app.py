from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)

server = 'lefoot.database.windows.net'
database = 'lefootbal-server'
client_id = '74f9a752-947b-4098-9e3f-bccefdd3d265'
client_secret = '11ee7605-8750-4d5f-b540-a076227ba8aa'
tenant_id = 'ea2a6ba1-a44f-4d01-b99c-217bd4677f95'
driver = '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus(
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Authentication=ActiveDirectoryServicePrincipal;'
    f'UID={client_id};'
    f'PWD={client_secret};'
    f'Encrypt=yes;'
    f'TrustServerCertificate=no;'
    f'Connection Timeout=30;'
    f'Authority Id={tenant_id};'
) 

app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc:///?odbc_connect={params}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    m1 = db.Column(db.String(50))
    m2 = db.Column(db.String(50))      
    m3 = db.Column(db.String(50))
    m4 = db.Column(db.String(50))
    m5 = db.Column(db.String(50))
    m6 = db.Column(db.String(50))

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['fname']
        m1 = request.form['1']
        m2 = request.form['2']
        m3 = request.form['3']
        m4 = request.form['4']
        m5 = request.form['5']
        m6 = request.form['6']
    except KeyError as e:
        return f"Missing form field: {str(e)}", 400
    # Create a new user instance and add it to the database
    new_user = User(name=name, m1=m1, m2=m2, m3=m3, m4=m4, m5=m5, m6=m6)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('index'))


@app.route("/")
def index():
    print("i")
    return render_template("index.html")

@app.route("/joueurs")
def joueurs():
    print("j")
    return render_template("joueurs.html")

@app.route("/enationale/")
def enationale():
    print("n")
    return render_template("enationale.html")
@app.route("/paris")
def paris():
    print("n")
    return render_template("paris.html")

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
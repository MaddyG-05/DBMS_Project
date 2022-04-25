from contextlib import nullcontext
from click import style
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abcd'
app.config['MYSQL_DB'] = 'endsem_evaluation'

mysql = MySQL(app)

user_id=None
date = None

t_src_id=None
t_dest_id=None
t_train_id=None
t_class_type=None
t_date=None

b_src_id=None
b_dest_id=None
b_train_id=None

f_src_id=None
f_dest_id=None
f_train_id=None
f_class_type=None

@app.route('/')
def form():
    global user_id
    user_id=None
    return render_template('AdminPage.html')

@app.route('/Schedule')
def Schedule():
    return render_template('Schedule.html')

@app.route('/trainS')
def trainS():
    global user_id
    return render_template('trainS.html')

@app.route('/trainSchedule', methods = ['POST', 'GET'])
def trainSchedule():
    global date

    if(request.method == 'GET'):
        date = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct t.train_id, t.train_type, ts1.station_id, ts2.station_id, tfrom Train_booking where train_date ='{0}'""".format(date)
        cursor.execute(query, ())
        result=cursor.fetchall()
        print(result)
        cursor.close()
        return render_template("trainSchedule.html", value=result)

@app.route('/busesS')
def busesS():
    global user_id
    return render_template('busesS.html')

@app.route('/busesSchedule', methods = ['POST', 'GET'])
def busesSchedule():
    global date

    if(request.method == 'GET'):
        date = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct bus_id from Bus_booking where bus_date ='{0}'""".format(date)
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("busesSchedule.html", value=result)

@app.route('/flightS')
def flightS():
    global user_id
    return render_template('flightS.html')

@app.route('/flightsSchedule', methods = ['POST', 'GET'])
def flightsSchedule():
    global date

    if(request.method == 'GET'):
        date = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct flight_id from Flight_booking where flight_date ='{0}'""".format(date)
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("flightsSchedule.html", value=result)

@app.route('/Bookings')
def Bookings():
    global user_id
    return render_template('Bookings.html')

@app.route('/trainB')
def trainB():
    global user_id
    return render_template('trainB.html')

@app.route('/trainBooking', methods = ['POST', 'GET'])
def trainBooking():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("trainBooking.html", value=result)

@app.route('/busB')
def busB():
    global user_id
    return render_template('busB.html')

@app.route('/busBooking', methods = ['POST', 'GET'])
def busBooking():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        # id = request.form['']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("busBooking.html", value=result)

@app.route('/flightB')
def flightB():
    global user_id
    return render_template('flightB.html')

@app.route('/flightBooking', methods = ['POST', 'GET'])
def flightBooking():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("flightBooking.html", value=result)

@app.route('/Cancellation')
def Cancellation():
    global user_id
    return render_template('Cancellation.html')

@app.route('/trainC')
def trainC():
    global user_id
    return render_template('trainC.html')

@app.route('/trainCancel', methods = ['POST', 'GET'])
def trainCancel():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("Success.html", value=result)

@app.route('/busC')
def busC():
    global user_id
    return render_template('busC.html')

@app.route('/busCancel', methods = ['POST', 'GET'])
def busCancel():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("Success.html", value=result)

@app.route('/flightC')
def flightC():
    global user_id
    return render_template('flightC.html')

@app.route('/flightCancel', methods = ['POST', 'GET'])
def flightCancel():
    global date
    global id

    if(request.method == 'GET'):
        date = None
        id = None
        return render_template('error.html')

    if(request.method == 'POST'):
        date = request.form['dot']
        cursor=mysql.connection.cursor()
        query="""select distinct train_id from Train_booking where train_date ='{0}'""".format(date) #write
        cursor.execute(query, ())
        result=cursor.fetchall()
        return render_template("Success.html", value=result)

app.run(host='localhost', port=5000,debug=True)

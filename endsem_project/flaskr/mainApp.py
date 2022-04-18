from flask import Flask,render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abcd'
app.config['MYSQL_DB'] = 'endsem_evaluation'

mysql = MySQL(app)

user_id=None

t_src_id=None
t_dest_id=None
t_train_id=None
t_class_type=None

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
    return render_template('mainPage.html')

@app.route('/register')
def register():
    global user_id
    return render_template('register.html')

@app.route('/dashboard', methods=['POST', 'GET'])    #after you have registered
def dashboard():
    global user_id
    if(request.method=='GET'):
        user_id=None
        return render_template('error.html')
        # return "Go back"
        
    if(request.method=='POST'):
        id=request.form['userID']
        password=request.form['psw']
        cursor=mysql.connection.cursor()
        query="""select * from User where user_id='{0}'""".format(id)
        cursor.execute(query, ())
        user_record=cursor.fetchone()
        if(len(user_record)==0):
            return render_template('wrongLogin.html')
            # return "Wrong User ID or password"
        if(user_record[1]!=password):
            return render_template('wrongLogin.html')
            # return "Wrong User ID or password"

        
        user_id=id
        cursor.close()
        print(user_id)
        return render_template('dashboard.html')

@app.route('/postregistration', methods=['POST', 'GET'])
def postregistration():
    global user_id
    if(request.method=='GET'):
        user_id=None
        return render_template('error.html')
        # return "Wrong User ID or password"

    if(request.method=='POST'):
        id=request.form['userID']
        firstname=request.form['FirstName']
        lastname=request.form['LastName']
        password=request.form['psw']
        dob=request.form['dob']
        contactno=request.form['contactno']
        gender=request.form['gender']
        houseno=request.form['houseno']
        locality=request.form['locality']
        city=request.form['city']
        state=request.form['state']
        pincode=request.form['pincode']
        # print(request.form)
        query1="""select * from User where user_id='{0}'""".format(id)
        cursor=mysql.connection.cursor()
        cursor.execute(query1, ())
        if(len(cursor.fetchall())!=0):
            return render_template('unsuccessReg.html')
            # need ID main page somehow

        query2="""insert into User values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')""".format(id, password, contactno, dob, gender, firstname, lastname, houseno, locality, city, state, pincode)
        cursor.execute(query2, ())
        mysql.connection.commit()
        cursor.close()
        return render_template('successReg.html')
        # return "Wrong User ID or password"


@app.route('/agentLogin', methods=['POST', 'GET'])   #after you have logged in
def agentLogin():
    return "agentLogin"

@app.route('/contactUs', methods=['POST', 'GET'])   #selecting trains after log in
def contactUs():
    return render_template('contactUs.html')

@app.route('/trains', methods=['POST', 'GET'])
def trains():
    global user_id
    
    if(user_id==None):
        return render_template('error.html')
    return render_template('trains.html')

@app.route('/train1', methods=['POST', 'GET'])
def train1():
    global t_src_id, t_dest_id
    if(request.method=='GET'):
        return render_template('error.html')
    print(request.form)
    t_src_id=request.form['from']
    t_dest_id=request.form['to']
    query="""
    select Train.train_id, Train.train_type
	from Train, Train_stops t1, Train_stops t2
	where t1.train_id=Train.train_id 
	and t1.train_id=t2.train_id and t1.station_id='{0}' and t2.station_id='{1}'
	and((t2.arrival_day>t1.arrival_day) OR (t2.arrival_hour>t1.arrival_hour));""".format(t_src_id, t_dest_id)
    cursor=mysql.connection.cursor()
    cursor.execute(query, ())
    result=cursor.fetchall()
    print(result)
    cursor.close()
    return render_template("train1.html",value=result)

@app.route('/train2')
def train2():
    return 'train2'

@app.route('/train3')
def train3():
    return 'train3'















@app.route('/flights', methods=['POST', 'GET'])
def flights():
    global user_id
    
    if(user_id==None):
        return render_template('error.html')
    return render_template('flights.html')

@app.route('/buses', methods=['POST', 'GET'])
def buses():
    global user_id
    print(request.method)
    if(user_id==None):
        return render_template('error.html')
    return render_template('buses.html')

@app.route('/ticketdetails', methods=['POST', 'GET'])
def ticketdetails():
    print(user_id)
    return render_template('ticketDetails.html')




app.run(host='localhost', port=5000,debug=True)
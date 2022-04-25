from click import style
from flask import Flask,render_template, request, redirect
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
t_date=None
t_details=None

b_src_id=None
b_dest_id=None
b_bus_id=None
b_details=None

f_src_id=None
f_dest_id=None
f_flight_id=None
f_class_type=None
f_details=None

amount=None

# common/helper URLs
def reset():
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, b_src_id, b_dest_id, b_bus_id, b_details, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, amount
    user_id=None

    t_src_id=None
    t_dest_id=None
    t_train_id=None
    t_class_type=None
    t_date=None

    b_src_id=None
    b_dest_id=None
    b_bus_id=None
    b_details=None

    f_src_id=None
    f_dest_id=None
    f_flight_id=None
    f_class_type=None
    f_details=None

    amount=None

@app.route('/')
def form():
    reset()
    return render_template('mainPage.html')

@app.route('/mainApp')
def mainApp():
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard', methods=['POST', 'GET'])    
def dashboard():
    global user_id
    if(request.method=='GET'):
        reset()
        return redirect('/error')
        
    if(request.method=='POST'):
        id=request.form['userID']
        password=request.form['psw']
        cursor=mysql.connection.cursor()
        query="""select * from User where user_id='{0}'""".format(id)
        cursor.execute(query, ())
        user_record=cursor.fetchall()
        print(user_record)
        if(len(user_record)==0 or user_record==None):
            return redirect('/wrongLogin')
        if(user_record[0][1]!=password):
            return redirect('/wrongLogin')

        user_id=id
        cursor.close()
        print(user_id)
        return render_template('dashboard.html')

@app.route('/postregistration', methods=['POST', 'GET'])
def postregistration():
    global user_id
    if(request.method=='GET'):
        reset()
        return redirect('/error')
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
            return redirect('/unsuccessReg')
            # need ID main page somehow

        query2="""insert into User values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')""".format(id, password, contactno, dob, gender, firstname, lastname, houseno, locality, city, state, pincode)
        cursor.execute(query2, ())
        mysql.connection.commit()
        cursor.close()
        return render_template('successReg.html')

@app.route('/agentLogin', methods=['POST', 'GET'])   
def agentLogin():
    return "agentLogin"

@app.route('/contactUs', methods=['POST', 'GET'])   
def contactUs():
    return render_template('contactUs.html')

@app.route('/payment', methods=['POST', 'GET'])
def payment():
    if(request.method=='GET'):
        reset()
        return render_template('error.html')
    global t_train_id, t_details
    t_train_id=int(request.form['trainID'])
    train_choices=[train[0] for train in t_details]
    if(t_train_id in train_choices):
        return render_template('paymentPortal.html')
        
    return redirect('/trains')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/wrongLogin')
def incorrectLogin():
    return render_template('wrongLogin.html')
    
@app.route('/unsuccessReg')
def unsuccessReg():
    return render_template('unsuccessReg.html')

# ticket details
@app.route('/ticketdetails', methods=['POST', 'GET'])
def ticketdetails():
    print(user_id)
    return render_template('ticketDetails.html')

@app.route('/trainTicketDetails')
def trainTicketDetails():
    return render_template('trainTicketDetails.html')

@app.route('/busTicketDetails')
def busTicketDetails():
    return render_template('busTicketDetails.html')

@app.route('/flightTicketDetails')
def flightTicketDetails():
    return render_template('flightTicketDetails.html')

@app.route('/trainTicketDetails1')
def trainTicketDetails1():
    # return render_template('trainTicketDetails.html')
    return "bruh"

@app.route('/busTicketDetails1')
def busTicketDetails1():
    # return render_template('busTicketDetails.html')
    return "bruh"

@app.route('/busTicketDetails1')
def flightTicketDetails1():
    # return render_template('flightTicketDetails.html')
    return "bruh"

# train
@app.route('/trains', methods=['POST', 'GET'])
def trains():
    global user_id    
    if(user_id==None):
        return redirect('/error')
    return render_template('trains.html')

@app.route('/train1', methods=['POST', 'GET'])
def train1():
    # something about redirecting is broken, try and fix it.
    print(request.method)
    global t_src_id, t_dest_id, t_date, t_class_type, t_train_id, t_details
    if(request.method=='GET'):
        reset()
        return redirect('/error')
        
    # print(request.form)
    t_src_id=request.form['from']
    t_dest_id=request.form['to']
    t_date=request.form['dateTravel']
    t_class_type=request.form['class']
    query="""
    select t.train_id, t.train_type, ts1.departure_hour, ts1.departure_minute, ts2.arrival_hour, ts2.arrival_minute, ts2.departure_hour, ts2.departure_minute, (t.price_per_km*tdf.distance*tc.price_multiplier)
    from Train t, train_classes tc, Train_distance_from tdf, Train_stops ts1, Train_stops ts2
    where t.train_id=tc.train_id AND tc.class_type='{0}' AND count_of(tc.train_id, tc.class_type, '{1}')<tc.count_of_seats AND ((tdf.source_id='{2}' AND tdf.destination_id='{3}') OR (tdf.source_id='{3}' AND tdf.destination_id='{2}')) AND ts1.train_id=t.train_id AND ts2.train_id=t.train_id AND ts1.station_id='{2}' AND ts2.station_id='{3}' AND ((ts1.departure_day<ts2.arrival_day ) OR (ts1.departure_hour<ts2.arrival_hour) OR (ts1.departure_minute<ts2.arrival_minute));""".format(t_class_type, t_date, t_src_id, t_dest_id)
    cursor=mysql.connection.cursor()
    cursor.execute(query, ())
    queryresult=cursor.fetchall()
    t_details=queryresult
    result=[]
    for i in queryresult:
        temp=(i[0], i[1], str(i[2])+':'+str(i[3]), str(i[4])+':'+str(i[5]), str(i[6])+":"+str(i[7]), i[8])
        result.append(temp)
    print(result)
    cursor.close()
    if(len(result)==0):
        return render_template('notAvailable.html')
    return render_template("train1.html",value=result)

@app.route('/successBook', methods=['POST', 'GET'])
def successBook():
    if(request.method=='GET'):
        return render_template('error.html')
    global t_details, t_train_id, t_date, t_class_type, t_dest_id, t_src_id, user_id
    global f_details, f_src_id, f_dest_id, f_
    method=request.form['from']
    cursor=mysql.connection.cursor()
    query1="""
    select max(payment_id) from Payment"""
    cursor.execute(query1, ())
    result=cursor.fetchall()
    print(result)
    print(result[0][0])
    new_id=1
    if(result[0][0] is None):
        new_id=1
    else:
        new_id=result[0][0]+1
    # if(len(result)!=0):
    #     new_id=result[0][0]+1



    if(t_src_id!=None):
        required_train=None
        print(t_details)
        for train_detail in t_details:
            if(train_detail[0]==t_train_id):
                required_train=train_detail
                break
            required_train=None
        print(t_details)
        for train_detail in t_details:
            if(train_detail[0]==t_train_id):
                required_train=train_detail
                break
        
        price=required_train[-1]

        print(user_id)
        query2="""
        insert into Payment
        values('{0}', '{1}', '{2}')""".format(new_id, price, method)
        cursor.execute(query2, ())
        query3="""
        select max(ticket_id) from Train_booking"""
        cursor.execute(query3, ())
        new_train_id=1
        result3=cursor.fetchall()
        if(result3[0][0] is None):
            new_train_id=1
        else:
            new_train_id=result[0][0]+1
        mysql.connection.commit()
        query4="""
        insert into Train_booking
        values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');""".format(t_train_id, t_src_id, t_dest_id, user_id, new_train_id, new_id, t_date, t_class_type)
        cursor.execute(query4, ())
        mysql.connection.commit()
        cursor.close()

    if(b_src_id!=None):
        pass

    if(f_src_id!=None):
        pass

    return render_template('successReg.html')



@app.route('/flights', methods=['POST', 'GET'])
def flights():
    global user_id
    
    if(user_id==None):
        return redirect('/error')
    return render_template('flights.html')






app.run(host='localhost', port=5000,debug=True)
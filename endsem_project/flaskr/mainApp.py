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
b_date=None
b_details=None

f_src_id=None
f_dest_id=None
f_flight_id=None
f_class_type=None
f_details=None
f_date=None

amount=None

# common/helper URLs
def reset():
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, t_details, b_src_id, b_dest_id, b_bus_id, b_details, b_date, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, f_date, amount
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
    b_date=None
    b_details=None

    f_src_id=None
    f_dest_id=None
    f_flight_id=None
    f_class_type=None
    f_details=None
    f_date=None

    amount=None

def formatTime(time):
    if(time<10):
        return '0'+str(time)
    return str(time)

@app.route('/')
def form():
    reset()
    return render_template('mainPage.html')

@app.route('/mainApp')
def mainApp():
    return redirect('/')

@app.route('/mainPage')
def mainPage():
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
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, t_details, b_src_id, b_dest_id, b_bus_id, b_details, b_date, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, amount
    
    if(t_src_id!=None):
        t_train_id=int(request.form['ID'])
        train_choices=[train[0] for train in t_details]
        if(t_train_id in train_choices):
            return render_template('paymentPortal.html')
            
        return redirect('/trains')

    elif(b_src_id!=None):
        b_bus_id=int(request.form['ID'])
        bus_choices=[bus[0] for bus in b_details]
        if(b_bus_id in bus_choices):
            return render_template('paymentPortal.html')
            
        return redirect('/buses')

    elif(f_src_id!=None):
        f_flight_id=int(request.form['ID'])
        flight_choices=[flight[0] for flight in f_details]
        if(f_flight_id in flight_choices):
            return render_template('paymentPortal.html')
            
        return redirect('/flights')

    return redirect('/error')

@app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('error.html')

@app.route('/wrongLogin', methods=['POST', 'GET'])
def incorrectLogin():
    return render_template('wrongLogin.html')
    
@app.route('/unsuccessReg', methods=['POST', 'GET'])
def unsuccessReg():
    return render_template('unsuccessReg.html')

# ticket details
@app.route('/ticketDetails', methods=['POST', 'GET'])
def ticketdetails():
    return render_template('ticketDetails.html')

@app.route('/trainTicketDetails', methods=['POST', 'GET'])
def trainTicketDetails():
    return render_template('trainTicketDetails.html')

@app.route('/busTicketDetails', methods=['POST', 'GET'])
def busTicketDetails():
    return render_template('busTicketDetails.html')

@app.route('/flightTicketDetails', methods=['POST', 'GET'])
def flightTicketDetails():
    return render_template('flightTicketDetails.html')

@app.route('/trainTicketDetails1', methods=['POST', 'GET'])
def trainTicketDetails1():
    if(request.method=='GET'):
        return redirect('/error')
    
    ticket_id=request.form['ticketID']
    query1="""
    select tb.ticket_id, t.train_id, t.train_type, tb.train_class, tb.source_id, ts1.departure_hour, ts1.departure_minute, tb.destination_id, ts2.arrival_hour, ts2.arrival_minute, tb.train_date, p.amount
    from Train t, Train_booking tb, Train_stops ts1, Train_stops ts2, Payment p
    where t.train_id=tb.train_id AND ts1.train_id=t.train_id AND ts2.train_id=t.train_id AND tb.payment_id=p.payment_id AND tb.ticket_id='{0}' AND
    tb.source_id=ts1.station_id AND tb.destination_id=ts2.station_id;""".format(ticket_id)
    cursor=mysql.connection.cursor()
    cursor.execute(query1, ())
    queryresult=cursor.fetchall()
    result=[]
    for element in queryresult:
        temp=(element[0], element[1], element[2], element[3], element[4], formatTime(int(element[5]))+":"+formatTime(int(element[6])), element[7], formatTime(int(element[8]))+":"+formatTime(int(element[9])), element[10], element[11])
        result.append(temp)

    return render_template('trainTicketDetails1.html', value=result)

@app.route('/busTicketDetails1', methods=['POST', 'GET'])
def busTicketDetails1():
    if(request.method=='GET'):
        return redirect('/error')
    
    ticket_id=request.form['ticketID']
    query1="""
    select bb.ticket_id, b.bus_id, b.bus_type, bb.source_id, bs1.departure_hour, bs1.departure_minute, bb.destination_id, bs2.arrival_hour, bs2.arrival_minute, bb.bus_date, p.amount
    from Bus b, Bus_booking bb, Bus_stops_at bs1, Bus_stops_at bs2, Payment p
    where b.bus_id=bb.bus_id AND bs1.bus_id=b.bus_id AND bs2.bus_id=b.bus_id AND bb.payment_id=p.payment_id AND bb.ticket_id='{}' AND
    bb.source_id=bs1.bus_stop_ID AND bb.destination_id=bs2.bus_stop_id;""".format(ticket_id)
    cursor=mysql.connection.cursor()
    cursor.execute(query1, ())
    queryresult=cursor.fetchall()
    result=[]
    for element in queryresult:
        temp=(element[0], element[1], element[2], element[3], formatTime(int(element[4]))+":"+formatTime(int(element[5])), element[6], formatTime(int(element[7]))+":"+formatTime(int(element[8])), element[9], element[10])
        result.append(temp)

    return render_template('busTicketDetails1.html', value=result)

@app.route('/flightTicketDetails1', methods=['POST', 'GET'])
def flightTicketDetails1():
    if(request.method=='GET'):
        return redirect('/error')
    
    ticket_id=request.form['ticketID']
    query1="""
    select fb.ticket_id, f.flight_ID, f.flight_name, fc.class_type, f.src_id, f.departure_hour, f.departure_minute, f.dest_id, f.arrival_hour, f.arrival_minute, fb.flight_date, p.amount
    from Flight f, Flight_booking fb, Payment p, flight_classes fc
    where f.flight_ID=fb.flight_id AND fb.payment_id=p.payment_id AND fb.ticket_id='{0}' AND f.flight_id=fc.flight_id AND fb.flight_class=fc.class_type;""".format(ticket_id)
    cursor=mysql.connection.cursor()
    cursor.execute(query1, ())
    queryresult=cursor.fetchall()
    result=[]
    for element in queryresult:
        temp=(element[0], element[1], element[2], element[3], element[4], formatTime(int(element[5]))+":"+formatTime(int(element[6])), element[7], formatTime(int(element[8]))+":"+formatTime(int(element[9])), element[10], element[11])
        result.append(temp)

    return render_template('flightTicketDetails1.html', value=result)

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
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, t_details, b_src_id, b_dest_id, b_bus_id, b_details, b_date, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, amount
    b_src_id=None
    b_dest_id=None
    b_bus_id=None
    b_date=None
    b_details=None

    f_src_id=None
    f_dest_id=None
    f_flight_id=None
    f_class_type=None
    f_details=None

    amount=None
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
    where t.train_id=tc.train_id AND tc.class_type='{0}' AND count_of(tc.train_id, tc.class_type, '{1}')<tc.count_of_seats AND ((tdf.source_id='{2}' AND tdf.destination_id='{3}') OR (tdf.source_id='{3}' AND tdf.destination_id='{2}')) AND ts1.train_id=t.train_id AND ts2.train_id=t.train_id AND ts1.station_id='{2}' AND ts2.station_id='{3}' AND ((ts1.departure_day<ts2.arrival_day ) OR (ts1.departure_day=ts2.arrival_day AND ts1.departure_hour<ts2.arrival_hour) OR (ts1.departure_day=ts2.arrival_day AND ts1.departure_hour=ts2.arrival_hour AND ts1.departure_minute<ts2.arrival_minute));""".format(t_class_type, t_date, t_src_id, t_dest_id)
    print(query)
    cursor=mysql.connection.cursor()
    cursor.execute(query, ())
    queryresult=cursor.fetchall()
    t_details=queryresult
    result=[]
    for i in queryresult:
        temp=(i[0], i[1], formatTime(int(i[2]))+':'+formatTime(int(i[3])), formatTime(int(i[4]))+':'+formatTime(int(i[5])), formatTime(int(i[6]))+":"+formatTime(int(i[7])), i[8])
        result.append(temp)
    print(result)
    cursor.close()
    if(len(result)==0):
        return render_template('notAvailable.html')
    return render_template("train1.html",value=result)

@app.route('/buses', methods=['POST', 'GET'])
def buses():
    global user_id
    if(user_id is None):
        return redirect('/error')
    return render_template('buses.html')

@app.route('/bus1', methods=['POST', 'GET'])
def bus1():
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, t_details, b_src_id, b_dest_id, b_bus_id, b_details, b_date, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, amount

    t_src_id=None
    t_dest_id=None
    t_train_id=None
    t_class_type=None
    t_date=None
    t_details=None

    f_src_id=None
    f_dest_id=None
    f_flight_id=None
    f_class_type=None
    f_details=None

    amount=None
    if(request.method=='GET'):
        reset()
        return redirect('/error')
    
    b_src_id=int(request.form['from'])
    b_dest_id=int(request.form['to'])
    b_date=request.form['dateTravel']


    print(b_src_id)
    print(b_dest_id)
    print(b_date)
    query1="""
select b.bus_id, b.bus_type, bs1.departure_hour, bs1.departure_minute, bs2.arrival_hour, bs2.arrival_minute, bs2.departure_hour, bs2.departure_minute, (b.price_per_km*bdf.distance)
from Bus b, Bus_distance_from bdf, Bus_stops_at bs1, Bus_stops_at bs2
where count_of_bus(b.bus_id, '{0}')<b.count_of_seats AND ((bdf.source_id='{1}' AND bdf.destination_id='{2}') OR (bdf.source_id='{2}' AND bdf.destination_id='{1}')) AND bs1.bus_id=b.bus_id AND bs2.bus_id=b.bus_id AND bs1.bus_stop_id='{1}' AND bs2.bus_stop_id='{2}' AND ((bs1.departure_day<bs2.arrival_day ) OR (bs1.departure_day=bs2.arrival_day AND bs1.departure_hour<bs2.arrival_hour) OR (bs1.departure_day=bs2.arrival_day AND bs1.arrival_hour=bs2.arrival_hour AND bs1.departure_minute<bs2.arrival_minute));
""".format(b_date, b_src_id, b_dest_id)
    print(query1)

    cursor=mysql.connection.cursor()
    cursor.execute(query1)
    queryresult=cursor.fetchall()
    print(queryresult)
    b_details=queryresult
    result=[]
    for i in queryresult:
        temp=(i[0], i[1], str(i[2])+':'+str(i[3]), str(i[4])+':'+str(i[5]), str(i[6])+":"+str(i[7]), i[8])
        result.append(temp)
    print(result)
    cursor.close()
    if(len(result)==0):
        return render_template('notAvailable.html')
    return render_template("bus1.html",value=result)

@app.route('/flights', methods=['POST', 'GET'])
def flights():
    global user_id
    if(user_id==None):
        return redirect('/error')
    return render_template('flights.html')

@app.route('/flight1', methods=['POST', 'GET'])
def flight1():
    global user_id, t_src_id, t_dest_id, t_train_id, t_class_type, t_date, t_details, b_src_id, b_dest_id, b_bus_id, b_details, b_date, f_src_id, f_dest_id, f_flight_id, f_class_type, f_details, f_date, amount

    t_src_id=None
    t_dest_id=None
    t_train_id=None
    t_class_type=None
    t_date=None
    t_details=None

    b_src_id=None
    b_dest_id=None
    b_bus_id=None
    b_date=None
    b_details=None

    amount=None

    if(request.method=='GET'):
        reset()
        return redirect('/error')

    f_src_id=request.form['from']
    f_dest_id=request.form['to']
    f_date=request.form['dateTravel']
    f_class_type=request.form['class']
    print(f_src_id, f_dest_id, f_date, f_class_type)
    query1="""
select f.flight_ID, f.flight_name, f.departure_hour, f.departure_minute, f.arrival_hour, f.arrival_minute, (f.base_price*fc.price_multiplier)
from Flight f, flight_classes fc
where f.flight_ID=fc.flight_id AND f.src_ID='{0}' AND f.dest_id='{1}' AND count_of_flight(f.flight_id, fc.class_type, '{2}')<fc.count_of_seats AND fc.class_type='{3}';""".format(f_src_id, f_dest_id, f_date, f_class_type)
    cursor=mysql.connection.cursor()
    cursor.execute(query1, ())
    queryresult=cursor.fetchall()
    f_details=queryresult
    print(queryresult)
    result=[]
    for i in queryresult:
        temp=(i[0], i[1], str(i[2])+':'+str(i[3]), str(i[4])+':'+str(i[5]), i[6])
        result.append(temp)

    if(len(result)==0):
        return render_template('notAvailable.html')
    return render_template('flight1.html', value=result)
    return "Hello there"



@app.route('/successBook', methods=['POST', 'GET'])
def successBook():
    if(request.method=='GET'):
        return render_template('error.html')
    global t_details, t_train_id, t_date, t_class_type, t_dest_id, t_src_id, user_id
    global f_details, f_src_id, f_dest_id, f_flight_id, f_date, f_class_type
    global b_bus_id, b_src_id, b_dest_id, b_details, b_date
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
        
        
        price=required_train[-1]

        print(user_id)
        query2="""
        insert into Payment
        values('{0}', '{1}', '{2}')""".format(new_id, price, method)
        cursor.execute(query2, ())
        query3="""
        select max(ticket_id) from Train_booking"""
        cursor.execute(query3, ())
        result3=cursor.fetchall()
        query4="""
        select max(ticket_id) from Train_cancelled;"""
        new_train_id=1
        cursor.execute(query4, ())
        result4=cursor.fetchall()
        print(result3)
        print(result4)
        if(result3[0][0] is None and result4[0][0] is None):
            new_train_id=1
        elif(result3[0][0] is None):
            new_train_id=result4[0][0]+1
        elif(result4[0][0] is None):
            new_train_id=result3[0][0]+1

        else:
            new_train_id=max(result3[0][0], result4[0][0])+1

        mysql.connection.commit()
        query4="""
        insert into Train_booking
        values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');""".format(t_train_id, t_src_id, t_dest_id, user_id, new_train_id, new_id, t_date, t_class_type)
        cursor.execute(query4, ())
        mysql.connection.commit()
        cursor.close()
        reset()

    elif(b_src_id!=None):
        required_bus=None
        print(b_details)
        for bus_detail in b_details:
            if(bus_detail[0]==b_bus_id):
                required_bus=bus_detail
                break
        
        
        price=required_bus[-1]

        print(user_id)
        query2="""
        insert into Payment
        values('{0}', '{1}', '{2}')""".format(new_id, price, method)
        cursor.execute(query2, ())
        query3="""
        select max(ticket_id) from Bus_booking"""
        cursor.execute(query3, ())
        new_bus_id=1
        result3=cursor.fetchall()

        query4="""
        select max(ticket_id) from Bus_cancelled"""
        cursor.execute(query4, ())
        result4=cursor.fetchall()

        print(result3)
        print(result4)
        if(result3[0][0] is None and result4[0][0] is None):
            new_bus_id=1
        elif(result3[0][0] is None):
            new_bus_id=result4[0][0]+1
        elif(result4[0][0] is None):
            new_bus_id=result3[0][0]+1
        else:
            new_bus_id=max(result3[0][0], result4[0][0])+1
        mysql.connection.commit()
        query4="""
        insert into Bus_booking
        values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');""".format(b_bus_id, b_src_id, b_dest_id, user_id, new_bus_id, new_id, b_date)
        cursor.execute(query4, ())
        mysql.connection.commit()
        cursor.close()
        reset()

    elif(f_src_id!=None):
        required_flight=None
        print(f_details)
        for flight_detail in f_details:
            if(flight_detail[0]==f_flight_id):
                required_flight=flight_detail
                break
        
        
        price=required_flight[-1]

        print(user_id)
        query2="""
        insert into Payment
        values('{0}', '{1}', '{2}')""".format(new_id, price, method)
        cursor.execute(query2, ())
        query3="""
        select max(ticket_id) from Flight_booking"""
        cursor.execute(query3, ())
        new_flight_id=1
        result3=cursor.fetchall()


        query4="""
        select max(ticket_id) from Flight_cancelled"""
        cursor.execute(query4, ())
        result4=cursor.fetchall()

        print(result3)
        print(result4)
        if(result3[0][0] is None and result4[0][0] is None):
            new_flight_id=1
        elif(result3[0][0] is None):
            new_flight_id=result4[0][0]+1

        elif(result4[0][0] is None):
            new_flight_id=result3[0][0]+1

        else:
            new_flight_id=max(result3[0][0], result4[0][0])+1
            
        mysql.connection.commit()
        query4="""
        insert into Flight_booking
        values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');""".format(f_flight_id, f_src_id, f_dest_id, user_id, new_flight_id, new_id, f_date, f_class_type)
        cursor.execute(query4, ())
        mysql.connection.commit()
        cursor.close()
        reset()

    return render_template('successReg.html')

@app.route('/cancellationRedirect', methods=['POST', 'GET'])
def cancellationRedirect():
    if(user_id is None):
        return redirect('/error')

    return render_template('cancellationRedirect.html')

@app.route('/cancellation', methods=['POST', 'GET'])
def cancellation():
    if(request.method=='GET'):
        return redirect('/error')

    if(user_id is None):
        return redirect('/error')
    ticket_id=request.form['ticketID']
    choice=int(request.form['choice'])
    print(choice)
    if(choice==1):
        query="""
        delete from Train_booking
        where ticket_id='{}' AND user_id='{}'""".format(ticket_id, user_id)

        cursor=mysql.connection.cursor()
        cursor.execute(query, ())
        count=cursor.rowcount
        mysql.connection.commit()
        print(count)
        if(count==0):
            return "error"
    if(choice==2):
        query="""
        delete from Bus_booking
        where ticket_id='{}' AND user_id='{}'""".format(ticket_id, user_id)

        cursor=mysql.connection.cursor()
        cursor.execute(query, ())
        count=cursor.rowcount
        mysql.connection.commit()
        print(count)
        if(count==0):
            return "error"
    if(choice==3):
        query="""
        delete from Train_booking
        where ticket_id='{}' AND user_id='{}'""".format(ticket_id, user_id)

        cursor=mysql.connection.cursor()
        cursor.execute(query, ())
        count=cursor.rowcount
        mysql.connection.commit()
        print(count)
        if(count==0):
            return "error"

    return 'success'

app.run(host='localhost', port=5000,debug=True)
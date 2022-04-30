from flask import Flask,render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Admin'
app.config['MYSQL_PASSWORD'] = 'Admin123'
app.config['MYSQL_DB'] = 'endsem_evaluation'

mysql = MySQL(app)

def formatTime(time):
    if(time<10):
        return '0'+str(time)
    return str(time)

@app.route('/')
def form():
    return render_template('AdminPage.html')

@app.route('/error', methods=['POST', "GET"])
def error():
    return render_template('error.html')

@app.route('/payment', methods=['POST', "GET"])
def payments():
    # return 'Bruh'
    return render_template('payments.html')

@app.route('/payment1', methods=['POST', "GET"])
def payment1():
    return render_template('payment1.html')

@app.route('/paymentbyType', methods=['POST', "GET"])
def paymentByType():
    if(request.method=='GET'):
        return redirect('/error')

    vehicle=int(request.form['vehicle'])
    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        select * from TrainAllPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)

    elif(vehicle==2):
        cursor=mysql.connection.cursor()
        query1="""
        select * from BusAllPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)
    elif(vehicle==3):
        cursor=mysql.connection.cursor()
        query1="""
        select * from BusAllPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)

    return redirect('/error')

@app.route('/payment2', methods=['POST', "GET"])
def payment2():
    return render_template('payment2.html')

@app.route('/paymentbyDate', methods=['POST', "GET"])
def paymentbyDate():
    if(request.method=='GET'):
        return redirect('/error')

    vehicle=int(request.form['vehicle'])
    vehicle_id=int(request.form['ID'])
    date=request.form['dateTravel']
    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        select tb.train_id, tb.train_date, sum(p.amount), p.payment_type
        from Train_booking tb join Payment p on tb.payment_id=p.payment_id
        where tb.train_id='{}' AND tb.train_date='{}' 
        group by p.payment_type;""".format(vehicle_id, date)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyDate.html', value=queryresult)

    elif(vehicle==2):
        # return "Hello"
        cursor=mysql.connection.cursor()
        query1="""
        select bb.bus_id, bb.bus_date, sum(p.amount), p.payment_type
        from Bus_booking bb join Payment p on bb.payment_id=p.payment_id
        where bb.bus_id='{}' AND bb.bus_date='{}' 
        group by p.payment_type;""".format(vehicle_id, date)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyDate.html', value=queryresult)
    elif(vehicle==3):
        # return "Hello"
        cursor=mysql.connection.cursor()
        query1="""
        select fb.flight_id, fb.flight_date, sum(p.amount), p.payment_type
        from Flight_booking fb join Payment p on fb.payment_id=p.payment_id
        where fb.flight_id='{}' AND fb.flight_date='{}' 
        group by p.payment_type;""".format(vehicle_id, date)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyDate.html', value=queryresult)

    return redirect('/error')

@app.route('/payment3', methods=['POST', "GET"])
def payment3():
    return render_template('payment3.html')

@app.route('/paymentCancelled', methods=['POST', "GET"])
def paymentCancelled():
    if(request.method=='GET'):
        return redirect('/error')

    vehicle=int(request.form['vehicle'])
    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        select * from TrainAllCancelledPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)

    elif(vehicle==2):
        cursor=mysql.connection.cursor()
        query1="""
        select * from BusAllCancelledPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)
    elif(vehicle==3):
        cursor=mysql.connection.cursor()
        query1="""
        select * from BusAllCancelledPayments;"""
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        # result=[("PAYMENT ID", "TOTAL AMOUNT")]
        # for i in queryresult:
        #     result.append(i)

        # cursor.execute()
        return render_template('paymentbyType.html', value=queryresult)

    return redirect('/error')

@app.route('/schedule', methods=['POST', "GET"])
def schedules():
    return render_template('schedule.html')

@app.route('/schedule1', methods=['POST', "GET"])
def schedule1():
    return render_template('schedule1.html')

@app.route('/scheduleVehicle', methods=['POST', "GET"])
def scheduleVehicle():
    if(request.method=='GET'):
        return redirect('/error')

    vehicle=int(request.form['vehicle'])
    vehicle_id=int(request.form['ID'])
    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        select * from Train_stops where train_id='{0}' order by arrival_day, arrival_hour, arrival_minute""".format(vehicle_id)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        print(queryresult)
        
        result=[]
        for i in queryresult:
            temp=[i[0], i[1], formatTime(int(i[3]))+formatTime(int(i[4])), formatTime(int(i[6]))+formatTime(int(i[7]))]
            result.append(temp)

        mysql.connection.commit()
        cursor.close()
        return render_template('scheduleVehicle.html', value=result)
    if(vehicle==2):
        cursor=mysql.connection.cursor()
        query1="""
        select * from Bus_stops_at where bus_id='{0}' order by arrival_day, arrival_hour, arrival_minute""".format(vehicle_id)

        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        
        result=[]
        for i in queryresult:
            temp=[i[0], i[1], formatTime(int(i[3]))+":"+formatTime(int(i[4])), formatTime(int(i[6]))+":"+formatTime(int(i[7]))]
            result.append(temp)
        print
        mysql.connection.commit()
        cursor.close()
        return render_template('scheduleVehicle.html', value=result)
    if(vehicle==3):
        cursor=mysql.connection.cursor()
        query1="""
        select * from Flight where flight_id='{0}'""".format(vehicle_id)

        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        result=[]
        for i in queryresult:
            temp=[i[0], i[2], formatTime(int(i[5]))+":"+formatTime(int(i[6])),i[3], formatTime(int(i[7]))+":"+formatTime(int(i[8]))]
            result.append(temp)
        return render_template('scheduleFlight.html', value=result)

@app.route('/schedule2', methods=['POST', "GET"])
def schedule2():
    return render_template('schedule2.html')

@app.route('/scheduleStation', methods=['POST', "GET"])
def scheduleStation():
    source=request.form['ID']
    type=int(request.form['vehicle'])
    if(type==1):
        cursor=mysql.connection.cursor()
        query1="""
        select ts.station_id, ts.train_id, ts.departure_hour, ts.departure_minute from Train_stops ts where ts.station_id='{0}'""".format(source)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        # print(queryresult)
        
        result=[]
        for i in queryresult:
            temp=[i[0], i[1], formatTime(int(i[2]))+":"+formatTime(int(i[3]))]
            result.append(temp)

        mysql.connection.commit()
        cursor.close()
        return render_template('scheduleStation.html', value=result)

    elif(type==2):
        cursor=mysql.connection.cursor()
        query1="""
        select bs.bus_stop_id, bs.bus_id, bs.departure_hour, bs.departure_minute from Bus_stops_at bs where bs.bus_stop_id='{0}'""".format(source)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        # print(queryresult)
        
        result=[]
        for i in queryresult:
            temp=[i[0], i[1], formatTime(int(i[2]))+":"+formatTime(int(i[3]))]
            result.append(temp)

        mysql.connection.commit()
        cursor.close()
        return render_template('scheduleStation.html', value=result)

    elif(type==3):
        cursor=mysql.connection.cursor()
        query1="""
        select f.src_id , f.flight_id, f.departure_hour, f.departure_minute from Flight f where f.src_id='{0}'""".format(source)
        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        # print(queryresult)
        
        result=[]
        for i in queryresult:
            temp=[i[0], i[1], formatTime(int(i[2]))+":"+formatTime(int(i[3]))]
            result.append(temp)

        mysql.connection.commit()
        cursor.close()
        return render_template('scheduleStation.html', value=result)

@app.route('/bookings', methods=['POST', "GET"])
def booking():
    return render_template('booking.html')

@app.route('/booking1', methods=['POST', "GET"])
def booking1():
    return render_template('booking1.html')
 



@app.route('/bookingStation', methods=['POST', "GET"])
def bookingStation():
    if(request.method=='GET'):
        return redirect('/error')
    
    vehicle=int(request.form['vehicle'])
    src_id=request.form['src_ID']
    dest_id=request.form['dest_ID']
    date=request.form['dateTravel']
    print(vehicle)
    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        select tb.ticket_id, tb.train_id, tb.user_id, tb.train_class, tb.payment_id, p.amount
        from Train_booking tb join Payment p on tb.payment_id=p.payment_id 
        where tb.train_date='{0}' AND tb.source_id='{1}' AND tb.destination_id='{2}';""".format(date, src_id, dest_id)

        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        cursor.close()
        return render_template('bookingStation.html', value=queryresult)

    elif(vehicle==2):
        cursor=mysql.connection.cursor()
        query1="""
        select bb.ticket_id, bb.bus_id, bb.user_id, bb.payment_id, p.amount
        from Bus_booking bb join Payment p on bb.payment_id=p.payment_id 
        where bb.bus_date='{0}' AND bb.source_id='{1}' AND bb.destination_id='{2}';""".format(date, src_id, dest_id)

        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        cursor.close()
        result=[]
        print(queryresult)
        for i in queryresult:
            temp=(i[0], i[1], i[2], "-", i[3], i[4])
            result.append(temp)
        return render_template('bookingStation.html', value=result)


    elif(vehicle==3):
        cursor=mysql.connection.cursor()
        query1="""
        select fb.ticket_id, fb.flight_id, fb.user_id, fb.flight_class, fb.payment_id, p.amount
        from Flight_booking fb join Payment p on fb.payment_id=p.payment_id 
        where fb.flight_date='{0}' AND fb.source_id='{1}' AND fb.destination_id='{2}';""".format(date, src_id, dest_id)

        cursor.execute(query1, ())
        queryresult=cursor.fetchall()
        cursor.close()
        return render_template('bookingStation.html', value=queryresult)
    return redirect('/error')

    


@app.route('/booking2', methods=['POST', "GET"])
def booking2():
    return render_template('/booking2.html')

@app.route('/bookingCancelDate', methods=['POST', "GET"])
def bookingCancelDate():
    if(request.method=='GET'):
        return redirect('/error')
    vehicle=int(request.form['vehicle'])
    vehicle_id=request.form['vehicle_ID']
    date=request.form['dateTravel']

    if(vehicle==1):
        cursor=mysql.connection.cursor()
        query1="""
        delete from Train_booking
        where train_id='{}' AND train_date='{}'""".format(vehicle_id, date)
        cursor.execute(query1, ())
        mysql.connection.commit()
        cursor.close()
    if(vehicle==2):
        cursor=mysql.connection.cursor()
        query1="""
        delete from Bus_booking
        where bus_id='{}' AND bus_date='{}'""".format(vehicle_id, date)
        cursor.execute(query1, ())
        mysql.connection.commit()
        cursor.close()
    if(vehicle==3):
        cursor=mysql.connection.cursor()
        query1="""
        delete from Flight_booking
        where flight_id='{}' AND flight_date='{}'""".format(vehicle_id, date)
        cursor.execute(query1, ())
        mysql.connection.commit()
        cursor.close()

    return render_template('delete.html')

app.run(host='localhost', port=5500,debug=True)

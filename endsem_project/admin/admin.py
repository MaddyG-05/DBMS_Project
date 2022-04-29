from flask import Flask,render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Admin'
app.config['MYSQL_PASSWORD'] = 'Admin123'
app.config['MYSQL_DB'] = 'endsem_evaluation'

mysql = MySQL(app)


@app.route('/')
def form():
    return render_template('AdminPage.html')

@app.route('/payment', methods=['POST', "GET"])
def payments():
    return 'Bruh'
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


@app.route('/error', methods=['POST', "GET"])
def error():
    return render_template('error.html')

app.run(host='localhost', port=5500,debug=True)

from flask import Flask, render_template, request
import mysql.connector
from send_email import send_email
import qrcode
import qrcode.image.svg
from json2html import *
import webbrowser

con = mysql.connector.connect(
    user='root',
    password='123456',
    host='localhost',
    database='na_py1'
)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        year = request.form['year']
        phone = request.form['phone']
        gender = request.form['gender']
        vehicle_type = request.form['vehicle']
        vehicle_number = request.form['number']
        departure = request.form['departure']
        destination = request.form['destination']
        departure_day = request.form['fromDay']
        destination_day = request.form['toDay']
        fever = request.form['fever']
        cough = request.form['cough']
        stifling = request.form['stifling']
        pneumonia = request.form['pneumonia']
        throat = request.form['throat']
        tired = request.form['tired']
        in_contact_1 = request.form['in_contact_1']
        in_contact_2 = request.form['in_contact_2']
        in_contact_3 = request.form['in_contact_3']
        liver = request.form['liver']
        blood = request.form['blood']
        lung = request.form['lung']
        kidney = request.form['kidney']
        cancer = request.form['cancer']
        obj = {
            "name": name,
            "email": email,
            "phone": phone,
            "year_of_birth": year,
            "gender": gender,
            "vehicle_type": vehicle_type,
            "vehicle_number": vehicle_number,
            "departure": departure,
            "destination": destination,
            "departure_day": departure_day,
            "destination_day": destination_day,
            "fever": fever,
            "cough": cough,
            "stifling": stifling,
            "pneumonia": pneumonia,
            "throat": throat,
            "tired": tired,
            "in_contact_1": in_contact_1,
            "in_contact_2": in_contact_2,
            "in_contact_3": in_contact_3,
            "liver": liver,
            "blood": blood,
            "lung": lung,
            "kidney": kidney,
            "cancer": cancer,
        }

        img = qrcode.make(obj)
        img.save('qr.png')
        send_email(email)
        cursor = con.cursor()
        cursor.execute(f'INSERT INTO declaration(id, name, email, year, phone, gender, vehicle_type, vehicle_number, departure, destination, departure_day, destination_day, fever, cough, stifling, pneumonia, throat, tired, in_contact_1, in_contact_2, in_contact_3, liver, blood, lung, kidney, cancer) VALUES (0, "{name}", "{email}", "{year}", "{phone}", "{gender}", "{vehicle_type}", "{vehicle_number}", "{departure}", "{destination}", "{departure_day}", "{destination_day}", "{fever}", "{cough}", "{stifling}", "{pneumonia}", "{throat}", "{tired}", "{in_contact_1}", "{in_contact_2}", "{in_contact_3}", "{liver}", "{blood}", "{lung}", "{kidney}", "{cancer}")')
        con.commit()
        # con.close()
        return render_template('success.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
import smtplib,ssl
from email.mime.text import MIMEText

def send_mail(name, height ,weight,email):
    port = 465
    smtp_server = 'smtp.gmail.com'
    login = 'bmicalculator0@gmail.com'
    password = 'Saini@123'
    message = f"<h3> Your BMI</h3><ul><li>Name: {name}</li><li>Height: {height}</li><li>Weight: {weight}</li><li>BMI: {get_bmi(height, weight)}</li></ul>"

    sender_email = 'bmicalculator0@gmail.com'
    receiver_email = email
    msg = MIMEText(message , 'html')
    msg['Subject'] = 'Calculated BMI'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server , port) as server:
        server.ehlo()
        server.login(login , password)
        server.sendmail(sender_email , receiver_email , msg.as_string())
        server.close()





def get_bmi(height, weight):
    weight = float(weight)
    height = float (height)/100
    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    return bmi

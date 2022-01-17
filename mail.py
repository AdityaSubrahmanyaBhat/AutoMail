import smtplib



def send_mail(message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('from address','password_goes_here')
    server.sendmail('from address','to address',message)

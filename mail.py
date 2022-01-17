import smtplib




def send_mail(message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('4ni19cs010_a@nie.ac.in','password_goes_here')
    server.sendmail('4ni19cs010_a@nie.ac.in','adityasbhat1234@gmail.com',message)

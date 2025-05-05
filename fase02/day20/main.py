import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

email = input("Introduza su email: ")
password = input("Introduza su contraseña: ")

server.login(email, password)

email_addressee = input("Introduzca el email del destinatario: ")
subject = input("Introduzca el asunto: ")
content = input("Introduzca el contenido del mensaje: ")

server.sendmail(email, email_addressee, subject + "\n" + content)

server.quit()

import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "asd@gmail.com"  # Enter your address

def sendMails(couples):
	password = 'asdssasda' #your app password, see https://support.google.com/accounts/answer/185833
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		for c in couples:
			sendMail(c[0][0],c[0][1],c[1][0],server)
	pass

def sendMail(nome_dest,mail_dest,nome_rec,server):
	message=f'Car* {nome_dest} lei è caldamente invitat* a regalare qualche cacata a {nome_rec} in occasione della sacra festa del 2023° compleanno di Nostro Signore Gesù Cristo'
	server.sendmail(sender_email, mail_dest, message.encode('utf-8'))
	pass
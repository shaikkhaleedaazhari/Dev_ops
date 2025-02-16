import smtplib

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, "Test Email from Python")
server.quit()

print("Test email sent!")

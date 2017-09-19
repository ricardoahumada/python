import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

# Next, log in to the server
server.login("ricado@enmotionvalue.com", "izaskun777")
server.ehlo()
server.starttls()

# Send the mail
msg = "Hello!"  # The /n separates the message from the headers
server.sendmail("ricado@enmotionvalue.com", "rit7es@hotmail.com", msg)

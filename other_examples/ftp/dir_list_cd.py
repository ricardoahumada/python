import ftplib

ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")

data = []

ftp.cwd('/pub/')         # change directory to /pub/
ftp.dir(data.append)

ftp.quit()

for line in data:
    print("-", line)

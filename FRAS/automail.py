import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("herculep01020@gmail.com", "AxFg6667")

# sent the mail
yag.send(
    to="herculep01020@gmail.com",
    subject="attendance", # email subject
    contents="This is email",  # email body
)
print("Email Sent!")

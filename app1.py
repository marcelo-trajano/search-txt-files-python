import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

root_dir = "C:\\Users\\marce\\Desktop"
txt_files = []

# Find all txt files as before
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".txt"):
             txt_files.append(os.path.join(subdir, file))

# Email details
email_address = input("Enter the recipient email address: ")
email_password = input("Enter the email account password: ")
email_subject = "TXT files"
email_body = "Attached are the txt files found on the machine"

# Create the email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body))

# Add attachments
for txt_file in txt_files:
    with open(txt_file, "rb") as f:
        part = MIMEApplication(f.read(),_subtype="txt")
        part.add_header('content-disposition', 'attachment', filename=txt_file)
        msg.attach(part)

# Send the email
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(email_address, email_password)
smtp.sendmail(email_address, email_address, msg.as_string())

smtp.quit()
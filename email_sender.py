import datetime
import smtplib
import time

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()
msg = ""

def send_mail(from_address, password, to_address):
    smtp_obj.login(from_address, password)
    print("Email logged in")

    subject = input("Subject: \n")
    message = input("Message: \n")

    print("This will be your mail:\n")
    msg = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}"
    print(msg)

    return msg

def quit_mail():
    smtp_obj.quit()

def email_sender():
    from_address = input("Email: ")
    password = input("Password: ")
    to_address = from_address


    datetime_str = input("Enter date and time in the format YYYY-MM-DD HH:MM:SS: ")
    datetime_format = "%Y-%m-%d %H:%M:%S"

    try:
        send_time = datetime.datetime.strptime(datetime_str, datetime_format)
    except ValueError:
        print("Invalid datetime format. Please enter the datetime in YYYY-MM-DD HH:MM:SS format.")
        return

    msg = send_mail(from_address, password, to_address)

    # Calculate the delay until the send time
    delay = (send_time - datetime.datetime.now()).total_seconds()
    if delay > 0:
        print(f"Email will be sent in {delay} seconds.")
        time.sleep(delay)
        smtp_obj.sendmail(from_address, to_address, msg)
        print("Email is sent")
    else:
        print("The specified time is in the past. Please enter a future time.")

    quit_mail()

email_sender()
def send_email(receiver_email, subject, body):
    from email.message import EmailMessage
    import ssl
    import smtplib

    sender_email = 'surya.pratap120@gmail.com'
    passwod = 'kmdndwkcornmwzut'

    em = EmailMessage()

    em['From'] = sender_email
    em['To'] = receiver_email
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(sender_email, passwod)
        smtp.sendmail(sender_email, receiver_email, em.as_string())


if __name__ == '__main__':
    receiver_email = input("Enter receiver email: ").strip()
    subject = input("Enter email subject: ").strip()
    body = input("Write down the email body content: ").strip()

    if send_email(receiver_email, subject, body) == None:
        print("Email has been sent successfully..")

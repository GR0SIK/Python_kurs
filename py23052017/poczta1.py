import smtplib
from py23052017.secrets import *

adresat = moj_login

mailer = smtplib.SMTP('smtp.gmail.com', 587)

# witam sie z serwerem

mailer.ehlo()

mailer.starttls()

mailer.login(moj_login, moje_haslo)

temat = "Hello from Grzechu"
wiadomosc = "To jest moja wiadomość"

tresc = temat + wiadomosc

# wysyłanie maila

mailer.sendmail(moj_login, adresat, tresc)

mailer.quit()
import smtplib
from py23052017.secrets import *
from email.mime.text import MIMEText


adresat = moj_login

temat = "Wiadomość od Grzecha"
wiadomosc = "To jest treść moja wiadomość óź"

tresc = MIMEText(wiadomosc, _charset="utf-8")
tresc['Subject'] = temat
tresc['From'] = moj_login
tresc['To'] = moj_login

mailer = smtplib.SMTP('smtp.gmail.com', 587)

# witam sie z serwerem
mailer.ehlo()

# szyfrowanie
mailer.starttls()

# logowanie do konta
mailer.login(moj_login, moje_haslo)

# wysyłanie maila
# utf-8 musimy tresc maila - as_string from MIMEText
#for f in repr(4)
mailer.sendmail(moj_login, adresat, tresc.as_string())

# zamykamy polaczenie
mailer.quit()
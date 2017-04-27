import smtplib
from py27042017 import secrets

# definiuje dane do logowania

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo


# tworzenie silnika mailera

mailer = smtplib.SMTP('smtp.gmail.com', 587)

# witam sie z serwerem

mailer.ehlo()

# właczyć szyfrowanie

mailer.starttls()

# loguje sie

mailer.login(nadawca, haslo)

temat = "Subject: Hello from Grzegorz\n"
wiadomosc = "To jest tresc wiadomosci"
tresc = temat + wiadomosc

# wysyłam

mailer.sendmail(nadawca, adresat, tresc)

print("Wysłano maila")

mailer.quit()

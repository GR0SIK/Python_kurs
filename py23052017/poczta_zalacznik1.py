import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class Poczta(object):
    def __init__(self, login, haslo, server="smtp.gmail.com"):
        """Tworzy serwer pocztowy"""
        self.login = login
        self.haslo = haslo
        self.server = server

    def wyslij_wiadomosc(self, adresat, temat, tresc, pliki=None):
        """Wysyła wiadomość z załacznikami do adresatów
        adresat: lista
        pliki: lista
        """
        assert isinstance(adresat, list)

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = COMMASPACE.join(adresat)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = temat

        wiadomosc = MIMEText(tresc, _charset='utf-8')
        msg.attach(wiadomosc)

        for plik in pliki or []:
            with open(plik, 'rb') as zalacznik:
                part = MIMEApplication(
                    zalacznik.read(),
                    Name=basename(plik)
                )
                part['Content-Disposition'] = \
                    'attachment; filename="{}"'.format(basename(plik))

                msg.attach(part)

        mailer = smtplib.SMTP(self.server, 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.login(self.login, self.haslo)
        mailer.sendmail(self.login, adresat, msg.as_string())
        mailer.close()




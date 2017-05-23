import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.application import MIMENonMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
# domyslne argumenty zawsze na koncu
class Poczta(object):
    def __init__(self, login, haslo, server="smtp.gmail.com"):
        self.login = login
        self.haslo = haslo
        self.server = server
# None dlatego ze mozemy tez nie chciec wysylac zalacznikow
    def wyslij_wiadomosc(self, adresat, temat, tresc, pliki=None):
        """Wysyla wiadomosc z zalacznikami do adrestaow
        adresat: lista
        pliki: lista
        """
# sprawdzamy czy argument jest prawidlowy czy jest lista
        assert isinstance(adresat, list)
# tworzymy obiekt wiadomosci
        msg = MIMENonMultipart()
        msg['From'] = self.login
# wezmie nam z listy adresatow i polaczy jest w string do listy
        msg['To'] = COMMASPACE.join(adresat)
# musimy podac date i czas
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = temat

        wiadomosc = MIMEText(tresc, _charset='utf-8')
# dodajemy wiadomosc
        msg.attach(wiadomosc)
# sprawdza czy obiket jest lista jak nie jest przechodzi do drugiego
# jesli bedzie lista otwiera pliki jako binarne i laczy je w calosc
        for plik in pliki or []:
            with open(plik, 'rb') as zalacznik:
# jako argument podajemy zalacznik jako nazwe zalacznika wymierame basename i pobiera nazwe z pliku
                part = MIMEApplication(zalacznik.read(), Name=basename(plik))
# dodajemy formatowanie stringu
                part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(plik))
                #part['Content-Disposition'] = 'attachment; filename="%s' % basename(plik)
# dodajemy do naszej wiadomosci
                msg.attach(part)


        mailer = smtplib.SMTP(self.server, 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.login(self.login, self.haslo)
        mailer.sendmail(self.login, adresat, msg.as_string())
        mailer.close()


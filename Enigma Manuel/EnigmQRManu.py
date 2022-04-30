from pyzbar import pyzbar
from PIL import Image
import qrcode


# Données de teste
donnee = "{'F':'O','O':'F','G':'M','M':'G','L':'T','T':'L','H':'K','K':'H','J':'A','A':'J','E':'X','X':'E','D':'W','W':'D','I':'B','B':'I','Y':'V','V':'Y','Z':'S','S':'Z'};(RotorI,RotorV,RotorVII);(3,24,19);ReflectorB"
data="(RotorI,RotorV,RotorVII);(3,24,19);ReflectorB"

# Fichier d'enregistrement
QRCodefile = "sample.png"


# Paramètrage
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=1,
)


# Fonction pour passer de data à QRcode
def fToImage(data):
    global QRCodefile
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(QRCodefile)

# Fonction pour passer du QRcode à data
def fToData():
    global QRCodefile
    image = Image.open(QRCodefile)
    qr_code = pyzbar.decode(image)[0]
    data= qr_code.data.decode("utf-8")
    print(data)

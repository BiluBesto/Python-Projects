#QR code generator
import qrcode
data = input("Enter URL or text: ").strip()
fname= input("Enter file name: ").strip()
q=qrcode.QRCode(box_size=10,border=4)
q.add_data(data)
q.make(fit=True)
img=q.make_image(fill_color="black", back_color="white")
img.save(fname)
print("QR Code saved in",fname)
import qrcode
import qrcode.constants
from PIL import Image, ImageDraw, ImageFont

def create_qr_with_label(url, label, filename):
    # QR kodu oluşturma
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=7,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Resim boyutlarını al
    qr_width, qr_height = qr_image.size
    
    # Etiket için ekstra alan (örneğin 50 piksel)
    label_height = 50  
    new_img = Image.new('RGB', (qr_width, qr_height + label_height), "white")
    new_img.paste(qr_image, (0, 0))
    
    draw = ImageDraw.Draw(new_img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
    
    # draw.textbbox ile metnin sınırlarını alıyoruz
    # textbbox(xy, text, font=font) x ve y başlangıç koordinatını alır, sonuç (left, top, right, bottom)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Metni ortalamak için koordinatlar hesaplanıyor
    text_x = (qr_width - text_width) // 2
    text_y = qr_height + (label_height - text_height) // 2
    
    draw.text((text_x, text_y), label, fill="black", font=font)
    
    new_img.save(filename)
    new_img.show()
    print(f"{label} QR kodu '{filename}' olarak kaydedildi.")

linkler = {
    "GitHub Profil": "https://github.com/hdemirz",
    "LinkedIn Profil": "https://www.linkedin.com/in/hakan-demir-a8604b224/"
}

for label, url in linkler.items():
    dosya_adi = label.lower().replace(" ", "_") + "_qr.png"
    create_qr_with_label(url, label, dosya_adi)

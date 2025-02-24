# QR Kod Oluşturucu

Bu proje, Python kullanarak bir URL'den QR kod oluşturmak amacıyla hazırlanmıştır. Projede [qrcode](https://pypi.org/project/qrcode/) kütüphanesi kullanılmıştır.

## Özellikler

- Belirtilen URL'den QR kod üretimi
- QR kod renkleri özelleştirilebilir (dolgu ve arka plan rengi)
- Oluşturulan QR kodu bir PNG dosyası olarak kaydedilir

## Gereksinimler

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) kütüphanesi  
- [Pillow](https://pypi.org/project/Pillow/) kütüphanesi (otomatik olarak qrcode ile birlikte yüklenebilir)

## Kurulum

Öncelikle, gerekli paketleri yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

```bash
pip install qrcode[pil]

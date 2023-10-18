from PIL import Image


#Mesajımızı Binary'e Çevirme Fonksiyonu
def text_to_binary(text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

#Mesajımızı Binary'den Text'e Çevirme Fonksiyonu
def binary_to_text(binary_text):
    text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        text += chr(int(byte, 2))
    return text


#Mesajı Resme Gizleme Fonksiyonu
def hide_text_in_image(image_path, text_to_hide, output_path):
    img = Image.open(image_path)
    binary_text = text_to_binary(text_to_hide)

    if len(binary_text) > img.width * img.height * 3:
        print("Gizlenecek metin çok büyük, daha küçük bir metin kullanın veya daha büyük bir resim seçin.")
        return

    data_index = 0

    for y in range(img.height):
        for x in range(img.width):
            pixel = list(img.getpixel((x, y)))

            for i in range(3):
                if data_index < len(binary_text):
                    pixel[i] = pixel[i] & ~1 | int(binary_text[data_index])
                    data_index += 1

            img.putpixel((x, y), tuple(pixel))

            if data_index == len(binary_text):
                break

    img.save(output_path)
    print("Metin resme başarıyla gizlendi ve kaydedildi.")
    
    
#Mesajı Resimden Çıkarma Fonksiyonu
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    binary_text = ""

    for y in range(img.height):
        for x in range(img.width):
            pixel = list(img.getpixel((x, y)))

            for i in range(3):
                binary_text += str(pixel[i] & 1)

    hidden_text = binary_to_text(binary_text)
    return hidden_text



# Kullanım örneği
image_path = "stenografi.jpg"
text_to_hide = "Sifrelenmis metin"
output_path = "SifrelenmisResim.png"

hide_text_in_image(image_path, text_to_hide, output_path)

extracted_text = extract_text_from_image(output_path)
print("Çıkarılan Gizli Metin:", extracted_text)

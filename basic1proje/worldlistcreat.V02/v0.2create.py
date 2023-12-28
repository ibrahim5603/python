import tkinter as tk
from tkinter import ttk
from itertools import permutations
import threading
import os
from PIL import Image, ImageTk

def generate_passwords():
    girdi = entry.get()
    if not girdi:
        result_text.set("oluşturulması istenen karakterleri giriniz : ")
        return

    tum_siralamalar = []
    for i in range(1, len(girdi)+1):
        tum_siralamalar.extend(list(permutations(girdi, i)))

    total_permutations = len(tum_siralamalar)

    progress['maximum'] = total_permutations

    def generate():
        with open("guiolusturulan_sifre.txt", "w") as dosya:
            for i, şifre in enumerate(tum_siralamalar, start=1):
                dosya.write(''.join(şifre) + "\n")
                progress['value'] = i
                root.update_idletasks()

        result_text.set("Tüm şifreler başarıyla dosyaya yazıldı.")
        progress['value'] = 0
        entry.delete(0, tk.END)  # Girdi kutusunu temizle

    thread = threading.Thread(target=generate)
    thread.start()

def show_passwords():
    try:
        os.startfile("guiolusturulan_sifre.txt")
    except FileNotFoundError:
        result_text.set("Dosya bulunamadı.")

# Ana pencereyi oluşturun
root = tk.Tk()
root.title("Şifre Oluşturucu")
root.geometry("300x300+50+100")

# Arka plan resmini yükleme
bg_image = Image.open("14k.jpeg")  # Arka plan resmi dosyası
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Girdi kutusu ve etiket
label = tk.Label(root, text="Bir girdi girin:")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

# Şifre oluşturma düğmesi
generate_button = tk.Button(root, text="Şifreleri Oluştur", command=generate_passwords, bg="#4caf50", fg="white", relief="raised")
generate_button.pack(pady=5)

# İlerleme çubuğu
progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress.pack(padx=10, pady=5)

# Dosyayı gösterme düğmesi
show_button = tk.Button(root, text="Dosyayı Aç", command=show_passwords, bg="#2196f3", fg="white", relief="raised")
show_button.pack(pady=5)

# Sonuç metni
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=5)

# Arayüzü başlatma
root.mainloop()
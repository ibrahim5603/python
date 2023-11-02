import tkinter as tk
from itertools import permutations

def generate_passwords():
    girdi = entry.get()
    if not girdi:
        result_text.set("Lütfen bir girdi girin.")
        return

    tum_siralamalar = [''.join(siralama) for siralama in permutations(girdi)]

    with open("guiolusturulan_sifre", "w") as dosya:
        for şifre in tum_siralamalar:
            dosya.write(şifre + "\n")

    result_text.set("Tüm şifreler başarıyla dosyaya yazıldı.")

# Ana pencereyi oluşturun
root = tk.Tk()
root.title("Şifre Oluşturucu")
root.geometry("200x200+50+100")
# Girdi kutusu ve etiket
label = tk.Label(root, text="Bir girdi girin:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Şifre oluşturma düğmesi
generate_button = tk.Button(root, text="Şifreleri Oluştur", command=generate_passwords)
generate_button.pack()

# Sonuç metni
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()



# GUI'yi başlatın
root.mainloop()

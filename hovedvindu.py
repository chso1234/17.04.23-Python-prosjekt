import tkinter as tk

# Lag et Tkinter-vindu
root = tk.Tk()

# Lag etikett for temperatur-input
label_temp = tk.Label(root, text="Skriv inn temperatur i Celsius:")
label_temp.pack()

# Lag tekstboks for temperatur-input
entry_temp = tk.Entry(root)
entry_temp.pack()

# Lag etikett for konverteringsresultat
label_result = tk.Label(root, text="")
label_result.pack()



# Lag knapp for å konvertere temperatur
button_convert = tk.Button(root, text="Konverter",)
button_convert.pack()

# Start Tkinter-loopen
root.mainloop()

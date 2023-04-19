import tkinter as tk
import funksjoner

# Lag et Tkinter-vindu
root = tk.Tk()

# Lag etikett for Celsius-input
label_celsius = tk.Label(root, text="Skriv inn temperatur i Celsius:")
label_celsius.pack()

label_temp2 = tk.Label(root, text= "Skriv inn temperatur i fahrenheit:")
label_temp2.pack()

# Lag tekstboks for temperatur-input
entry_temp = tk.Entry(root,)
entry_temp.pack()

# Lag etikett for konverteringsresultat
label_result = tk.Label(root, text="")
label_result.pack()

# Lag funksjon for å konvertere temperatur
def convert_temp():
    celsius = entry_celsius.get()
    fahrenheit = entry_fahrenheit.get()

    if celsius:
        celsius = float(celsius)
        fahrenheit = funksjoner.tempconvert(celcius=celsius)
        label_result.config(text=f"{celsius} grader Celsius = {fahrenheit} grader Fahrenheit")
    elif fahrenheit:
        fahrenheit = float(fahrenheit)
        celsius = funksjoner.tempconvert(farenheit=fahrenheit)
        label_result.config(text=f"{fahrenheit} grader Fahrenheit = {celsius} grader Celsius")
    else:
        label_result.config(text="Feil: Vennligst skriv inn en temperaturverdi.")


# Lag knapp for å konvertere temperatur
button_convert = tk.Button(root, text="Konverter", command=convert_temp)
button_convert.pack()

# Start Tkinter-loopen
root.mainloop()

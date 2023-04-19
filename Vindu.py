import tkinter as tk
import funksjoner

# Lag et Tkinter-vindu
root = tk.Tk()
root.title("Temperaturkonvertering")

# Lag etikett for Celsius-input
label_celsius = tk.Label(root, text="Skriv inn temperatur i Celsius:")
label_celsius.pack()

# Lag tekstboks for Celsius-input
entry_celsius = tk.Entry(root, width=20, justify="center")
entry_celsius.pack(pady=10)
entry_celsius.insert(0, "Skriv inn Celsius-temperatur")
entry_celsius.bind("<FocusIn>", lambda event: entry_celsius.delete(0, tk.END))

# Lag etikett for Fahrenheit-input
label_fahrenheit = tk.Label(root, text="Skriv inn temperatur i Fahrenheit:")
label_fahrenheit.pack()

# Lag tekstboks for Fahrenheit-input
entry_fahrenheit = tk.Entry(root, width=20, justify="center")
entry_fahrenheit.pack(pady=10)
entry_fahrenheit.insert(0, "Skriv inn Fahrenheit-temperatur")
entry_fahrenheit.bind("<FocusIn>", lambda event: entry_fahrenheit.delete(0, tk.END))

# Lag etikett for konverteringsresultat
label_result = tk.Label(root, text="")
label_result.pack(pady=10)
label_result.pack_forget()

# Lag funksjon for å konvertere temperatur
def convert_temp():
    celsius = entry_celsius.get()
    fahrenheit = entry_fahrenheit.get()

    if celsius:
        celsius = float(celsius)
        fahrenheit = funksjoner.tempconvert(celcius=celsius)
        result_text = f"{celsius} grader Celsius = {fahrenheit} grader Fahrenheit"
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, fahrenheit)
    elif fahrenheit:
        fahrenheit = float(fahrenheit)
        celsius = funksjoner.tempconvert(farenheit=fahrenheit)
        result_text = f"{fahrenheit} grader Fahrenheit = {celsius} grader Celsius"
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, celsius)
    else:
        result_text = "Feil: Vennligst skriv inn en temperaturverdi."

    label_result.config(text=result_text)
    label_result.pack()

# Lag knapp for å konvertere temperatur
button_convert = tk.Button(root, text="Konverter", command=convert_temp)
button_convert.pack(pady=10)

# Start Tkinter-loopen
root.mainloop()

import tkinter as tk
import requests
import json
from tkinter import ttk
from tkinter.messagebox import showerror

# Api requests
api_key = " "            # Enter API Key
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
response = requests.get(f"{url}").json()
currencies = dict(response['conversion_rates'])


def convert_currency():
    try:
        source = from_currency_combo.get()
        destination = to_currency_combo.get()
        amount = amount_entry.get()
        result = requests.get(
            f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source}/{destination}/{amount}").json()
        converted_result = result['conversion_result']
        formatted_result = f'{amount} {source} = {converted_result} {destination}'
        resul_label.config(text=formatted_result)
    except:
        showerror(title="Error", message="An error occurred!")


# Creating main window

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300+500+200")
root.resizable(False, False)

# Aplication colors
primary = "#005dcf"
secondary = "#0083FF"
# white = "#FFFFFF"

# Creating, labels, buttons
name_label = tk.Label(root, text="Currency Converter", font=("Poppins", 10, "bold"),
                      fg="black", padx=10,
                      pady=10)
name_label.grid(row=0, column=0)

from_label = tk.Label(root, text="FROM", font=("Poppins", 10, "bold"), justify="left", padx=5, pady=5)
from_label.grid(row=1, column=0)
to_label = tk.Label(root, text="TO", font=("Poppins", 10, "bold"), pady=5, padx=5)
to_label.grid(row=1, column=2)

# combox currency

from_currency_combo = ttk.Combobox(root, width=12, values=list(currencies.keys()), font=("Poppins", 10, "bold"))
from_currency_combo.grid(row=2, column=0)

to_currency_combo = ttk.Combobox(root, width=12, values=list(currencies.keys()), font=("Poppins", 10, "bold"))
to_currency_combo.grid(row=2, column=2)

# Amount label, and text entry

amount_label = tk.Label(root, text="AMOUNT", font=("Poppins", 10, "bold"), padx=5, pady=5)
amount_label.grid(row=3, column=0)

amount_entry = tk.Entry(root, width=30, font=("Poppins", 10, "bold"))
amount_entry.grid(row=4, column=0, padx=5, pady=5)

resul_label = tk.Label(root, text="", font=("Poppins", 10, "bold"))
resul_label.grid(row=5, column=0)

convert_btn = tk.Button(root, text="CONVERT", font=("Poppins", 10, "bold"), command=convert_currency)
convert_btn.grid(row=6, column=0)

quit_btn = tk.Button(root, text="QUIT", font=("Poppins", 10, "bold"), command=root.quit)
quit_btn.grid(row=6, column=2)

root.mainloop()

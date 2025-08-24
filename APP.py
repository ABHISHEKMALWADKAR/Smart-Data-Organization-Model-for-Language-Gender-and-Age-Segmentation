import pandas as pd
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tabulate import tabulate
from ipyleaflet import Map
import webbrowser
# Load data
df = pd.read_csv("D:\\PYTHON\\Final project\\Languages.txt", sep="\t")

root = tk.Tk()
root.title("Language Data Filter")
root.geometry("900x500")
root.configure(bg="#F9F3F3")
label_bg = "#f0f4f7"
label_fg = "#2d4159"
entry_bg = "#3c0d0d"
entry_fg = "#2d4159"
button_bg = "#00d7ef"
button_fg = "#ffffff"

# display(m)  # Removed because 'display' is not defined and ipyleaflet is not compatible with Tkinter


gender_var = tk.StringVar()
age_var = tk.StringVar()
country_var = tk.StringVar()
language_var = tk.StringVar()

def save():
    gender = gender_var.get().strip()
    age = age_var.get().strip()
    country = country_var.get().strip()
    language = language_var.get().strip()

    filtered = df[
        (df['Gender'].str.lower() == gender.lower() if gender else True) &
        (df['Age'].astype(str) == age if age else True) &
        (df['Country'].str.lower() == country.lower() if country else True) &
        (
            df['Native Language'].str.lower().str.contains(language.lower()) |
            df['Other Languages'].str.lower().str.contains(language.lower())
        if language else True)
    ]

    output_text.delete(1.0, tk.END)  # Clear previous output

    if filtered.empty:
        messagebox.showinfo("No Data", "No records found for the given filters.")
    else:
        table = tabulate(filtered, headers='keys', tablefmt='grid', showindex=False)
        output_text.insert(tk.END, table)
        output_text.insert(tk.END, filtered.to_string(index=False))
        output_path = "D:\\PYTHON\\SOFTWARE DEVELOPMENT\\Final project\\Sorted data.csv"
        filtered.to_csv(output_path, index=False)
        messagebox.showinfo("Success", f"Filtered data saved to:\n{output_path}")
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def show_map():
    messagebox.showinfo("Map", "Map functionality is not implemented in this Tkinter app.")

tk.Label(root, text="Gender:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, textvariable=gender_var).grid(row=0, column=1)
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)
tk.Label(root, text="Country:").grid(row=2, column=0, sticky="e",   padx=10, pady=5)
tk.Entry(root, textvariable=country_var).grid(row=2, column=1)
tk.Label(root, text="Language:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, textvariable=language_var).grid(row=3, column=1)


tk.Button(
    root,
    text="Filter and Show Output",
    command=save,
    bg=button_bg,
    fg=button_fg,
    font=("Arial", 12, "bold"),
    activebackground="#388e3c",
    activeforeground="#ffffff"
).grid(row=4, column=0, columnspan=2, pady=20, padx=10, sticky="ew")


output_text = scrolledtext.ScrolledText(root, width=110, height=15, font=("Consolas", 10), bg="#f8f8f8")
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
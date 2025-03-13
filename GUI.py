import tkinter as tk
from tkinter import messagebox
from firebase_config import db

def add_user():
    user_id = entry_user_id.get()
    name = entry_name.get()
    age = entry_age.get()
    height = entry_height.get()
    weight = entry_weight.get()
    
    if not (user_id and name and age and height and weight):
        messagebox.showerror("Fel", "Alla fält måste fyllas i!")
        return
    
    db.collection("users").document(user_id).set({
        "name": name,
        "age": int(age),
        "height": float(height),
        "weight": float(weight)
    })
    messagebox.showinfo("Success", f"Användaren {name} har lagts till!")

def get_user():
    user_id = entry_user_id.get()
    doc = db.collection("users").document(user_id).get()
    if doc.exists:
        user_data = doc.to_dict()
        messagebox.showinfo("Användardata", str(user_data))
    else:
        messagebox.showerror("Fel", "Användaren finns inte!")

def update_user():
    user_id = entry_user_id.get()
    field = entry_field.get()
    value = entry_value.get()
    
    if not (user_id and field and value):
        messagebox.showerror("Fel", "Alla fält måste fyllas i!")
        return
    
    db.collection("users").document(user_id).update({field: value})
    messagebox.showinfo("Success", f"{field} uppdaterades till {value}")

def delete_user():
    user_id = entry_user_id.get()
    db.collection("users").document(user_id).delete()
    messagebox.showinfo("Success", f"Användaren {user_id} raderades!")

def log_meal():
    user_id = entry_user_id.get()
    meal = entry_meal.get()
    calories = entry_calories.get()
    
    if not (user_id and meal and calories):
        messagebox.showerror("Fel", "Alla fält måste fyllas i!")
        return
    
    db.collection("users").document(user_id).collection("meals").add({
        "meal": meal,
        "calories": int(calories)
    })
    messagebox.showinfo("Success", f"Måltiden '{meal}' lagts till!")


root = tk.Tk()
root.title("Health Tracker")
root.geometry("500x600")

tk.Label(root, text="Användar-ID:").pack()
entry_user_id = tk.Entry(root)
entry_user_id.pack()

tk.Label(root, text="Namn:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Ålder:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Längd (cm):").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Vikt (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Lägg till användare", command=add_user).pack()

tk.Button(root, text="Hämta användardata", command=get_user).pack()

tk.Label(root, text="Fält att uppdatera:").pack()
entry_field = tk.Entry(root)
entry_field.pack()

tk.Label(root, text="Nytt värde:").pack()
entry_value = tk.Entry(root)
entry_value.pack()

tk.Button(root, text="Uppdatera användare", command=update_user).pack()

tk.Button(root, text="Ta bort användare", command=delete_user).pack()

tk.Label(root, text="Måltid:").pack()
entry_meal = tk.Entry(root)
entry_meal.pack()

tk.Label(root, text="Kalorier:").pack()
entry_calories = tk.Entry(root)
entry_calories.pack()

tk.Button(root, text="Logga måltid", command=log_meal).pack()

root.mainloop()

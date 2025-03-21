import time
import firebase_admin
from firebase_admin import credentials, db
#from firebase_config import firebase_db as db
import tkinter as tk
from tkinter import messagebox, ttk
import random

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("agila-utveckling-firebase-adminsdk-fbsvc-585f89298c.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://agila-utveckling-default-rtdb.firebaseio.com/'})

def calculate_calories(meals):
    time.sleep(2)  # Simulate slow process
    calorie_data = {"egg": 78, "bread": 75, "rice": 200, "chicken": 250, "apple": 95, "banana": 105}
    total_calories = sum(calorie_data.get(meal.lower(), random.randint(50, 300)) for meal in meals)
    return total_calories

def update_statistics(user_id, total_calories):
    ref = db.reference("/statistics")
    stats = ref.get() or {"total_users": 0, "total_calories": 0}
    users_ref = db.reference("/users")
    
    if user_id not in (users_ref.get() or {}):
        stats["total_users"] += 1
    
    stats["total_calories"] += total_calories
    ref.set(stats)
    users_ref.child(user_id).set({"calories": total_calories})

def fetch_statistics():
    ref = db.reference("/statistics")
    stats = ref.get() or {"total_users": 0, "total_calories": 0}
    messagebox.showinfo("Statistics", f"Total Users: {stats['total_users']}\nTotal Calories Recorded: {stats['total_calories']}")

def stress_relief():
    messagebox.showinfo("Relax", "Inhale...\nHold...\nExhale...\nRepeat 3 times")

def recommend_health(goal, total_calories):
    # Recommendations based on goal and calories
    if goal == "Muscle Building":
        if total_calories < 2500:
            recommendation = "Your calorie intake is low for muscle building. Consider increasing your intake with protein-rich foods!"
        elif 2500 <= total_calories <= 3000:
            recommendation = "Great! You're on track for muscle building. Ensure you're getting enough protein."
        else:
            recommendation = "You're consuming too many calories for muscle building. Consider a slight reduction and focus on protein-rich foods."
    
    elif goal == "Weight Loss":
        if total_calories < 1500:
            recommendation = "Your calorie intake is very low for weight loss. Ensure you're getting enough nutrients and vitamins."
        elif 1500 <= total_calories <= 1800:
            recommendation = "Good job! You're in the ideal calorie range for weight loss. Keep going!"
        else:
            recommendation = "You're consuming too many calories for weight loss. Consider reducing your intake and focus on a balanced diet."
    
    elif goal == "Maintenance":
        if total_calories < 2000:
            recommendation = "Your calorie intake is a bit low for maintenance. Consider eating a bit more for energy."
        elif 2000 <= total_calories <= 2500:
            recommendation = "Perfect! You're in the ideal range for maintaining your current weight."
        else:
            recommendation = "You're consuming too many calories for maintenance. Consider reducing your intake slightly."

    return recommendation



def submit_meals():
    user_id = user_id_entry.get()
    meals = [breakfast_entry.get(), lunch_entry.get(), dinner_entry.get()]
    total_calories = calculate_calories(meals)
    update_statistics(user_id, total_calories)
    messagebox.showinfo("Result", f"Your total calorie intake: {total_calories} kcal")

def about():
    messagebox.showinfo("About", "Health Tracker App\nCreated by Your Name")

def quit_app():
    root.destroy()

# GUI Setup
def main():
    global user_id_entry, breakfast_entry, lunch_entry, dinner_entry
    root = tk.Tk()
    root.title("Health Tracker")
    root.geometry("400x500")
    root.configure(bg="#f0f0f0")

    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Create a "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Quit", command=quit_app)

    # Create a "Help" menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    
    frame = tk.Frame(root, bg="#d9e4dd", padx=10, pady=10)
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
    tk.Label(frame, text="User ID:", bg="#d9e4dd", font=("Arial", 12)).pack()
    user_id_entry = tk.Entry(frame, font=("Arial", 12))
    user_id_entry.pack()
    
    tk.Label(frame, text="Breakfast:", bg="#d9e4dd", font=("Arial", 12)).pack()
    breakfast_entry = tk.Entry(frame, font=("Arial", 12))
    breakfast_entry.pack()
    
    tk.Label(frame, text="Lunch:", bg="#d9e4dd", font=("Arial", 12)).pack()
    lunch_entry = tk.Entry(frame, font=("Arial", 12))
    lunch_entry.pack()
    
    tk.Label(frame, text="Dinner:", bg="#d9e4dd", font=("Arial", 12)).pack()
    dinner_entry = tk.Entry(frame, font=("Arial", 12))
    dinner_entry.pack()

    tk.Label(frame, text="Your Goal:", bg="#d9e4dd", font=("Arial", 12)).pack()
    goal_combobox = ttk.Combobox(frame, values=["Muscle Building", "Weight Loss", "Maintenance"], font=("Arial", 12))
    goal_combobox.set("Maintenance")
    goal_combobox.pack()
    
    tk.Button(frame, text="Submit", command=submit_meals, font=("Arial", 12), bg="#87ceeb").pack(pady=5)
    tk.Button(frame, text="View Statistics", command=fetch_statistics, font=("Arial", 12), bg="#ffa07a").pack(pady=5)
    tk.Button(frame, text="Relax", command=stress_relief, font=("Arial", 12), bg="#90ee90").pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()

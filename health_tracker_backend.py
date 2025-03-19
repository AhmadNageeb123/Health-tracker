from firebase_config import db

def add_user(user_id, name, age, height, weight):
    user_ref = db.collection("users").document(user_id)
    user_ref.set({
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    })
    print(f"✅ Användaren {name} har lagts till!")

def get_user(user_id):
    user_ref = db.collection("users").document(user_id)
    doc = user_ref.get()
    if doc.exists:
        print(f"📄 Användardata: {doc.to_dict()}")
    else:
        print("❌ Användaren finns inte.")

def update_user(user_id, field, value):
    user_ref = db.collection("users").document(user_id)
    user_ref.update({field: value})
    print(f"✅ {field} har uppdaterats till {value} för användare {user_id}!")

def delete_user(user_id):
    user_ref = db.collection("users").document(user_id)
    user_ref.delete()
    print(f"❌ Användaren {user_id} har raderats!")

def log_meal(user_id, meal, calories):
    meal_ref = db.collection("users").document(user_id).collection("meals").document()
    meal_ref.set({
        "meal": meal,
        "calories": calories
    })
    print(f"🍽 Måltiden '{meal}' har lagts till för {user_id}!")

def get_meals(user_id):
    meals_ref = db.collection("users").document(user_id).collection("meals").stream()
    meals = [meal.to_dict() for meal in meals_ref]
    if meals:
        print(f"📄 Måltider för {user_id}: {meals}")
    else:
        print("❌ Inga måltider hittades.")

def main():
    while True:
        print("\n--- Hälsospårningssystem ---")
        print("1. Lägg till användare")
        print("2. Hämta användardata")
        print("3. Uppdatera användardata")
        print("4. Ta bort användare")
        print("5. Logga måltid")
        print("6. Hämta måltider")
        print("7. Avsluta")
        
        choice = input("Välj ett alternativ (1-7): ")
        
        if choice == "1":
            user_id = input("Ange användar-ID: ")
            name = input("Ange namn: ")
            age = int(input("Ange ålder: "))
            height = float(input("Ange längd (cm): "))
            weight = float(input("Ange vikt (kg): "))
            add_user(user_id, name, age, height, weight)
        elif choice == "2":
            user_id = input("Ange användar-ID: ")
            get_user(user_id)
        elif choice == "3":
            user_id = input("Ange användar-ID: ")
            field = input("Ange fält att uppdatera (name, age, height, weight): ")
            value = input("Ange nytt värde: ")
            update_user(user_id, field, value)
        elif choice == "4":
            user_id = input("Ange användar-ID: ")
            delete_user(user_id)
        elif choice == "5":
            user_id = input("Ange användar-ID: ")
            meal = input("Ange måltid: ")
            calories = int(input("Ange kalorier: "))
            log_meal(user_id, meal, calories)
        elif choice == "6":
            user_id = input("Ange användar-ID: ")
            get_meals(user_id)
        elif choice == "7":
            print("Avslutar programmet...")
            break
        else:
            print("❌ Ogiltigt val, försök igen!")


def get_statistics():
    users_ref = db.collection("users").stream()
    total_users = 0
    total_age = 0
    total_height = 0
    total_weight = 0
    total_meals = 0

    for user in users_ref:
        user_data = user.to_dict()
        total_users += 1
        total_age += user_data.get("age", 0)
        total_height += user_data.get("height", 0)
        total_weight += user_data.get("weight", 0)

        # Hämta måltider för användaren
        meals_ref = db.collection("users").document(user.id).collection("meals").stream()
        total_meals += sum(1 for _ in meals_ref)

    if total_users == 0:
        return "Ingen statistik tillgänglig (inga användare i databasen)."

    avg_age = total_age / total_users
    avg_height = total_height / total_users
    avg_weight = total_weight / total_users

    return f"""📊 Statistik:
    - Totalt antal användare: {total_users}
    - Genomsnittlig ålder: {avg_age:.1f} år
    - Genomsnittlig längd: {avg_height:.1f} cm
    - Genomsnittlig vikt: {avg_weight:.1f} kg
    - Totalt antal loggade måltider: {total_meals}"""

if __name__ == "__main__":
    main()

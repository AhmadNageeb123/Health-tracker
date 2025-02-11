from firebase_config import db

# Funktion för att lägga till en användare
def add_user(user_id, name, age, height, weight):
    user_ref = db.collection("users").document(user_id)
    user_ref.set({
        "name": name,
        "age": age,
        "height": height,
        "weight": weight
    })
    print(f"✅ Användaren {name} har lagts till!")

# Funktion för att hämta en användares data
def get_user(user_id):
    user_ref = db.collection("users").document(user_id)
    doc = user_ref.get()
    if doc.exists:
        print(f"📄 Användardata: {doc.to_dict()}")
    else:
        print("❌ Användaren finns inte.")

# Funktion för att uppdatera en användares data
def update_user(user_id, field, value):
    user_ref = db.collection("users").document(user_id)
    user_ref.update({field: value})
    print(f"✅ {field} har uppdaterats till {value} för användare {user_id}!")

# Funktion för att ta bort en användare
def delete_user(user_id):
    user_ref = db.collection("users").document(user_id)
    user_ref.delete()
    print(f"❌ Användaren {user_id} har raderats!")

# Funktion för att logga en måltid för en användare
def log_meal(user_id, meal, calories):
    meal_ref = db.collection("users").document(user_id).collection("meals").document()
    meal_ref.set({
        "meal": meal,
        "calories": calories
    })
    print(f"🍽 Måltiden '{meal}' har lagts till för {user_id}!")

# Funktion för att hämta alla måltider för en användare
def get_meals(user_id):
    meals_ref = db.collection("users").document(user_id).collection("meals").stream()
    meals = [meal.to_dict() for meal in meals_ref]
    if meals:
        print(f"📄 Måltider för {user_id}: {meals}")
    else:
        print("❌ Inga måltider hittades.")

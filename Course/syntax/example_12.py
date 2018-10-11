
age = 12
male = "f"
location = "Russia"
locations = ["Russia", "Ukraine", "Belarus"]
is_programmer = True
is_admin = False

if (age >= 12
    and male == "f"
    and location in locations
    and (is_programmer or is_admin)):
    print("Доступ открыт")

if age >= 12 \
   and male == "m" \
   and location in locations \
   and (is_programmer or is_admin):
    print("Доступ открыт")

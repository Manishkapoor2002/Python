user_data = {}

def get_user_info():
    user_id = input("Enter User ID: ")
    user_name = input("Enter User Name: ")
    user_age = input("Enter User Age: ")

    user_data[user_id] = {
        "Name": user_name,
        "Age": user_age
    }

def print_user_details():
    search_id = input("Enter User ID to retrieve details: ")
    user_details = user_data.get(search_id)

    if user_details:
        print("\nUser Details:")
        print("User ID:", search_id)
        print("User Name:", user_details["Name"])
        print("User Age:", user_details["Age"])
    else:
        print("User ID not found.")


 
while True:
    n = int(input("For Entering Data Type 1 AND For Display Data Type 2 : "))

    if n == 1:
        get_user_info()
    elif n == 2:
        print_user_details()
    else:
        print("Invalid choice.")
    # print(user_data)



fruits = ["apple", "banana", "orange", "kiwi", "pear"]

def show_fruits(fruits):
    all_fruits = ", ".join(fruits)
    return all_fruits

print()

# Adding a new fruit
name_of_fruit = input("Enter the name of the fruit you want to add: ").strip().lower()
if name_of_fruit in fruits:
    print("This fruit is already in the list.")
else:
    fruits.append(name_of_fruit)
    print(f"The fruit '{name_of_fruit}' has been added to the list.")
    print(f"The list at the moment: {show_fruits(fruits)}")

print()

# Deleting a fruit by name
delete_fruit = input("Enter the name of the fruit you want to delete: ").strip().lower()
if delete_fruit in fruits:
    fruits.remove(delete_fruit)
    print(f"The fruit '{delete_fruit}' has been removed.")
    print(f"The list at the moment: {show_fruits(fruits)}")
else:
    print("That fruit is not in the list.")

print()

# Sorting fruits alphabetically
sorted_fruits = sorted(fruits)
print(f"List of fruits sorted alphabetically: {show_fruits(sorted_fruits)}")

# Listing fruits with names longer than 5 letters
print()
print("Fruits with names longer than 5 letters:")
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
if long_fruits:
    for fruit in long_fruits:
        print(f"- {fruit}")
else:
    print("There are no fruits with names longer than 5 letters.")










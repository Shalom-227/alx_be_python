#!/bin/python3

def display_menu():
	print("Shopping List Manager")
	print("1. Add Item")
	print("2. Remove Item")
	print("3. View List")
	print("4. Exit")

def main():
	shopping_list = []
	while True:
		display_menu()
		choice = input("Enter your choice: ")

		if choice == '1':
			new_item = input("Enter new item: ")
			shopping_list.append(new_item)
			pass
		elif choice == '2':
			item_removed = input("Enter item name to be removed: ")
			for item in shopping_list:
				if item_removed is not item:
					print("Item not found")
				break
			else:
				shopping_list.remove(item_removed)
				pass
		elif choice == '3':
			print(f"Shopping list: {shopping_list}")
			pass
		elif choice == '4':
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

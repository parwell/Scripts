# To Do List
# allows for displaying and editing of a to do list


class ToDoList(object):
    def __init__(self):
        print("Welcome to the To-Do List")		
        self.items = []
        self.update()
        self.display()

		
    def menu(self):
        while True:
            print("\nOptions:")
            print("0 - Display to do list")
            print("1 - Add items")
            print("2 - Delete an item")
            choice = input("Enter choice (enter to exit): ")
            if not choice:
                break
            elif choice == '0':
                self.display()
            elif choice == '1':
                self.addItems()
            elif choice == '2':
                self.deleteItem()
            else:
                print("Invalid input.")


    def display(self):
        if not self.items:
            print("List is empty.")
        else:
            print("\nItems:")
            for i, item in enumerate(self.items):
                print("\t{}: {}".format(str(i), item), end="")
                

    def update(self):
        with open("toDoList.txt", "r") as f:
            self.items = f.readlines()


    def addItems(self):
        things = []
        item = input("Enter item to add (enter to stop): ")
        while item:
            things.append(item)
            item = input("Enter item to add (enter to stop): ")
        if things:
            with open("toDoList.txt", "a") as f:
                for thing in things:
                    f.write(thing + "\n")
        self.update()


    def deleteItem(self):
        if not self.items:
            print("Nothing to delete.")
        else:
            self.display()
            index = input("Enter index of item to delete: ")
            try:
                index = int(index)
                with open("toDoList.txt", "r") as f:
                    content = f.readlines()
                    deleted = content.pop(index)[:-2]
                    print("Item \"{}\" deleted.".format(deleted))
                with open("ToDoList.txt", "w") as f:
                    for item in content:
                        f.write(item)
                self.update()
            except TypeError:
                print("ERROR :Input must be an integer.")
            except IndexError:
                print("ERROR: Index is out of range.")
            except ValueError:
                print("ERROR: No input.")
            except:
                print("ERROR: Unknown error.")


if __name__ == '__main__':
    lst = ToDoList()
    lst.menu()

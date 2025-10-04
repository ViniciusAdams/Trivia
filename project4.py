#Load existing items
#create a new item
#list items
#mark item as complete
#save items

def load_taks():
    pass

def save_taks():
    pass

def view_taks():
    pass

def create_task():
    pass

def mark_task_complete():
    pass

def main():
    tasks = load_taks()

    while True:
        print("\nTo-Do list Manager")
        print("1.View Task")
        print("2:Add task")
        print("3.Complete task")
        print("4.Exit")
        
        choice = input ("Enter your choice").strip()

        if choice == "1":
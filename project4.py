#Load existing items
#create a new item
#list items
#mark item as complete
#save items
import json

file_name = "todo_list.json"

def load_taks():
   try:
        with open(file_name, "r") as file:
            return json.load(file)
   except:
       return {"tasks":[]}
       
def save_taks(tasks):
    pass

def view_taks():
    try:
         with open(file_name, "w") as file:
            return json.load(file)
    except:
       return {"tasks":[]}
        

def create_task():
    pass

def mark_task_complete():
    pass

def main():
    tasks = load_taks()
    print(tasks)
    
    while True:
        print("\nTo-Do list Manager")
        print("1.View Task")
        print("2:Add task")
        print("3.Complete task")
        print("4.Exit")
        
        choice = input ("Enter your choice:").strip()

        if choice == "1":
            view_taks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            mark_task_complete() 
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid Choise, try again.")

main()
todo_list = []

while True:
    print("""What will you like to do: 
                                1. Create todo
                                2. Update todo
                                3. Delete todo
                                4. Print todo
                                5. Exit""")
    action = int(input(""))
    if action == 1:
      todo_input = input("Enter what you want to do: ")
      todo_time = input("Enter when you want to do it: ")
      todo_list.append({"todo_input": todo_input, "todo_time": todo_time, "isDone": False})
    elif action == 2:
      for index, todo in enumerate(todo_list):
          print(f"{index+1}. {todo_list[index]["todo_input"]} at {todo_list[index]["todo_time"]} is { "completed" if todo_list[index]["todo_time"] == True else "not completed"}")            
      update_index = int(input("Enter the position of todo to update: "))
      update_todo = input("Enter the new todo: ")
      update_todo_time = input("Enter the new todo time: ")
      update_todo_status = bool(input("Is it completed or not: True(Done)/False(Not done)"))
      
      todo_list[update_index - 1] = {"todo_input": update_todo, "todo_time": update_todo_time, "isDone": update_todo_status}
    elif action == 3:
        for index, todo in enumerate(todo_list):
          print(f"{index+1}. {todo_list[index]["todo_input"]} at {todo_list[index]["todo_time"]} is { "completed" if todo_list[index]["todo_time"] == True else "not completed"}")            
        delete_index = int(input("Enter the position of todo to delete: "))
        del todo_list[delete_index - 1]
    elif action == 4:
        print()
        print("Your Todos".center(20, "*"))
        for index, todo in enumerate(todo_list):
          print(f"{index+1}. {todo_list[index]["todo_input"]} at {todo_list[index]["todo_time"]} is { "completed" if todo_list[index]["todo_time"] == True else "not completed"}")            
    else:
        break
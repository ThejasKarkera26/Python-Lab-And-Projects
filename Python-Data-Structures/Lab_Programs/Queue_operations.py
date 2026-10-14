
queue = []

while True:
    print("\nQUEUE OPERATIONS \n1.Enqueue \n2.Dequeue \n3.Display \n4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to enqueue: ")
        queue.append(element)
        print(element, "inserted into queue")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            element = queue.pop(0)
            print("Deleted element:", element)

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", queue)
            
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

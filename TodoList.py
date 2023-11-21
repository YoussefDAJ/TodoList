todo = input("Enter your day tasks splited by comma: \n").split(",")

don_tasks = []
ongoing_tasks = []

for tasks in todo:
    done = input(f"\nDo you have done {tasks} ? Enter yes or no: \n").lower()
    if done == "yes":
        print("Well done!")
        don_tasks.append(tasks)
    else:
        print("Dont wait to long")
        ongoing_tasks.append(tasks)
    print("--------")
see_progress = input("Do you want to see your today's progress? (yes , no)").lower()
if see_progress == "yes":
    print(
        """
            *********** Done Tasks ***********
        """
    )
    print(don_tasks)
    print(
        """
            *********** Ongoing Tasks ***********
          """
    )
    print(ongoing_tasks)

else:
    print("Presse Enter to quite")

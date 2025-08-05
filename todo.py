To_do=[]
def save_task(To_do):
    with open("file.txt","w") as f:
        for i in To_do:
            f.write(i+ "\n")
def view(To_do):
    print("Here is your to do list of the day")
    for i in range(len(To_do)):
        print(To_do[i])
def task_add(To_do):
    tsk=input("Enter the task")
    To_do.append(tsk)
    print("Task added")
def task_remove(To_do):
    txt=input("Enter the task to be removed")
    for i in To_do:
        if txt==i:
            To_do.remove(txt)
    print("Task removed")            
while True:
    choice=int(input("Enter your choice(1-4) \n 1.view \n 2.To add \n 3.To remove \n 4.Exit"))
    if choice==4:
        print("Exited")
        break
    if choice==1:
        view(To_do)
        save_task(To_do)
    if choice==2:
        task_add(To_do)
        save_task(To_do)
    if choice==3:
        task_remove(To_do)
        save_task(To_do)
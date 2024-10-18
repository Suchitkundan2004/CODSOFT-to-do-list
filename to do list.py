import tkinter
import random


#creat root window
root = tkinter.Tk()

#change root window background color
root.configure(bg='white')

#change the title
root.title("My Super To Do List")

#change the window size
root.geometry("300x275")

#creat and empty list
tasks = []

#for testing purposes use a default list
#tasks =["Call mom", "Buy a guitar","Eat sushi"]



#creat functions

def update_listbox():
    #clear the current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0,"end")
 

def add_task():
    #Get tahe tasks to add
    task = txt_input.get()
    #make sure the task is not empty
    if task !="":
        #Append to the list
        tasks.append(task)
        #Update the listbox
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task."
    txt_input.delete(0, "end")


def del_all():
     #since we are changeing the list, it need to be globle
    global tasks
    #clear the tasks list
    tasks = []
    #update the listbox
    update_listbox()
     
def del_one():
    #Get the text of currently selected item
    task = lb_tasks.get("active")
    #Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox()    

def sort_asc():
    #sort the list
    tasks.sort()
    #update the listbox
    update_listbox()

def sort_desc():
    #sort the list
    tasks.sort()
    #Reverse the list
    tasks.reverse()
    #update the listbox
    update_listbox()

def choose_random():
    #choose a random task
    task = random.choice(tasks)
    #update the display label
    lbl_display["text"]=task

def show_number_of_tasks():
    #get the number of tasks
    number_of_tasks = len(tasks)

    msg = "Number of tasks: %s" %number_of_tasks
    #Dispaly the message
    lbl_display["tasks"]=msg


lbl_title = tkinter.Label(root, text="TO-DO-List", fg="white", bg="black")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="red")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="ADD Task", fg="white", bg="black", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="white", bg="black", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="white", bg="black", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="white", bg="black", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="Sort (desc)", fg="white", bg="black", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root, text="Choose Random", fg="white", bg="black", command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = tkinter.Button(root, text="Number of tasks", fg="white", bg="black", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="EXIT", fg="white", bg="black", command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root,fg="white",bg="black")
lb_tasks.grid(row=2,column=1,rowspan=7)



root.mainloop()
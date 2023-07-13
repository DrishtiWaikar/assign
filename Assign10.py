import tkinter as tk
import webbrowser as wb

obj = tk.Tk()

e = tk.Entry(obj, font=("Geogria",25), width=20)
e.grid(row=0,column=0)

l1 = tk.Label(obj, font=("Times in Roman",20))
l1.grid(row=1,column=0)

def navigate():
    search = e.get()
    print(search)
    if search:
        
        wb.open(f"https://www.youtube.com/{search}")
    else:
        print("Please enter something")

s_button = tk.Button(obj, text="Search", font=("Arial",20),command=navigate)
s_button.grid(row=4, column=0)

c_button = tk.Button(obj, text="Close", font=("Arial",20),command=obj.destroy)
c_button.grid(row=5,column=0)

obj.mainloop()
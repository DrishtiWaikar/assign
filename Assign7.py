def update_file(file="Info.txt"):
    try:
        f=open(file,"a") #Open file in append mode 
        #writing info to file 
        roll_number = "105"
        name = "Drishti"
        class_name = "CO B2"
        f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])

        f=open(file, "r") #reopening file in read mode
        print(f.readlines()) #read & print the info from the file 

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

        #Call the function 
        update_file()
#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution. 
#Student ID: w1956364 
#Date: 04/12/2022


import Part1_w1956364       #https://csatlas.com/python-import-file-module/
import Part2_w1956364

while True:
        print("")
        menu_input = input("Enter '1' to Open List with Text file: \n"
                           "Enter '2' to Open List with Dictionary: \n"
                           "Enter 'q' to Quit: ")
            
        if menu_input == "q":
            break
                    
        elif menu_input == "1":
            print("-" * 65)
            print("List with Text file\n")
            Part1_w1956364.menu_list()
            print("-" * 65)    
                    
        elif menu_input == "2":
            print("-" * 65)
            print("List with Dictionary\n")
            Part2_w1956364.menu_dictionary()
            print("-" * 65)
                
        else:
            print("Please Enter 1 or 2 or q")
                
print("'q' Pressed, Quit Programme")            

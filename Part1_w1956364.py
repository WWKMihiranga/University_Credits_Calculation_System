#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution. 
#Student ID: w1956364 
#Date: 04/12/2022 

def menu_list():

    total=0             #passes+defers+fails
    count1=0            #Progress count
    count2=0            #Progress(module trailer) count
    count3=0            #Module retriever count
    count4=0            #Exclude count
    total_count=0       #sum of 4 counts
    main_list=[]        #open a list

    text_file=open('new_file.text','w') #open a text file

    def file_inputs(): 
        text_file.write(f"{progression_outcome}-{passes},{defers},{fails}\n")
        
    answer='y'    
    while(answer=='y'):
        
        try:
            
            passes=int(input('Enter your total PASS credits: '))
            if passes==0 or passes==20 or passes==40 or passes==60 or passes==80 or passes==100 or passes==120:
                defers=int(input('Enter your total DEFER credits: '))
                if defers==0 or defers==20 or defers==40 or defers==60 or defers==80 or defers==100 or defers==120:
                    fails=int(input('Enter your total FAIL credits: '))
                    if fails==0 or fails==20 or fails==40 or fails==60 or fails==80 or fails==100 or fails==120:
                        
                        total=passes+defers+fails
                        if total==120:
                            
                            if fails>=80:
                                 progression_outcome='Exclude'                
                                 file_inputs()
                                 count4=count4+1
                                 
                            elif passes==120:
                                progression_outcome='Progress'
                                file_inputs()
                                count1=count1+1
                                
                            elif passes==100:           
                                progression_outcome='Progress(module trailer)'
                                file_inputs()
                                count2=count2+1
                                
                            elif passes<=80:
                                progression_outcome='Module retriever'
                                file_inputs()
                                count3=count3+1
                                
                            print(progression_outcome)

                            nested_list=[]    #open nested list
                            nested_list.insert(0,progression_outcome)
                            nested_list.insert(1,passes)
                            nested_list.insert(2,defers)
                            nested_list.insert(3,fails)
                            main_list.append(nested_list)
                            
                        else:
                            print('Total incorrect')
                    else:
                        print('Out of range')
                else:
                    print('Out of range')
            else:
                print('Out of range')        
        except:
            print('Integer required')
            
        while True:
            answer=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
            answer=answer.lower()
            print('')
            if answer=='y':
                break
            elif answer=='q':
                break
            else:
                print('Invalid Input.Try Again')
                continue
            
        if answer=='y':
            continue
        else:
            break
        
    text_file.close()

    print('-'*65)

    total_count=count1+count2+count3+count4
    print("Historigm")
    print("Progress",count1,' :','*'*count1)
    print("Trailer",count2,'  :','*'*count2)
    print("Retriever",count3,':','*'*count3)
    print("Excluded",count4,' :','*'*count4,'\n')
    print(total_count,"outcomes in total.")

    print('-'*65)

    for i in range(0,total_count):
        if main_list[i][0]=='Progress':
            print('Progress-',','.join(map(str,main_list[i][1:]))) 
            #https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
            
        if main_list[i][0]=='Progress(module trailer)':
            print('Progress(module trailer)-',','.join(map(str,main_list[i][1:])))

        if main_list[i][0]=='Module retriever':
            print('Module retriever-',','.join(map(str,main_list[i][1:])))

        if main_list[i][0]=='Exclude':
            print('Exclude-',','.join(map(str,main_list[i][1:])))

    print('')
    text_fileR=open('new_file.text','r')
    text_fileREAD=text_fileR.read()
    text_fileR.close()
    print(text_fileREAD)
         




                

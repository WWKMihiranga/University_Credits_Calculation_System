#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
#Any code taken from other sources is referenced within my code solution. 
#Student ID: w1956364 
#Date: 04/12/2022

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
                                 
                    elif passes==120:
                        progression_outcome='Progress'                                
                                
                    elif passes==100:           
                        progression_outcome='Progress(module trailer)'
                                
                    elif passes<=80:
                        progression_outcome='Module retriever'

                    print(progression_outcome)     
                        
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
            
        
                                

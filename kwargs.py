''' To pass an unspecified number of keyword(name) arguments. 

Python collects these arguments into a dictionary.'''


def show_profiles(**kwargs):
    for key,value in kwargs.items(): 
        
        ''' for key+value , when we call items - python give us pairing value. 
                                           since key and value both are in kwargs items , so we get key and value both once at a time.  '''
        print(key,"  :  " , value)


show_profiles(Name = "Elon " , Work = "New_For_Human_Civilization" , Age = "40" , )
show_profiles(Name = "Liger" , Work  = "Educator")
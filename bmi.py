def calculate_bmi (height,weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))

    bmi = weight / (height * height)

    print ("bmi = " + str(bmi))

    if bmi < 18.5:
        print ("Under Weight", -1) #-1 for lab3
        
    elif bmi > 25.0:
        print ("Over Weight", 0)# 0 for lab3
    else:
        print ("Normal Weight", 1) #1 for lab3
    

calculate_bmi(weight=57, height=1.73)
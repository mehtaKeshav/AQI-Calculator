# My name : Keshav Mehta, Student id: 026729168
# Teammate : Dhruv Gorasiya, Student id: 026737293
def print_index_level(elementname,concentrations,index):
    if elementname == "PM-2.5"  or elementname == "CO":
        print(f"    {elementname} concentration of {concentrations} is index level {index} ({index_quality(index)})")
    else:
        print(f"    {elementname} concentration of {int(concentrations)} is index level {index} ({index_quality(index)})")

def truncate_to_one_decimal(x):
    x = 10*x
    x = int(x)
    x = x/10
    return float(x)

def concentration_and_index(element_details):
    if element_details != 'O3 [ppb, 1-hr avg]' and  element_details != "O3 [ppb, 8-hr avg]":
        indexes = [[0,50],[51,100],[101,150],[151,200],[201,300],[301,500]]
    if element_details == "PM-2.5 [ug/m3, 24-hr avg]":
        concentrations = [[0,12.0],[12.1,35.4],[35.5,55.4],[55.5,150.4],[150.5,250.4],[250.5,500.4]] 
    elif element_details == "PM-10 [ug/m3, 24-hr avg]": 
        concentrations = [[0,54],[55,154],[155,254],[255,354],[355,424],[425,604]]  
    elif element_details == "NO-2 [ppb, 1-hr avg]":
        concentrations = [[0,53],[54,100],[101,360],[361,649],[650,1249],[1250,2049]]
    elif element_details == "SO-2 [ppb, 1-hr avg]":
        concentrations = [[0,35],[36,75],[76,185],[186,304],[305,604],[605,1004]]
    elif element_details == "CO [ppm, 8-hr avg]":
        concentrations = [[0,4.4],[4.5,9.4],[9.5,12.4],[12.5,15.4],[15.5,30.4],[30.5,50.4]]
    elif element_details == "O3 [ppb, 8-hr avg]":
        concentrations = [[0,54],[55,70],[71,85],[86,105],[106,200]]    
        indexes = [[0,50],[51,100],[101,150],[151,200],[201,300]]
    elif element_details == 'O3 [ppb, 1-hr avg]':
        concentrations = [[125,164],[165,204],[205,404],[405,604]]
        indexes = [[101,150],[151,200],[201,300],[301,500]]
    return concentrations, indexes

def calculate_index(measurement,concentrations,indexes):
    for i in range(len(indexes)):
        if concentrations[i][0] <= measurement <= concentrations[i][1]:
            clow = concentrations[i][0]
            chigh = concentrations[i][1]
            Ilow = indexes[i][0]
            Ihigh = indexes[i][1]
            index = ((Ihigh - Ilow)/(chigh - clow))*(measurement - clow) + Ilow
            return round(index)
    return -1 

def index_quality(index):
    if 0<= index <= 50:
        return 'Good'
    if 51<= index <= 100:
        return "Moderate"
    if 101<= index <= 150:
        return "Unhealthy for Sensitive Groups"
    if 151<= index <= 200:
        return "Unhealthy"
    if 201<= index <= 300:
        return "Very Unhealthy"
    if 301<= index <= 500:
        return "Hazardous"

if __name__ == "__main__":
    element_details = [['PM-2.5 [ug/m3, 24-hr avg]',"PM-2.5"],['PM-10 [ug/m3, 24-hr avg]',"PM-10"],['NO-2 [ppb, 1-hr avg]',"NO-2"],['SO-2 [ppb, 1-hr avg]',"SO-2"],['CO [ppm, 8-hr avg]',"CO"],['O3 [ppb, 8-hr avg]','O3'],['O3 [ppb, 1-hr avg]','O3']]
    total_number_of_indexes,sum_of_indexes = 0,0
    AQI = 0
    max_AQI_pollutant = None
    print("Air Quality Index Calculator")                                       
    name = str(input("What is the name of the location? "))                              
    for i in range(len(element_details)):
        if i == 0 or i == 4:
            measurement = truncate_to_one_decimal(float(input(f"\n -> Enter {element_details[i][0]}:")))
        else: 
            measurement = int(float(input(f"\n -> Enter {element_details[i][0]}:"))) 
        
        element_details[i].append(measurement)  #This statement add the input from the user to it's respective element details which is the sub list. This enables us to later use the value to print and comapare.
        concentrations, indexes = concentration_and_index(element_details[i][0])
        index = calculate_index(measurement,concentrations,indexes)
        element_details[i].append(index)
        if index >= -1:                         #The least value of index is taken -1 because of the special case of comparing inputs of O3 8hr and O3 1hr to ensure the correct output if the later index is -1.
            if index >= 0:                      #Since we include the -1 index value due to the reason explained above ,there would be a distortion in calculating average. So we exclude -1 by taking the least index value to be 0. 
                sum_of_indexes = sum_of_indexes + index
                total_number_of_indexes += 1
            if index > AQI:
                AQI = index
                max_AQI_polluatant = element_details[i][1]
            if element_details[i][0] == 'O3 [ppb, 8-hr avg]':
                continue
            if i == 6 and element_details[6][3] < element_details[5][3]:
                print_index_level(element_details[5][1],element_details[5][2],element_details[5][3])
            else:
                print_index_level(element_details[i][1],element_details[i][2],element_details[i][3])
    average = sum_of_indexes/total_number_of_indexes
    print(f"AQI for {name} is {AQI}"f"\nAir Quality: {index_quality(AQI)}")
    print('Summary:'f"\n\tPollutant with highest index level is {max_AQI_polluatant}"f"\n\tAverage index level is {truncate_to_one_decimal(average)}")

    

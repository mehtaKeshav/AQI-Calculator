def calc_I(arg):
    x = ((ihigh - ilow)/(chigh - clow))*(arg - clow) + ilow
    return x

loc = input("What is the name of this location?")

#calculation for pm25
pm25 = float(input(" ->Enter PM-2.5 [ug/m3, 24-hr avg]:"))
pm25=pm25*10
pm25=int(pm25)
pm25=pm25/10


if pm25 >=0 and pm25 <= 12.0:
    clow = 0
    chigh = 12.0
    ihigh = 50
    ilow = 0
    
elif pm25 >= 12.1 and pm25 <= 35.4:  
    clow = 12.1
    chigh = 35.4
    ihigh = 100
    ilow = 51

elif pm25 >= 35.5 and pm25 <= 55.4:
    clow = 35.5
    chigh = 55.4
    ihigh = 150
    ilow = 101
    
elif pm25 >= 55.5 and pm25 <= 150.4:
    clow = 55.5
    chigh = 150.4
    ihigh = 200
    ilow = 151
    
elif pm25 >= 150.5 and pm25 <= 250.4:
    clow = 150.5
    chigh = 250.4
    ihigh = 300
    ilow = 201
    
elif pm25 >= 250.5 and pm25 <= 500.4:
    clow = 250.5
    chigh = 500.4
    ihigh = 500
    ilow = 301
    
Ipm25 = int(calc_I(pm25))
print(f"    PM-2.5 concentration of {pm25} index level", int(Ipm25))
print()


#calculation for pm10
pm10 = int(input(" -> Enter PM-10 [ug/m3, 24-hr avg]:"))

if pm10 >= 0 and pm10 <= 54:
    clow = 0
    chigh = 54
    ihigh = 50
    ilow = 0
    
elif pm10 > 54 and pm10 <= 154:
    clow = 55
    chigh = 154
    ihigh = 100
    ilow = 51
    
elif pm10 > 154 and pm10 <= 254:
    clow = 155
    chigh = 254
    ihigh = 150
    ilow = 101
    
elif pm10 > 254 and pm10 <= 354:
    clow = 255
    chigh = 354
    ihigh = 200
    ilow = 151
    
elif pm10 > 354 and pm10 <= 424:
    clow = 355
    chigh = 424
    ihigh = 300
    ilow = 201
    
elif pm10 > 424 and pm10 <= 604:
    clow = 425
    chigh = 604
    ihigh = 500
    ilow = 301

Ipm10 = int(calc_I(pm10))
print(f"    PM-2.5 concentration of {pm10} index level", int(Ipm10))
print()

#calculation for no2
no2 = float(input("-> Enter NO-2 [ppb, 1-hr avg]:"))
no2 = int(no2)
if no2>= 0 and no2 <= 53:
    clow = 0
    chigh = 53
    ihigh = 50
    ilow = 0
    
elif no2 > 53 and no2 <= 100:
    clow = 54
    chigh = 100
    ihigh = 100
    ilow = 51
    
elif no2 > 100 and no2 <= 360:
    clow = 101
    chigh = 360
    ihigh = 100
    ilow = 51
    
elif no2 > 360 and no2 <= 649:
    clow = 361
    chigh = 649
    ihigh = 100
    ilow = 51
    
elif no2 > 649 and no2 <= 1249:
    clow = 650
    chigh = 1249
    ihigh = 100
    ilow = 51
    
elif no2 > 1249 and no2 <= 2049:
    clow = 1250
    chigh = 2049
    ihigh = 100
    ilow = 51
Ino2 = int(calc_I(no2))
print(f"    N0-2 concentration of {no2} index level", int(Ino2))
print()
if Ipm25 > Ipm10:
    maximum = Ipm25
else:
    maximum = Ipm10
if maximum > Ino2:
    AIQ = maximum
else:
    AIQ = Ino2

if AIQ >= 0 and AIQ <= 50:
    condition = "Good"
elif AIQ > 50 and AIQ <= 100:
    condition = "Moderate"
elif AIQ > 100 and AIQ <= 150:
    condition = "Unhealthy forSensitive Groups"
elif AIQ > 150 and AIQ <= 200:
    condition = "Unhealthy"
elif AIQ > 200 and AIQ <= 300:
    condition = "Very Unhealthy"
elif AIQ > 300 and AIQ <= 500:
    condition = "Hazardous"
print(f"AQI for {loc} is {AIQ}")
print("Air Quality:", condition)
                

def calc_I(cp):
    I = ((ihigh - ilow)/(chigh - clow))*(cp - clow) + ilow
    return I
def truncate(x):
    x = int(x)
    x = x/10
    return x


#The value of the maximum is subject to change with the progression of the code
#hence the maximum value is checked after every index calculation
AQI = 0
h_index = 0


loc = str(input("Air Quality Index Calculator\n\nWhat is the name of the location?"))


pm25 = float(input("\n -> Enter PM-2.5 [ug/m3, 24-hr avg]:"))



truncate(pm25)
if pm25>=0:
    valid_pm25 = True
else:
    valid_pm25 = False
if valid_pm25 == True:
    if pm25 >=0 and pm25 <= 12.0:
        clow = 0
        chigh = 12.0
        ihigh = 50
        ilow = 0
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    elif pm25 >= 12.1 and pm25 <= 35.4:
        clow = 12.1
        chigh = 35.4
        ihigh = 100
        ilow = 51
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    elif pm25 >= 35.5 and pm25 <= 55.4:
        clow = 35.5
        chigh = 55.4
        ihigh = 150
        ilow = 101
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    elif pm25 >= 55.5 and pm25 <= 150.4:
        clow = 55.5
        chigh = 150.4
        ihigh = 200
        ilow = 151
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    elif pm25 >= 150.5 and pm25 <= 250.4:
        clow = 150.5
        chigh = 250.4
        ihigh = 300
        ilow = 201
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    elif pm25 >= 250.5 and pm25 <= 500.4:
        clow = 250.5
        chigh = 500.4
        ihigh = 500
        ilow = 301
        Ipm25 = round(calc_I(pm25))
        AQI = Ipm25
        h_index = "PM-2.5"

    print(f"    PM-2.5 concentration of {pm25} is index level", int(Ipm25))








pm10 = float(input("\n -> Enter PM-10 [ug/m3, 24-hr avg]:"))
pm10 = int(pm10)
if pm10>=0:
    valid_pm10 = True
else:
    valid_pm10 = False
if valid_pm10 == True:
    if pm10 >= 0 and pm10 <= 54:
        clow = 0
        chigh = 54
        ihigh = 50
        ilow = 0
        Ipm10 = round(calc_I(pm10))

    elif pm10 > 54 and pm10 <= 154:
        clow = 55
        chigh = 154
        ihigh = 100
        ilow = 51
        Ipm10 = round(calc_I(pm10))

    elif pm10 > 154 and pm10 <= 254:
        clow = 155
        chigh = 254
        ihigh = 150
        ilow = 101
        Ipm10 = round(calc_I(pm10))

    elif pm10 > 254 and pm10 <= 354:
        clow = 255
        chigh = 354
        ihigh = 200
        ilow = 151
        Ipm10 = round(calc_I(pm10))

    elif pm10 > 354 and pm10 <= 424:
        clow = 355
        chigh = 424
        ihigh = 300
        ilow = 201
        Ipm10 = round(calc_I(pm10))
    elif pm10 > 424 and pm10 <= 604:
        clow = 425
        chigh = 604
        ihigh = 500
        ilow = 301
        Ipm10 = round(calc_I(pm10))
    if Ipm10 > AQI:
        AQI = Ipm10
        h_index = "PM-10"

    print(f"    PM-10 concentration of {pm10} is index level", int(Ipm10))

#calculation for no2
no2 = float(input("\n -> Enter NO-2 [ppb, 1-hr avg]:"))
no2 = int(no2)
if no2>=0:
    valid_no2 = True
else:
    valid_no2 = False
if valid_no2 == True:
    if no2>= 0 and no2 <= 53:
        clow = 0
        chigh = 53
        ihigh = 50
        ilow = 0
        Ino2 = round(calc_I(no2))

    elif no2 > 53 and no2 <= 100:
        clow = 54
        chigh = 100
        ihigh = 100
        ilow = 51
        Ino2 = round(calc_I(no2))

    elif no2 > 100 and no2 <= 360:
        clow = 101
        chigh = 360
        ihigh = 150
        ilow = 101
        Ino2 = round(calc_I(no2))

    elif no2 > 360 and no2 <= 649:
        clow = 361
        chigh = 649
        ihigh = 200
        ilow = 151
        Ino2 = round(calc_I(no2))

    elif no2 > 649 and no2 <= 1249:
        clow = 650
        chigh = 1249
        ihigh = 300
        ilow = 201
        Ino2 = round(calc_I(no2))

    elif no2 > 1249 and no2 <= 2049:
        clow = 1250
        chigh = 2049
        ihigh = 500
        ilow = 301
        Ino2 = round(calc_I(no2))

    if Ino2 > AQI:
        AQI = Ino2
        h_index = "NO-2"
    print(f"    NO-2 concentration of {no2} is index level", int(Ino2))









so2 = int(input("\n -> Enter SO-2 [ppb, 1-hr avg]:"))
if so2 >=0:
    valid_so2 = True
else:
    valid_so2 = False


if valid_so2 == True:
    if so2>= 0 and so2 <= 35:
        clow = 0
        chigh = 35
        ihigh = 50
        ilow = 0
        Iso2 = round(calc_I(so2))

    elif so2 > 35 and so2 <= 75:
        clow = 36
        chigh = 75
        ihigh = 100
        ilow = 51
        Iso2 = round(calc_I(so2))

    elif so2 > 75 and so2 <= 185:
        clow = 76
        chigh = 185
        ihigh = 150
        ilow = 101
        Iso2 = round(calc_I(so2))

    elif so2 > 185 and so2 <= 304:
        clow = 186
        chigh = 304
        ihigh = 200
        ilow = 151
        Iso2 = round(calc_I(so2))

    elif so2 > 304 and so2 <= 604:
        clow = 305
        chigh = 604
        ihigh = 300
        ilow = 201
        Iso2 = round(calc_I(so2))

    elif so2 >604 and so2 <=1004:
        clow = 605
        chigh = 1004
        ihigh = 500
        ilow = 301
        Iso2 = round(calc_I(so2))
    if Iso2 > AQI:
        AQI = Iso2
        h_index = "SO-2"
    print(f"    SO-2 concentration of {so2} is index level {Iso2}")





co = float(input("\n -> Enter CO [ppm, 8-hr avg]:"))
if co >= 0 and co <= 50.4:
    valid_co = True
else:
    valid_co = False

truncate(co)

if valid_co == True:
    if co>= 0 and co <= 4.4:
        clow = 0
        chigh = 4.4
        ihigh = 50
        ilow = 0
        Ico = round(calc_I(co))

    elif co > 4.4 and co <= 9.4:
        clow = 4.5
        chigh = 9.4
        ihigh = 100
        ilow = 51
        Ico = round(calc_I(co))

    elif co > 9.4 and co <= 12.4:
        clow = 9.5
        chigh = 12.4
        ihigh = 150
        ilow = 101
        Ico = round(calc_I(co))

    elif co > 12.4 and co <= 15.4:
        clow = 12.5
        chigh = 15.4
        ihigh = 200
        ilow = 151
        Ico = round(calc_I(co))

    elif co > 15.4 and co <= 30.4:
        clow = 15.5
        chigh = 30.4
        ihigh = 300
        ilow = 201
        Ico = round(calc_I(co))

    elif co > 30.4 and co <= 50.4:
        clow = 30.5
        chigh = 50.4
        ihigh = 500
        ilow = 301
        Ico = round(calc_I(co))

    if Ico > AQI:
        AQI = Ico
        h_index = "CO"
    print(f"    CO concentration of {co} is index level {Ico}")

o3_8hr = float(input('\n -> Enter O3 [ppb, 8-hr avg]:'))
o3_1hr = float(input(' -> Enter O3 [ppb, 1-hr avg]:'))

if o3_8hr >= 0 and o3_8hr <= 200:
    valid_o3_8hr = True
else:
    valid_o3_8hr = False
o3_8hr = int(o3_8hr)
o3_1hr = int(o3_1hr)


if valid_o3_8hr == True:
    if o3_8hr >= 0 and o3_8hr <= 54:
        clow = 0
        chigh = 54
        ihigh = 50
        ilow = 0
        Io3_8hr = round(calc_I(o3_8hr))

    elif o3_8hr > 54 and o3_8hr <= 70:
        clow = 55
        chigh = 70
        ihigh = 100
        ilow = 51
        Io3_8hr = round(calc_I(o3_8hr))

    elif o3_8hr > 70 and o3_8hr <= 85:
        clow = 71
        chigh = 85
        ihigh = 150
        ilow = 101
        Io3_8hr = round(calc_I(o3_8hr))

    elif o3_8hr > 85 and o3_8hr <= 105:
        clow = 86
        chigh = 105
        ihigh = 200
        ilow = 151
        Io3_8hr = round(calc_I(o3_8hr))

    elif o3_8hr > 105 and o3_8hr <= 200:
        clow = 106
        chigh = 200
        ihigh = 300
        ilow = 201
        Io3_8hr = round(calc_I(o3_8hr))

if o3_1hr >= 125 and o3_1hr <=604:
    valid_o3_1hr = True
else:
    valid_o3_1hr = False

if valid_o3_1hr == True:

    if o3_1hr > 125 and o3_1hr <= 164:
        clow = 125
        chigh = 164
        ihigh = 150
        ilow = 101
        Io3_1hr = round(calc_I(o3_1hr))

    elif o3_1hr > 164 and o3_1hr <= 204:
        clow = 164
        chigh = 204
        ihigh = 200
        ilow = 151
        Io3_1hr = round(calc_I(o3_1hr))

    elif o3_1hr > 204 and o3_1hr <= 404:
        clow = 205
        chigh = 404
        ihigh = 300
        ilow = 201
        Io3_1hr = round(calc_I(o3_1hr))

    elif o3_1hr > 404 and o3_1hr <= 604:
        clow = 405
        chigh = 604
        ihigh = 300
        ilow = 201
        Io3_1hr = round(calc_I(o3_1hr))
else:
    No_Io3_1hr = True

#maximum function cannot be used when there is a posibility of absence of either of the O3 Indices.
#no comparison can be made when one or both are absent.
#if the input is valid index will be calculated and hence grater of the two will be assigned to Index of O3.
if valid_o3_8hr == False and valid_o3_1hr == True:
    Io3 = Io3_1hr
    o3 = o3_1hr

if valid_o3_8hr == True and valid_o3_1hr == False:
    Io3 = Io3_8hr
    o3 = o3_8hr

if valid_o3_8hr == True and valid_o3_1hr == True:
    Io3 = max(Io3_8hr,Io3_1hr)
    if Io3 == Io3_8hr:
        o3 = o3_8hr
    else:
        o3 = o3_1hr




if valid_o3_8hr == True or valid_o3_1hr == True:
    if Io3 > AQI:
        AQI = Io3
        h_index = "O3"
    print(f"    O3 concentration of {o3} is index level {Io3}")



if AQI >= 0 and AQI <= 50:
    condition = "Good"
elif AQI > 50 and AQI<= 100:
    condition = "Moderate"
elif AQI > 100 and AQI <= 150:
    condition = "Unhealthy forSensitive Groups"
elif AQI > 150 and AQI <= 200:
    condition = "Unhealthy"
elif AQI > 200 and AQI <= 300:
    condition = "Very Unhealthy"
elif AQI > 300 and AQI <= 500:
    condition = "Hazardous"

#correct average can only be calculated when the input entered is valid i.e.
#a non negative input. Hence only the positive and valid inputs should be used to calculate average
#valid input gives a valid index and a valid index contributes to average calculation
add = 0
count = 0
if valid_pm25 == True:
    add += Ipm25
    print(add)
    count += 1
if valid_pm10 == True:
    add += Ipm10
    print(add)
    count += 1
if valid_no2 == True:
    add += Ino2
    print(add)
    count += 1
if valid_so2 == True:
    add += Iso2
    print(add)
    count += 1
if valid_co == True:
    add += Ico
    print(add)
    count += 1
if valid_o3_8hr == True:
    add += Io3_8hr
    print(add)
    count += 1
if valid_o3_1hr == True:
    add += Io3_1hr
    print(add)
    count +=1
avg = add/count


print(f"\nAQI for {loc} is {AQI}"
    "\nAir Quality:", condition,
    "\n\nSummary:"
    "\n    Pollutant with highest index level is", h_index,
    f'\n    Average index level is {avg:.1f}')
print(add)
print(count)





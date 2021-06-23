import Main.py
car_dictionary = {"-------------------------------------------------------------","Weather Stats for - {}  || {}".format(location.upper(), date_time),
"-------------------------------------------------------------","Current temperature is: {:.2f} deg C".format(temp_city),
"Current weather desc  :",weather_desc,"Current Humidity      :",hmdt, '%',"Current wind speed    :",wind_spd ,'kmph',}

file = open("car.txt", "w")
for i in range(0,8,1):{
file.write(repr(car_dictionary))
}
file.close()
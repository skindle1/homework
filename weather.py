def main():
  import json, requests
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "80f86c4ebd9a87a7228dd599a019992b"  
  city = input ("Please input city or zipcode: ")
  url = f"{base_url}?q={city}&units=imperial&APPID={appid}" 
  print (url)
  print()
          
  response = requests.get(url)
  #checks the status of the connection
  print(f"status code:{response.status_code}")
  if response.status_code==200:
    print("Connection was successful.")
  else:
    print(f"I'm sorry. there's a {response.status_code} error with the connection.")
  unformated_data = response.json()
  #checks to make sure the city input is valid
  if unformated_data["cod"] !="404":
        
    #print(unformated_data)
  
  #This is the weather information for the data
  
    humidity = unformated_data["main"]["humidity"]    
    wind = unformated_data["wind"]["speed"]
    temp = unformated_data["main"]["temp"]  
    temp_max = unformated_data["main"]["temp_max"]





#This is where the weather is printed for the city
    print(f"The weather for {city} is: \nTemp: {temp}, \nHumidity level: {humidity}%,\nWind speed: {wind}\n")
    restart = input("Would you like to try another city?\n 1 for yes 2 for no: ")
    restart = int(restart)
    if restart == 1:
     main()
    else:
      print ("Thanks for checking the weather.")
    #this is the line that shows the error if the city is not found.
  #it goes with the if statement in line 17
  else:
    print("That city is not found.")
    main()

main()

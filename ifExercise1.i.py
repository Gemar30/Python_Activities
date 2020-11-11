india= ["mumbai","banglore", "chennai","delhi"]
pakistan= ["lahore","karachi","islamabad"]
bangladesh= ["dhaka","khulna","rangpur"]

cityName=input("Enter a city name: ")

if cityName in india:
    print("City Name is India")

elif cityName in pakistan:
    print("City name is Pakistan")

elif cityName in bangladesh:
    print("City name is Bangladesh")

else:
    print("The city name is unknown")


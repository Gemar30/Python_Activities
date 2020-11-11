india= ["mumbai","banglore", "chennai","delhi"]
pakistan= ["lahore","karachi","islamabad"]
bangladesh= ["dhaka","khulna","rangpur"]

cityName1=input("Enter first city name: ")
cityName2=input("Enter second city name: ")

if cityName1 in india and cityName2 in india:
    print("Both cities are in india")

elif cityName1 in pakistan and cityName2 in pakistan:
    print("Both cities are in pakistan")

elif cityName1 in bangladesh and cityName2 in bangladesh:
    print("Both cities are in bangladesh")

else:
    print("They dont belong to same country")


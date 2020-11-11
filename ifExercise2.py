sugar=input("Please enter your fasting sugar level: ")
sugar=float(sugar)

if sugar<80:
    print("Your sugar is low")

elif sugar >100:
    print("Your sugar is high")

else:
    print("Your sugar is normal")
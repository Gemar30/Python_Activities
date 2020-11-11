indian=["samosa","daal","naan"]
chinese=["egg role","pt sticker", "fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name: ")

if dish in indian:
    print("indian")

elif dish in chinese:
    print("chinese")

elif dish in italian:
    print("italian")

else:
    print("Based in little knowledge i dont know which cuisine is", dish)



for i in range(5):
    print(f"You ran {i+1} miles")
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

    if i == 4:
        print ("Hurray! You are  a rock star! You just finished 5 km race!")

    else:
        print(f"You didnt finish 5 km race  but hey congrats  anyways! You still you can ran {i+1} miles")
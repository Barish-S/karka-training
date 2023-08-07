total_mark=int(input("Enter The Mark : "))
if total_mark>92:
    print("Your Elegible For MBBS")
elif total_mark>85 and total_mark<=92:
    print("You Are Elegible For BDS")
elif total_mark>75 or total_mark<=85:
    print("Your Elegible For Agriculture")
else:
    print("Yor Are Elegible Engineer")
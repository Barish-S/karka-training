token=int(input("Enter The Amount : "))
if token>500 and token<=1000:
    print("You Hvae Owned a Silver Token")
elif token>1000 and token<5000:
    print("You Have Owned A Golden Token")
elif token>=5000:
    print("You Have Owned a Platinum Token")
else:
    print("No Token Available")
maths=int(input("Enter Maths Mark : "))
physics=int(input("Enter Physics Mark : "))
chemistry=int(input("Enter Chemistry Mark : "))
total=maths+physics+chemistry
ave=maths+physics
if (maths>=65 and physics>=55 and chemistry>=50) and (total>=190 or ave>=140):
        print("Your Eligeble")
else:
      print("Your Not Eligeble")
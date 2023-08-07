unit=int(input("Enter The Unit :"))
cost=int(input("Cost Per Unit : "))
if unit>=100 and unit<500:
    mul=cost*unit
    char=mul+50
    gst=char*.18
    total=char+gst
    print("Current Bill Is Rs.",total)
elif unit>=500 and unit<=1000:
      mul=cost*unit
      char=mul*.05
      mchar=mul+char
      gst=mchar*.18
      total=mchar+gst
      print("Current Bill Is Rs.",total)
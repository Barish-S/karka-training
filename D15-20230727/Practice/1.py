#Calculate GST on Gold

def cal_gst(amount):
    return amount*.03

gold_rate = 10000

making_charge = 1000

gst = cal_gst(gold_rate+making_charge)
v= cal_gst(1000)
total = gold_rate + making_charge + gst

print(total)
print("fds",v)
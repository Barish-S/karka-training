monthly_gold_rate=[{"month":"jan",
                    "gold_rate":2000,
                    "jewel_list":[{"name":"chain",
                                   "making_charge":12},
                                   {"name":"chain",
                                   "making_charge":11},
                                   {"name":"bangal",
                                    "making_charge":15}]},
                    {"month":"feb",
                    "gold_rate":1500,
                    "jewel_list":[{"name":"chain",
                                   "making_charge":12},
                                   {"name":"chain",
                                   "making_charge":11},
                                   {"name":"bangal",
                                    "making_charge":15}]},
                    {"month":"mar",
                    "gold_rate":1400,
                    "jewel_list":[{"name":"chain",
                                   "making_charge":12},
                                   {"name":"chain",
                                   "making_charge":11},
                                   {"name":"bangal",
                                    "making_charge":15}]},
                    {"month":"apr",
                    "gold_rate":2400,
                    "jewel_list":[{"name":"chain",
                                   "making_charge":12},
                                   {"name":"chain",
                                   "making_charge":11},
                                   {"name":"bangal",
                                    "making_charge":15}]},
                    {"month":"may",
                    "gold_rate":800,
                    "jewel_list":[{"name":"chain",
                                   "making_charge":12},
                                   {"name":"chain",
                                   "making_charge":11},
                                   {"name":"bangal",
                                    "making_charge":15}]}]
min_value=monthly_gold_rate[0]["gold_rate"]
max_value=0
for r in monthly_gold_rate:
    if r["gold_rate"]<=min_value:
        min_month=r["month"]
        min_value=r["gold_rate"]
    elif r["gold_rate"]>=max_value:
        max_month=r["month"]
        max_value=r["gold_rate"]
print("The Gold Is Cheaper",min_value,"In",min_month)
print("The Gold Is higher",max_value,"In",max_month)

for item in  monthly_gold_rate:
    print( "Gold rate is " + str(item["gold_rate"]),"In "+ str(item["month"]))
    jewls_list = item["jewel_list"]
    
    for j in jewls_list:
                        # 2000 * 13 / 100
        cal_mak_charge = item["gold_rate"] * j['making_charge'] / 100
        final_charge = item["gold_rate"] + cal_mak_charge
        print( j['name'] + " rate is "+ str(final_charge))
     
          
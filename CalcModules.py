#calculcate your current amount of coins including coins on open orders
def calc_current_amt(list):
    total = 0
    for x in range(len(list)):
        if list[x]['side'] == 'buy':
            #print("Bought amount {}".format(list[x]['size']))
            total += float(list[x]['size'])
        elif list[x]['side'] == 'sell':
            #print("Sold amoutn {}".format(list[x]['size']))
            total -= float(list[x]['size'])
    #print("Current Total of coin: {}".format(total))
    return total


#calculate total fees incurred
def calc_fees(list):
    fees = 0
    for x in range(len(list)):
        fees += float(list[x]['fee'])
    print("Total amount of fees: ${}".format(fees))
    return fees

def get_current_price(list):
    current_price = list['price']
    return current_price

#calculate Cost Average Unit Cost
#coin units x cost per unit = total cost    [Total cost/Total Units]
def calc_avg_cost(list, ticker):
    totalcost = 0
    for x in range(len(list)):
        if list[x]['side'] == 'buy':
            totalcost += float(list[x]['usd_volume'])
            #averageCost = totalcost/(calc_current_amt(list))
        elif list[x]['side'] == 'sell':
            totalcost -= float(list[x]['usd_volume'])
        averageCost = totalcost / (calc_current_amt(list))
    print("Total amount of coin units is: {}".format(calc_current_amt(list)))
    print("Total amount spent on this crypto ${}".format(totalcost))
    print("Average cost per unit is: ${}".format(averageCost))
    PL = (float(get_current_price(ticker))-float(averageCost))*(calc_current_amt(list))
    print("Profit/Loss: {} ".format(PL))
    print("-----------------------------------------------------------------")

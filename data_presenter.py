opened = open("CupcakeInvoices.csv")
total = 0
for line in opened:
    line = line.rstrip('\n').split(',')
    line[3] = int(line[3])
    line[4] = float(line[4])
    line.append(line[3]*line[4])
    line[5] = "{:.2f}".format(line[5])
    customer_total = float(line[5])
    total += customer_total
print("the total is", "{:.2f}".format(total))
opened.close()




integer = 6
string = F"{integer} is an integer"
print(string)
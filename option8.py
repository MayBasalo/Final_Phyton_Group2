def run():
    # We take the user input
    invNum = input("Please enter the 3 digits ID of the expense you would like a report on: ") 
    # Data obtained from accessing expense records
    driverNum = ''
    invDate = ''
    itemID = []
    numItem = []
    totItemCost = []
    subTotal = []
    formattedSubTotal = []
    hst = []
    invTotal = []

    # We access the expense records, store all pertinent information, and then close the file
    expenseFile = open("DataFiles/ExpenseRecords.dat", 'r')
    for line in expenseFile:
        record = line.split(",")
        # print(record[0]+" "+invNum)
        if record[0] == invNum:
            driverNum = record[1].strip()
            itemID.append(record[2].strip())
            invDate = record[3].strip()
            numItem.append(record[4].strip())
            totItemCost.append(float(record[5]))
            subTotal.append(float(record[6]))
            formattedSubTotal.append(f"${float(record[6]):,.2f}")
            hst.append(float(record[7]))
            invTotal.append(float(record[8]))
    expenseFile.close()
    # if no record found, end execution
    if(driverNum == ''):
        print("No Invoice with ID of "+ invNum +" can be found.")
        return
    # else, we continue
    else:
        # Information to be retreived by looking up itemId on Pats Inventory
        itemDesc = [None] * len(itemID)

        # We compare primary keys until we get a hit. 
        # We then save the result and continue for looking for the rest of the parts.
        for index in range(len(itemID)):
            partsFile = open("DataFiles/PartsInventory.dat", "r")
            for line in partsFile:
                record = line.split(",")
                if itemID[index] == record[0]:
                    itemDesc[index] = record[1].strip()
                    partsFile.close()
                    break
        # With all the information on hand, we can start to generate the report
        print(f"")
        print(f"               HAB TAXI SERVICES")
        print(f"               INVOICE BREAKDOWN")
        print(f"===============================================")
        print(f"Invoice Date: {invDate}")
        print(f"Invoice ID: {invNum}                 Driver ID: {driverNum}")
        print(f"===============================================")
        sumHST = 0
        sumInvTotal = 0
        sumSubTotal = 0
        # I calculate the sum of each total and display it in a formatted manner
        for index in range(len(itemID)):
            print(f"{itemDesc[index] + ' X ' + numItem[index]:35s} {formattedSubTotal[index]:>11s}")
            sumInvTotal += invTotal[index]
            sumHST += hst[index]
            sumSubTotal += subTotal[index]
        # I format some final values, then print the final part of the report
        formattedSumHST = f"${sumHST:,.2f}"
        formattedSumInvTotal = f"${sumInvTotal:,.2f}"
        formattedSumSubTotal = f"${sumSubTotal:,.2f}"
        print(f"-----------------------------------------------")
        print(f"SubTotal                           {formattedSumSubTotal:>12s}")
        print(f"HST                                 {formattedSumHST:>11s}")
        print(f"-----------------------------------------------")
        print(f"Total Expenditure:                 {formattedSumInvTotal:>12s}")
        print(f"===============================================")
        print("")
        print("")
        # I prompt the user to continue
        input("Press the Enter Key to Continue...")
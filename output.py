

def asCSV(accounts, transactions):
    outputDict = {}
    for a in accounts['data']['accounts']:
        name = a['name']
        outputDict[name] = {}

    for transaction in transactions['data']['transactions']:
        aID = transaction['account_id']
        tID = transaction['id']
        account = transaction['account_name']
        print(account)
        outputDict[account][tID] = {}
        outputDict[account][tID]['date'] = transaction['date']
        outputDict[account][tID]['payee'] = transaction['payee_name']
        outputDict[account][tID]['category'] = transaction['category_name']
        if float(transaction['amount']) > 0:
            outputDict[account][tID]['outflow'] = '0'
            outputDict[account][tID]['inflow'] = transaction['amount']
        else:
            outputDict[account][tID]['outflow'] = transaction['amount']
            outputDict[account][tID]['inflow'] = '0'
    #This return won't be here in the when this is completed. This is just to check current progress
    return outputDict

import requests
import api as ynab
import output
import pprint

def main():
    apiKey = raw_input('Please enter your API key: ')
    budgetID = raw_input('Please enter the budget ID: ')
    print('Fetching accounts')
    accounts = ynab.get_accounts(apiKey, budgetID)
    print('Found the following accounts:')
    for a in accounts['data']['accounts']:
        print(a['name'])
    transactions = ynab.get_transactions(apiKey, budgetID)
    pprint.pprint(output.asCSV(accounts, transactions))

if __name__ == '__main__':
    main()

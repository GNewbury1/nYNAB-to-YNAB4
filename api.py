import requests
import json

def get_accounts(apiKey, budgetID):
    headers = {'Authorization': 'Bearer {}'.format(apiKey)}
    response = requests.get('https://api.youneedabudget.com/v1/budgets/{}/accounts'.format(budgetID), headers=headers)
    return json.loads(response.text)

def get_transactions(apiKey, budgetID):
    headers = {'Authorization': 'Bearer {}'.format(apiKey)}
    response = requests.get('https://api.youneedabudget.com/v1/budgets/{}/transactions'.format(budgetID), headers=headers)
    return json.loads(response.text)

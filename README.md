# nYNAB-to-YNAB4

***This project is still in development, and does not yet output any .csv files***

This project aims to do one thing: export all nYNAB transaction data into one CSV file per account. This should allow for easy importing to YNAB4, provided the user has corresponding accounts set up in YNAB4.

## How to use:
Run `main.py` with `python main.py`
Input your API token/key/whatever you want to call it
Input your budget ID

Once this script is completed, you should find a CSV file per account in nYNAB. This can then be directly imported into a corresponding account on YNAB4

## To-do
- [x] Fetch accounts
- [x] Fetch transaction
- [x] Match transactions with accounts
- [x] Put data into dictionary for easy output to CSV
- [ ] Actually output to CSV

import csv
from eth_account import Account
Account.enable_unaudited_hdwallet_features()

def write_new_wallets_to_csv(wallet_data, csv_filename):
    filename = csv_filename + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["WALLET", "PRIVATE KEY", "SEED PHRASE"])

        for private_key, mnemonic in wallet_data:
            address = Account.from_key(private_key).address
            csv_writer.writerow([address, private_key.hex(), mnemonic])
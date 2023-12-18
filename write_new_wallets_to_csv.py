import csv
from eth_account import Account
Account.enable_unaudited_hdwallet_features()
import csv

def write_new_wallets_to_csv(wallet_data, csv_filename):
    """
    Write wallet data to a CSV file.

    Args:
        wallet_data (list): A list of tuples containing private keys and mnemonic phrases.
        csv_filename (str): The name of the CSV file to be created.

    Returns:
        None
    """
    filename = csv_filename + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["WALLET", "PRIVATE KEY", "SEED PHRASE"])

        for private_key, mnemonic in wallet_data:
            address = Account.from_key(private_key).address
            csv_writer.writerow([address, private_key.hex(), mnemonic])
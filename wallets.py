import datetime
from write_new_wallets_to_csv import write_new_wallets_to_csv
from ask_inputs import create_ask_input_init, create_ask_input
from generate_loop import generate_loop
from custom_logger import custom_logger, test_logger

def init_wallets():
    # Initiate the script
    dateNow = datetime.datetime.now()
    print("Script started at: " + str(dateNow))
    num_wallets = create_ask_input_init("How many wallets to generate: ")
    filename = create_ask_input("Enter the file name: ")
    wallet_data = generate_loop(num_wallets)
    write_new_wallets_to_csv(wallet_data, filename)
    print(f"{num_wallets} wallets generated and saved to {filename}.csv")

if __name__ == "__main__":
    init_wallets()
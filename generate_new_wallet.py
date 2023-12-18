from eth_account.hdaccount import generate_mnemonic
from web3.auto import w3

def generate_new_wallet():
    """
    Generate a new wallet and mnemonic
    """
    mnemonic = generate_mnemonic(12, "english")
    account = w3.eth.account.from_mnemonic(mnemonic)
    private_key = account._private_key
    return private_key, mnemonic
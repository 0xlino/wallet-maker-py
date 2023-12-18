from generate_new_wallet import generate_new_wallet

def generate_loop(num): 
    """
    Generate a list of new wallets.

    Args:
        num (int): The number of wallets to generate.

    Returns:
        list: A list of new wallets.
    """
    return [generate_new_wallet() for _ in range(num)]
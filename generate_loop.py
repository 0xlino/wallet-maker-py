from generate_new_wallet import generate_new_wallet

def generate_loop(num): 
    return [generate_new_wallet() for _ in range(num)]
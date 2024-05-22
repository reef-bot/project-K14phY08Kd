import random

def generate_random_code():
    # Generate a random code for selecting winners
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8)
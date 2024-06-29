# scripts/generate_wallet.py
from web3 import Web3

def create_wallet():
    web3 = Web3()
    account = web3.eth.account.create()
    return {'address': account.address, 'private_key': account.key.hex()}
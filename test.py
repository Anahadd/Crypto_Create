from crypto_create import Cryptocurrency

my_coin = Cryptocurrency(name="Nod's Coin", symbol="MYC")

print(f"Name: {my_coin.name}")
print(f"Symbol: {my_coin.symbol}")

my_coin.create_transaction({"from": "Anahad", "to": "Anunya", "amount": 10})
my_coin.create_transaction({"from": "Anunya", "to": "Anna", "amount": 5})

print("\nBlockchain:")
for block in my_coin.get_blockchain():
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}\n")

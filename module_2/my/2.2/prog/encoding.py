from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

def crypto_key(x):
    try:
        print(decrypt(x, encrypted))
    except:
        print('error')
    finally:
        print('finally')

password = ["9XB8nsIqRfYeswC",
            "4sEhUGLEZti9BiN",
            "bDjmT0NcIW8nzhb",
            "ZN6QQoMOO1ZQLUY",
            "RVrF2qdMpoq6Lib",
            "tnnX7HH3vJ9Hiji",
            "C24TJYYkqekv40l",
            "B2ropluPaMAitzE",
            "DRezNUVnr2zC0CP",
            "XCNmpTvvZb1n3mX"]
for i in range(len(password)):
    print(crypto_key(password[i]))





#password = ['9XB8nsIqRfYeswC', 'RVrF2qdMpoq6Lib', '9XB8nsIqRfYeswC']
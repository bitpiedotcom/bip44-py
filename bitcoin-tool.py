from bip32utils import BIP32Key, BIP32_HARDEN
from mnemonic import Mnemonic

# Bitcoin https://github.com/satoshilabs/slips/blob/master/slip-0044.md
coin_type = 0
# 0: receive, 1: change
path = 0
index = 0

while True:
    seed = raw_input('Please input your words separated by space: ')
    password = raw_input('Please input your password: ')

    m = BIP32Key.fromEntropy(Mnemonic.to_seed(seed, passphrase=password))

    m = m.ChildKey(44 + BIP32_HARDEN)
    m = m.ChildKey(coin_type + BIP32_HARDEN)
    m = m.ChildKey(0 + BIP32_HARDEN)
    m = m.ChildKey(path)
    m = m.ChildKey(index)

    print 'First address is %s' % m.Address()

import numpy as np
import prime

# This application uses two large prime numbers to implement public key
# cryptography. It generates a public key and a private key.  The
# keys are symmetric, so if one key is used to encrypt, then the other can be
# used to decrypt.

p1 = prime.get_next_prime(np.int64(2**63 - 1))
p2 = prime.get_next_prime(np.int64(2**62 - 1))

print(p1)
print(p2)

# Now we have found two large prime numbers and can start to perform public
# key cryptography.
# ...
# Pretend that there was more code here.

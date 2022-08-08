
from Crypto.PublicKey import ECC


key = ECC.generate(curve='P-256')
private_key = key.export_key()
public_key = key.publickey().export_key()


# Save private key to file
with open('private_key.pem', 'wb') as f:
    f.write(private_key)

# Save public key to file
with open('public.pem', 'wb') as f:
    f.write(public_key)


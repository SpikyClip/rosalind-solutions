import numpy as np

filename = 'MRNA.txt'
with open(filename) as f:
    prot_seq = f.read().strip()

# prot_seq = 'MA'

permute = {'F': 2,'L': 6,'I': 3,'V': 4,'M': 1,'S': 6,'P': 4,'T': 4,
    'A': 4,'Y': 2,'H': 2,'N': 2,'D': 2,'STOP': 3,'Q': 2,'K': 2,'E': 2,
    'C': 2,'R': 6,'G': 4,'W': 1}

permute_cache = {aa: 0 for aa in permute.keys()}

for aa in prot_seq:
    for key in permute:
        if aa == key:
            permute_cache[key] += 1

permute_list = [permute['STOP']]

for aa, freq in permute_cache.items():
    print(aa)
    print(f"{permute[aa]}**{freq}")
    value = permute[aa]**freq
    permute_list.append(value)

result = np.prod(permute_list)%1_000_000

print(result)
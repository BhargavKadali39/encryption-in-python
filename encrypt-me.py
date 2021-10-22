
from math import sqrt, ceil

give_me_data = input("Enter data to encrypt: ")
give_me_data = give_me_data.replace(" ", "")
size = len(give_me_data)

t1 = int(ceil(sqrt(size)))
t2 = int(ceil(float(size) / t1))

rows = min(t1, t2)
cols = max(t1, t2)
encrypted_data = []

while give_me_data:
    encrypted_data.append(give_me_data[:cols])
    give_me_data = give_me_data[cols:]
    
for j in range(cols):
    encrypting = []
    for i in range(rows):
        try:
            encrypting.append(encrypted_data[i][j])
        except IndexError:
            pass
    print(''.join(encrypting), end='\n')

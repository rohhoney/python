c_alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input()

for i in c_alpa:
    S = S.replace(i, '0')

print(len(S))
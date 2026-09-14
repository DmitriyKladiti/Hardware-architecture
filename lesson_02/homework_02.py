A = True
B = True
C = True

result1 = (not (A and B)) or (not (A or C))
print(result1)

result2 = (A and B) or (not B and C)
print(result2)

result3 = (A and B) or not C
print(result3)



# Эксперементы с битовыми операиями 

a = 0b0110
b = 0b1001
c = 0b0000
d = 0b1111

# AND
print(f"\n{a & b:04b}")
print(f"{b & c:04b}")
print(f"{b & d:04b}")

# OR
print(f"\n{a | b:04b}")
print(f"{b | c:04b}")
print(f"{c | d:04b}")

# NOT
print(f"\n{~a :04b}")
print(f"{~b:04b}")
print(f"{~c:04b}")
print(f"{~d:04b}")

# XOR
print(f"\n{a ^ b:04b}")
print(f"{b ^ c:04b}")
print(f"{c ^ d:04b}")
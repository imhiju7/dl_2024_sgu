import numpy as np
print("Tinh chu vi va dien tich hinh tron")
r = int(input("Moi ban nhap ban kinh r: "))
c = 2 * np.pi * r
s = np.pi * r * r
print("Chu vi hinh tron: %.2f"%c)
print("Dien tich hinh tron: %.2f"%s)
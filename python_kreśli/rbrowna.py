#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input("Ile ruchów? : "))
x = y = 0
wsp_x = [0]
wsp_y = [0]

for i in range(0, n):
	#wylosuj kąt i zamień go na radiany
	rad = float(random.randint(0, 360)) * np.pi / 180
	x = x + np.cos(rad)
	y = y + np.sin(rad)
	wsp_x.append(x)
	wsp_y.append(y)

print(wsp_x, wsp_y)
	
# oblicz wektor końcowego przesunięcia
s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia", s )

plt.plot(wsp_x, wsp_y, "r:+", color="green", linewidth="3", alpha=0.5)
plt.plot([0, wsp_x[-1]],[0, wsp_y[-1]])
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("Wsp_x")
plt.ylabel("Wsp_y")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()

import random
import matplotlib.pyplot as plt

flips = 10000
coin_flips = [random.randint(0, 1) for i in range(flips)]
heads = [sum(coin_flips[:i]) / (i+1) for i in range(flips)]

plt.plot(heads, label="Proportion of Heads")
plt.axhline(y=0.5, color='r', linestyle='--', label="Expected Probability (0.5)")
plt.title("Law of Large Numbers")
plt.ylim(0, 1)
plt.legend()
plt.show()

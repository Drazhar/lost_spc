import matplotlib.pyplot as plt
import numpy as np

from lost_spc.calculations.spc_values import ARL, ARL_R, oc, oc_r, power

# power, OC und ARL x_bar-Karte
k = np.linspace(-4, 4, 500)
sigma = 0.0262
mu = 1.2023 + k * sigma

_, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].plot(mu, power(k, 5), label="m = 5")
ax[0].plot(mu, power(k, 10), label="m = 10")
ax[0].plot(mu, power(k, 15), label="m = 15")

ax[0].legend()
ax[0].grid()
ax[0].set_xlabel("Wahrer Erwartungswert des Prozessmerkmales")
ax[0].set_title(r"Gütefunktion für die $\bar x$-Karte")

k0 = np.linspace(0, 4)
ax[1].plot(k0, oc(k0, 5), label="m = 5")
ax[1].plot(k0, oc(k0, 10), label="m = 10")
ax[1].plot(k0, oc(k0, 15), label="m = 15")

ax[1].legend()
ax[1].grid()
ax[1].set_xlabel(r"Abweichung von $\mu_0$ in Vielfachen von $\sigma$")
ax[1].set_title(r"Operationscharakteristik für die $\bar x$-Karte")

ax[2].plot(mu, ARL(k=k, m=5))
ax[2].grid()
ax[2].set_xlabel("Wahrer Erwartungswert des Prozesses")
ax[2].set_title(r"Durchschnittliche Lauflänge für die $\bar x$-Karte")
plt.tight_layout()
plt.show()

# power, OC und ARL x_bar-Karte R-Karte
_, ax = plt.subplots(1, 2, figsize=(15, 5))

lam = np.linspace(1, 5, 500)
ax[0].plot(lam, oc_r(lam=lam, m=5), label="m=5")
ax[0].plot(lam, oc_r(lam=lam, m=10), label="m=10")
ax[0].plot(lam, oc_r(lam=lam, m=15), label="m=15")

ax[0].legend()
ax[0].grid()
ax[0].set_xlabel("Verhältnis der Prozessstreuung in Phase II bzgl. Phase I")
ax[0].set_title(r"Operationscharakteristik für die $R$-Karte")

ax[1].plot(lam, ARL_R(lam=lam, m=5), label="m=5")
ax[1].plot(lam, ARL_R(lam=lam, m=10), label="m=10")
ax[1].plot(lam, ARL_R(lam=lam, m=15), label="m=15")

ax[1].legend()
ax[1].grid()
ax[1].set_xlabel("Verhältnis der Prozessstreuung in Phase II bzgl. Phase I")
ax[1].set_title(r"Mittlere Lauflänge der $R$-Karte")
plt.tight_layout()
plt.show()


# Berechnung der ARL für verschiedene m-Werte und Darstellung
_, ax = plt.subplots(1, 2, figsize=(15, 5))

# X̄ control chart
k = np.linspace(0, 2, 200)

for m in [2, 3, 5, 10]:
    ax[0].plot(k, ARL(k=k, m=m), label=f"m={m}")

ax[0].legend()
ax[0].grid()
ax[0].set_xlabel("$k = (\\mu_1 - \\mu_0) / \\sigma$")
ax[0].set_title("ARL der $\\bar{X}$-Karte")

# R-Karte
lam = np.linspace(1, 2, 500)

for m in [2, 3, 5, 10, 20]:
    ax[1].plot(lam, ARL_R(lam=lam, m=m), label=f"m={m}")

ax[1].legend()
ax[1].grid()
ax[1].set_xlabel("$\\lambda = \\sigma_1 / \\sigma_0$")
ax[0].set_ylabel("ARL")
ax[1].set_title("ARL der R-Karte")
plt.tight_layout()
plt.show()

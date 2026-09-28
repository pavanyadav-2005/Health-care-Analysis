import matplotlib.pyplot as plt
ages=[0.19,0.22,0.27,0.32,0.37,0.42,0.47,0.52,0.57,0.62,0.67,0.72]
illness=[938,1452,595,368,188,152,238,357,478,530,484,1652]
plt.figure(figsize=(12,7))
plt.bar(ages,illness,width=0.02)
plt.title("Total no.of illness by ages")
plt.xlabel("ages")
plt.ylabel("illness")
plt.show()
import matplotlib

matplotlib.use('tkagg')  # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(range(10))
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
import scipy.stats as st
import os

plt.style.use(os.path.join(os.getcwd(), 'mystyle.mplstyle'))

nvalues = 10
norm_variates = rnd.randn(nvalues)

for i, v in enumerate(sorted(norm_variates), start=1):
    print('{0:2d} {1:+.4f}'.format(i, v))

N = 4857
mean = 63.8
serror = 0.06
sdev = serror * np.sqrt(N)
rvnorm = st.norm(loc=mean, scale=sdev)

rvnorm.cdf(68)

rvnorm.cdf(63)

100 * (rvnorm.cdf(68) - rvnorm.cdf(63))
st.rv_continuous.fit

categories = [
    ('Petite', 59, 63),
    ('Average', 63, 68),
    ('Tall', 68, 71),
]
for cat, vmin, vmax in categories:
    percent = 100 * (rvnorm.cdf(vmax) - rvnorm.cdf(vmin))
    print('{0:>8s}: {1:.2f}'.format(cat, percent))

too_short = 100 * rvnorm.cdf(59)
too_tall = 100 * (1 - rvnorm.cdf(71))
unclassified = too_short + too_tall
print(too_short, too_tall, unclassified)

a = rvnorm.ppf(0.25)
b = rvnorm.ppf(0.75)
print(a, b)

mean, variance, skew, kurtosis = rvnorm.stats(moments='mvks')
print(mean, variance, skew, kurtosis)

eta = 1.0
beta = 1.5
rvweib = st.weibull_min(beta, scale=eta)

xmin = 0
xmax = 3
xx = np.linspace(xmin, xmax, 200)
plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.plot(xx, rvweib.cdf(xx))
plt.title('CDF')
plt.xlabel('Height (in)')
plt.ylabel('Proportion of women')
plt.subplot(1, 2, 2)
plt.plot(xx, rvweib.pdf(xx))
plt.title('PDF')
plt.xlabel('Height (in)')

plt.show()

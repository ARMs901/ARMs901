
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, sin(x))
plot(x, cos(x), 'rD')
plot(x, -sin(x), 'g--')
show()
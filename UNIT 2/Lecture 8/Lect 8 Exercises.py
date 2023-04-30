import scipy.integrate
import numpy as np
import random
def gaussian(x, mu, sigma):
    "assumes x, mu, sigma numbers return P(x) accr. to Gaussian Distribution"
    factor1 = (1.0/ (sigma * ((2**np.pi)**0.5)))
    factor2 = np.e**-(((x - mu)**2)/ (2 * sigma * 2))
    return factor1 * factor2


def check_empirical (mu_max, sigma_max, num_trials):

    for t in range(num_trials):
        mu = random.randint(-mu_max, mu_max + 1)
        sigma = random.randint(1, sigma_max)
        print('For mu = ', mu, ' and sigma = ',sigma)
        for num_std in (1,2,3):
            area = scipy.integrate.quad(gaussian, mu-num_std*sigma, mu + num_std*sigma,(mu, sigma))[0]
            print(' Fraction within ', num_std, 'std =', round(area,4))

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means =[]
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5 * random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color= color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means),
               hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1, 1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
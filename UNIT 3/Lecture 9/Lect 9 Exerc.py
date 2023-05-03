import random
import pylab as plt
import numpy as np
def plot_means(num_dice_per_trial, num_dice_thrown, num_bins,
               legend, color, style):
    means =[]
    num_trials = num_dice_thrown//num_dice_per_trial
    for i in range(num_trials):
        vals = 0
        for j in range(num_dice_per_trial):
            vals += 5*random.random()
        means.append(vals/num_dice_per_trial)
    plt.hist(means, num_bins, color = color, label = legend,
             weights = np.array(len(means)*[1])/len(means),
             hatch = style)
    return sum(means)/len(means), np.var(means)

mean, var = plot_means(1,10000, 11, '1 die','y','.')
mean, var = plot_means(100,10000, 11, '1 die','c','/')
plt.title('Rolling Continous Dice')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend(loc = 'upper left')
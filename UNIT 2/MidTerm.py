def max_sequence(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        print('Max Ending Here is ', max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
        print('Max so far is: ', max_so_far)
    return max_so_far


def solveit(test):
    for x in range(1000000):
        if test(x):

            return x
        elif test(-x):

            return -x
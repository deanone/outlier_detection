import sys
from random import seed
from random import random


def detect_and_replace_outliers(arr, threshold):
	"""

	This function implements the outlier detection and replacement method proposed by Basu and Meckesheimer
	'Automatic outlier detection for time series: an application to sensor data'
	https://link.springer.com/article/10.1007/s10115-006-0026-6

	:param arr: the array in which the outliers are searched for
	:param threshold: the threshold that determines if a value is an outlier 

	"""
	s = len(arr)
	first_value = arr[0]
	last_value = arr[s - 1]
	for i in range(s):
		temp = []
		if i == 0:
			temp.append(first_value)
			temp.append(arr[i])
			temp.append(arr[i + 1])
		elif i == (s - 1):
			temp.append(arr[i - 1])
			temp.append(arr[i])
			temp.append(last_value)
		else:
			temp.append(arr[i - 1])
			temp.append(arr[i])
			temp.append(arr[i + 1])
		temp.sort()
		median = temp[1]
		if abs(median - arr[i]) > threshold:
			# v[i] is an outlier
			# replace it the median
			arr[i] = median
		temp.clear()


def main():
	"""
	
	Starting point of the application.

	"""

	# seed random number generator
	seed(1)

	# read command line arguments
	n = int(sys.argv[1])
	low = int(sys.argv[2])
	high = int(sys.argv[3])

	# Generate n random numbers in range [low, high]
	arr = []
	for _ in range(n):
		val = low + (random() * (high - low))
		arr.append(val)

	threshold = sum(arr) / len(arr)
	arr[5] = 1589 # large value outside the [low, high] range considered as outlier

	# before outlier detection
	print('Before outlier detection:')
	for i in range(len(arr)):
		print(round(arr[i], 3), end=' ')
	print('\n')

	detect_and_replace_outliers(arr, threshold)

	# after outlier detection
	print('After outlier detection:')
	for i in range(len(arr)):
		print(round(arr[i], 3), end=' ')
	print('\n')


if __name__ == '__main__':
	main()
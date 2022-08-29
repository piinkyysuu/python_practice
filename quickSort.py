import random

def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp

def partition(arr, i, j):
	pivot = j
	j = j - 1
	while i < j:
		while arr[i] <= arr[pivot] and i < j:
			i = i + 1
		while arr[j] >= arr[pivot] and j > i:
			j = j - 1
		swap(arr, i, j)
	if (arr[i] <= arr[pivot]):
		return pivot
	else:
		swap(arr, i, pivot)
		return i

def quickSort(arr, start = -1, end = -1):
	if start == -1:
		start = 0
	if end == -1:
		end = len(arr) - 1
	if end <= start:
		return
	p = partition(arr, start, end)
	quickSort(arr, start, p - 1)
	quickSort(arr, p + 1, len(arr) - 1)

if __name__ == "__main__":
	numberList = random.sample(range(0, 20), 20)
	print(numberList)
	quickSort(numberList)
	print(numberList)
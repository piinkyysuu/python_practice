def binarySearch(value, numberList, start=-1, end=-1):
	listLen = len(numberList)
	if start == -1:
		start = 0
	if end == -1:
		end = listLen - 1
	mid = (start + end) // 2
	if numberList[mid] == value:
		return mid
	if start - end == -1:
		return -1
	if value > numberList[mid]:
		return binarySearch(value, numberList, mid + 1, end)
	elif value < numberList[mid]:
		return binarySearch(value, numberList, 0, mid - 1)

if __name__ == "__main__":
	numberList = list(range(1, 40, 3))
	print(numberList)
	number = 13
	print(f'binarySearch result: {binarySearch(number, numberList)}')
	print(f'index of number: {numberList.index(number)}')

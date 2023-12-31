class ArrayHandler():
    class Sort():
        @staticmethod
        def InsertionSort(arr : list ) -> list :
            for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return arr

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    sortedArr = ArrayHandler.Sort.InsertionSort(arr)
    print("arr:%s"%(str(arr)))
    print("sortedArr:%s"%(str(sortedArr)))

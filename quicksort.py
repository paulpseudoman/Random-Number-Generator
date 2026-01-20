from rng_module import fp_rng
import math
def partition(arr, low, high):
   pivot = arr[high]
   i = low - 1
   for j in range(low, high):
       if arr[j] <= pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]
   arr[i + 1], arr[high] = arr[high], arr[i + 1]
   return i + 1
def quick_sort(arr, low, high):
   if low < high:
       pi = partition(arr, low, high)
       quick_sort(arr, low, pi - 1)
       quick_sort(arr, pi + 1, high)
data = fp_rng(seed = (math.pi)/10 ,steps = 1000)
print("Unsorted Array:",data)
quick_sort(data, 0, len(data) - 1)
print("Sorted Array:",data)

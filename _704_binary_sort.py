def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n-1):
        ai = arr[i]
        j = i - 1 
        while ( j >= 0 and arr[j] > ai ):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ai


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i
        for k in range(i+1, n):
            if arr[k] < arr[min_index]:
                min_index = k  
        if (min_index != i):
            arr[min_index], arr[i] = arr[i],arr[min_index] 


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for k in range(0, len(arr)-1-i):
            if (arr[k] < arr[k+1]):
                arr[k], arr[k+1] = arr[k+1], arr[k]
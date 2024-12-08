def search_recursion(arr: list, target: int, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return False

    midd = (right+left) // 2
    if arr[midd] > target:
        return search_recursion(arr, target, left, right - 1)

    elif arr[midd] < target:
       return search_recursion(arr, target, midd + 1, right)

    else:
        return True

    
a  = search_recursion([1, 2, 3, 4, 5, 8 ,10], 0)
print(a),

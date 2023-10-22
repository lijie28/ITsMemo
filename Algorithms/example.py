import random


def get_random_ist(n=100, max_value=1000):
    result = []
    for i in range(0, n):
        value = random.randint(0, max_value)
        result.append(value)
    return result


def main():
    values = get_random_ist()
    # result = bubbleSort(values)
    # result = insertionSort(values)
    result = merge_sort(values)
    print(result)
    # newlist = range(0, 10, -1)
    # for i in range(10, 0, -1):
    #     print(i)


def bubble_sort(values):
    temp = values
    while True:
        changedInThisLoop = False
        for i in range(0, len(temp)-1):
            if values[i] > temp[i+1]:
                midValue = temp[i]
                temp[i] = temp[i+1]
                temp[i+1] = midValue
                changedInThisLoop = True
        if not changedInThisLoop:
            break
    return temp
    # print(bubbleSort.__name__)


def insertion_sort(values):
    temp = values
    new = [values[0]]
    for i in range(1, len(temp)):
        selectedValue = temp[i]
        newListLen = len(new)
        for n in range(0, newListLen):
            compareValue = new[newListLen-1-n]
            if selectedValue >= compareValue:
                new.insert(newListLen-n, selectedValue)
                break
    return new


def merge_sort(values):
    # 基于分治策略，将一个数组分为两半，然后递归地对这两半进行排序，最后将它们合并成一个有序数组
    def _inMerge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            #  精髓：通过while和i,j的增值，下方以下标记录当前最大值而进行比较
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 精髓：left或right有一方有可能未进入循环而未插入到result里
        # 但left和right都是由小到大排好的，所以只需要插入剩余即可（只可能是单方，另一方为空）
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(values) <= 1:
        return values
    x = len(values)//2
    left = values[:x]
    right = values[x:]
    left_half = merge_sort(left)
    right_half = merge_sort(right)

    # 合并两个子数组
    return _inMerge(left_half, right_half)


def quick_sort(arr):
    # 它使用分治的策略来将一个未排序的列表分成两个子列表，然后递归地对子列表进行排序
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    main()
    # test()

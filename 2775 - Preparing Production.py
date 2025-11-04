import sys

sys.setrecursionlimit(20000)


def merge_sort_with_cost(arr, times):
    def merge_sort(l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        cost = merge_sort(l, mid) + merge_sort(mid + 1, r)
        cost += merge(l, mid, r)
        return cost

    def merge(l, mid, r):
        temp_arr = []
        temp_time = []
        i, j = l, mid + 1
        cost = 0

        prefix_left = [0]
        for k in range(l, mid + 1):
            prefix_left.append(prefix_left[-1] + times[k])

        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp_arr.append(arr[i])
                temp_time.append(times[i])
                i += 1

            else:
                num_left = mid - i + 1
                cost += num_left * times[j] + (prefix_left[-1] - prefix_left[i - l])
                temp_arr.append(arr[j])
                temp_time.append(times[j])
                j += 1

        while i <= mid:
            temp_arr.append(arr[i])
            temp_time.append(times[i])
            i += 1
        while j <= r:
            temp_arr.append(arr[j])
            temp_time.append(times[j])
            j += 1

        arr[l:r + 1] = temp_arr
        times[l:r + 1] = temp_time
        return cost

    return merge_sort(0, len(arr) - 1)


def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    while idx < len(input_data):
        N = int(input_data[idx]);
        idx += 1
        arr = list(map(int, input_data[idx:idx + N]));
        idx += N
        times = list(map(int, input_data[idx:idx + N]));
        idx += N
        print(merge_sort_with_cost(arr, times))


if __name__ == "__main__":
    main()
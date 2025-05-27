def gcbr_insertion_sort(gcbr_arr):
    gcbr_count = 0
    for gcbr_i in range(1, len(gcbr_arr)):
        gcbr_key = gcbr_arr[gcbr_i]
        gcbr_j = gcbr_i - 1
        while gcbr_j >= 0 and gcbr_arr[gcbr_j] > gcbr_key:
            gcbr_arr[gcbr_j + 1] = gcbr_arr[gcbr_j]
            gcbr_j -= 1
            gcbr_count += 1
        gcbr_arr[gcbr_j + 1] = gcbr_key
    return gcbr_count

def pick_peaks(arr):
    result = {
        'pos': [],
        'peaks': []
    }

    if len(arr) == 0:
        return result
    last_pos = None
    last_peak = None
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            result['pos'].append(i)
            result['peaks'].append(arr[i])
            last_pos = None
            last_peak = None
            continue

        if arr[i - 1] < arr[i] == arr[i + 1]:
            if not last_peak is None:
                continue
            else:
                last_peak = arr[i]
                last_pos = i

        if arr[i] > arr[i + 1]:
            if not last_peak is None:
                result['pos'].append(last_pos)
                result['peaks'].append(last_peak)
                last_pos = None
                last_peak = None

    return result

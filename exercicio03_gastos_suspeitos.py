def activityNotifications(expenditure, d):
    def get_median(freq, d):
        count = 0
        if d % 2 == 1:
            median_pos = d // 2 + 1
            for i in range(201):
                count += freq[i]
                if count >= median_pos:
                    return i
        else:
            first = None
            second = None
            for i in range(201):
                count += freq[i]
                if first is None and count >= d // 2:
                    first = i
                if count >= d // 2 + 1:
                    second = i
                    break
            return (first + second) / 2

    freq = [0] * 201
    for i in range(d):
        freq[expenditure[i]] += 1

    notifications = 0
    for i in range(d, len(expenditure)):
        median = get_median(freq, d)
        if expenditure[i] >= 2 * median:
            notifications += 1
        freq[expenditure[i - d]] -= 1
        freq[expenditure[i]] += 1

    return notifications

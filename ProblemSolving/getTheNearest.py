def closest_sum_pair(a1, a2, target):
    i = 0
    j = len(a2) - 1
    smallest_diff = abs(a1[0] + a2[-1] - target)
    closest_pair = (a1[0], a2[-1])

    while i < len(a1) and j >= 0:
        current_sum = a1[i] + a2[j]
        current_diff = abs(current_sum - target)

        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_pair = (a1[i], a2[j])

        if current_sum == target:
            return closest_pair

        elif current_sum < target:
            i += 1
        else:
            j -= 1

    return closest_pair



a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
target = 20
print(closest_sum_pair(a1,a2,target))
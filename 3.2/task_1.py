def max_non_overlapping_intervals(intervals):
    # Сортируем интервалы по времени их окончания
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for interval in intervals:
        if interval[0] > last_end_time:
            count += 1
            last_end
            _time = interval[1]
    
    return count

# Пример использования
n = int(input())
intervals = []
print()
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

print(max_non_overlapping_intervals(intervals))

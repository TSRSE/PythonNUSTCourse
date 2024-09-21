totalMinutesPassed = int(input())
totalHours = totalMinutesPassed // 60 if totalMinutesPassed // 60 > 9 else f'0{totalMinutesPassed // 60}'
totalMinutes = totalMinutesPassed % 60 if totalMinutesPassed % 60 > 9 else f'0{totalMinutesPassed % 60}'
print(f'{totalHours}:{totalMinutes}:00')
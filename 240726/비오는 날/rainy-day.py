n = int(input())
date_strings = []
for i in range(n):
    a = input().split()
    if a[2] == 'Rain':
        date_strings.append(str(a[0]+' '+ a[1]+' '+a[2]))
sorted_date_strings = sorted(date_strings, key=lambda date: (date[:4], date[5:7], date[8:]))

print(sorted_date_strings[0])
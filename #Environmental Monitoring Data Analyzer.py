data = [20, 30, 40, 60, 80]
avg = sum(data) / len(data)

print("Average:", avg)
print("Maximum:", max(data))
print("Minimum:", min(data))

if avg <= 30:
    print("Good Quality")
elif avg <= 60:
    print("Moderate Quality")
else:
    print("Poor Quality")
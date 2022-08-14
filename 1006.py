entry_values = []
weights = [2, 3, 5]
results = []

for i in range(3):
    entry_values.append(float(input()))

i = 0
while i < len(entry_values):
    results.append(entry_values[i] * weights[i])
    i += 1

result = sum(results) / sum(weights)

print("MEDIA = {:.1f}".format(result))

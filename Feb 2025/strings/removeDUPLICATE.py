s = "banana"
seen = set()
result = ""

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

## time complexity = O(1)

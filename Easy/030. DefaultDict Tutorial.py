from collections import defaultdict
n, m = map(int, input().split())

word_positions = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    word_positions[word].append(i)

# Read list B and output results
for _ in range(m):
    word = input().strip()
    if word in word_positions:
        print(' '.join(map(str, word_positions[word])))
    else:
        print(-1)

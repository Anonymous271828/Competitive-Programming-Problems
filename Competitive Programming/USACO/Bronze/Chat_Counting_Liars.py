# Feb. 15th, 2025
# By: CHAT-GPT. NOT SOL KWAK
# Description: apparently this is faster
# Time Complexity: O(n^2)
# Additional comments: i knew this shit didn't work. huzzah.
# Feb. 15th-16th, 2025
# By: Sol Kwak
# Description: Optimized approach
# Time Complexity: O(N)

N = int(input())
statements = []

for _ in range(N):
    m, n = input().split()
    n = int(n)
    statements.append((m, n))

# Extract all possible boundary points
possible_boundaries = sorted(set(n for _, n in statements))

min_liars = float('inf')

# Try each possible boundary and count liars
for boundary in possible_boundaries:
    liars = sum(1 for m, n in statements if (m == "G" and n > boundary) or (m == "L" and n < boundary))
    min_liars = min(min_liars, liars)

print(min_liars)

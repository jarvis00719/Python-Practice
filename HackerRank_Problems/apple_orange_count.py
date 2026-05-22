def countApplesAndOranges(s, t, a, o, apples, oranges):
    sum_apples_tree = []
    sum_oranges_tree = []

    # Apples
    for i in apples:
        i += a
        if s <= i <= t:
            sum_apples_tree.append(i)

    # Oranges
    for i in oranges:
        i += o
        if s <= i <= t:
            sum_oranges_tree.append(i)

    # Return counts, not lists
    return len(sum_apples_tree), len(sum_oranges_tree)


# Input Statements !!
s, t = map(int, input().split())   # House: Start, End
a, o = map(int, input().split())   # Location: apple, orange Tree's
m, n = map(int, input().split())   # Number of apples and oranges

apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

apple_count, orange_count = countApplesAndOranges(s, t, a, o, apples, oranges)

print(apple_count)
print(orange_count)

def count_unique_words(inp):
    ans = None
    # YOUR CODE GOES HERE
    ans = 0
    arr = list(inp.split())
    for word in arr:
        if len(set(word)) == len(word) and len(word) > 3:
            ans += 1
    return ans
print(count_unique_words('Hii Hello Helo Hey'))
print(count_unique_words('the fruits of the tree were basically oranges and apples'))
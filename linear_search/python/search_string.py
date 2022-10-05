def search_string(string , target):
    for index in range(len(string)):
        if string[index] == target:
            return index

    return -1


string = 'afsan khan'
target = 'f'
ans = search_string(string, target)
print(ans)
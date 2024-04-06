def icecreamParlorBasic(m, arr):
    for i, flavor1 in enumerate(arr, start=1):
        for j, flavor2 in enumerate(arr, start=1):
            if flavor1 + flavor2 == m and i != j:
                return [i, j]

def icecreamParlor(m, arr):
    cost_to_index = {}
    for i, flavor1 in enumerate(arr):
        if m-flavor1 in cost_to_index:
            j = cost_to_index[m-flavor1]
            return [j+1, i+1]
        else:
            cost_to_index[flavor1] = i


if __name__ == '__main__':
    print(icecreamParlor(6, [1,3,4,5,6]))
    print(icecreamParlor(4, [2,2,4,3]))
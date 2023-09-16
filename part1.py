def cardinality_items(file_name):
    file_source = open(file_name, "r")
    unique_set = set()
    while True:
        line = file_source.readline()
        if not line:
            break
        line = line.split(",")
        for word in line:
            if word.strip() != "":
                unique_set.add(word.strip())
    print(unique_set)
    return len(unique_set)


def all_itemsets(unique_list, size):
    return travel(unique_list, 0, size)


def travel(unique_list, left, size):
    if size == 1:
        result = []
        for i in range(left, len(unique_list)):
            result.append({unique_list[i]})
        return result

    result = []
    for i in range(left, len(unique_list) - size + 1):
        tempo_list = travel(unique_list, i + 1, size - 1)
        for x in tempo_list:
            x.add(unique_list[i])
            result.append(x)

    return result


cardinality_items("basket_data.csv")
print(all_itemsets(["a", "b", "c"], 2))

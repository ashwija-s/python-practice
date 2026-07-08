def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in adj_list:
        for j in adj_list[i]:
            adj_matrix[i][j] = 1
    for i in adj_matrix:
        print(f"{i}")
    return adj_matrix
adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
def similar_pair(n, k, edges):
    from collections import defaultdict

    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    result = 0

    def dfs(node, ancestors):
        nonlocal result
        for anc in ancestors:
            if abs(anc - node) <= k:
                result += 1
        for child in tree[node]:
            dfs(child, ancestors + [node])

    all_nodes = set(range(1, n + 1))
    children = set(child for _, child in edges)
    root = list(all_nodes - children)[0]

    dfs(root, [])
    return result

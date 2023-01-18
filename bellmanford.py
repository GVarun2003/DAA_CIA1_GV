def bellmanford(m, s):
    n, inf = len(m), float("inf")
    v = range(n)
    dist = [inf for _ in v]
    dist[s] = 0
    for _ in range(n - 1):
        for i in v:
            for j in v:
                w = m[i][j]
                if dist[i] != inf and dist[i] + w < dist[j]:
                    dist[j] = dist[i] + w
                    
    for i in v:
        for j in v:
            w = m[i][j]
            if dist[i] != inf and dist[i] + w < dist[j]:
                return None
            
    return dist
    
def main():
    s=0
    m=[[0,1,2,3,5],
        [2,0,-1,1,-1],
        [1,6,0,13,2],
        [1,2,1,0,-1],
        [3,3,2,4,0]]
    print(bellmanford(m,s))

main()
def bellmanford(m, s):
    n, inf = len(m), float("inf")
    v = range(n)
    dist = [inf for x in v]
    dist[s] = 0
    for x in range(n - 1):
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
    m=[[0,4,2,0,0,],[0,0,3,2,3],[0,1,0,4,5],[0,0,0,0,0],[0,0,0,0,-5]]
    print(bellmanford(m,s))

main()

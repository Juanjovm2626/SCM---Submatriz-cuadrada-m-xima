def largestsquare_bruteforce(matriz):
    n = len(matriz)
    m = len(matriz[0])
    ans = 0
    for i in range(0, n):
        for j in range(0,m):
            maxside= min (n-i,m-j)
            for k in range (1, maxside):
                ok = True
                for l in range(j,j+k):
                    if matriz[i+k-1][l]==1:
                        ok = False
                        break
                for m in range(i,i+k):
                    if matriz[m][j+k-1]==1:
                        ok = False
                        break
                if not ok : break
                ans = max(ans, k)
    
    return print(f"La submatriz mas grande es de {ans} X {ans}")


largestsquare_bruteforce([[0,0,0],[0,0,1],[1,0,0]])

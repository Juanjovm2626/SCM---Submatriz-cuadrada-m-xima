def Solucion_Tabulacion(Matriz):
    columnas = len(Matriz[0])
    filas = len(Matriz)
    adj=[[0 for _ in range(columnas)] for _ in range(filas) ]

    for i in range(filas):
        for j in range(columnas):
            if (i==0 or j==0) and Matriz[i][j]==0:
                adj[i][j]=1 
            elif Matriz[i][j] == 0:
                adj[i][j] = min(adj[i-1][j-1],adj[i][j-1],adj[i-1][j]) + 1
            else:
                adj[i][j] = 0

    Cuadrado = max(max(fila) for fila in adj)
    return print(f"El cuadrado mas grande es de dimension {Cuadrado}x{Cuadrado}")

Solucion_Tabulacion([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])



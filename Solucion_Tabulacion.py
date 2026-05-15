

def Solucion_Tabulacion(Matriz):
    columnas = len(Matriz[0])
    filas = len(Matriz)
    adj=[[0 for _ in range(columnas)] for _ in range(filas) ]

    for i in range(filas):
        for j in range(columnas):
            if Matriz[i][j] == 0:
                adj[i][j]=



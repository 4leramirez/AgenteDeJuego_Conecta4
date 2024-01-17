def right (i,j,l,mat,find):
    v=True
    c=1
    while v and c<l:
        if mat[i][j+c]!=find[c]:
            v=False
        c+=1
    return v

def down (i,j,l,mat,find):
    v=True
    c=1
    while v and c<l:
        if mat[i+c][j]!=find[c]:
            v=False
        c+=1
    return v

def downright (i,j,l,mat,find):
    v=True
    c=1
    while v and c<l:
        if mat[i+c][j+c]!=find[c]:
            v=False
        c+=1
    return v

def downleft (i,j,l,mat,find):
    v=True
    c=1
    while v and c<l:
        if mat[i+c][j-c]!=find[c]:
            v=False
        c+=1
    return v

def gane (n,m,mat,find,l):
    for i in range(n):
        for j in range(m):
            if mat[i][j]==find[0]:
                if j<=m-l:
                    d=right(i,j,l,mat,find)
                    if d:
                        return True
                if i<=n-l:
                    d=down(i,j,l,mat,find)
                    if d:
                        return True
                if i<=n-l and j<=m-l:
                    d=downright(i,j,l,mat,find)
                    if d:
                        return True
                if i<=n-l and j>=l-1:
                    d=downleft(i,j,l,mat,find)
                    if d:
                        return True
    return False

def abajo(tab,i,j):
    lista=[]
    for n in range(4):
        lista.append(tab[i+n][j])
    return lista

def derecha(tab,i,j):
    lista=[]
    for n in range(4):
        lista.append(tab[i][j+n])
    return lista

def abajoDer(tab,i,j):
    lista=[]
    for n in range(4):
        lista.append(tab[i+n][j+n])
    return lista

def abajoIzq(tab,i,j):
    lista=[]
    for n in range(4):
        lista.append(tab[i+n][j-n])
    return lista

class pila:
    
    def __init__(self):
        self.data=[]
        self.capacity=7
    
    def push(self,a):
        if len(self.data)<self.capacity:
            self.data.append(a)
    
    def pop(self):
        return self.data.pop(-1)
    
    def peek(self):
        return self.data[-1]
    
    def empty(self):
        return len(self.data)==0
    
    def full(self):
        return len(self.data)==self.capacity
    
    def count(self):
        return len(self.data)

def movval(tab):
    lista=[]
    c=0
    for i in range (7):
        if tab[0][i]==0:
            lista.append(i)
            c+=1
    return lista,c

def validar(lista,u):
    return False if u in lista else True

def insertar(fich,col,player,v=False):
    for i in range (5,-1,-1):
        if fich[i][col]==0:
            if player:
                fich[i][col]=2
                return fich if v else (fich,i)
            else:
                fich[i][col]=1
                return fich

def continuidad(tab,player):
    if player:
        if gane(6,7,tab,[2,2,2,2],4):
            return 1
        else:
            for i in range (7):
                if tab[0][i]==0:
                    return 2
            return 0
    else:
        if gane(6,7,tab,[1,1,1,1],4):
            return -1
        else:
            for i in range (7):
                if tab[0][i]==0:
                    return 2
            return 0

def mostrarTab(tab):
    print('\n\n')
    for i in range(6):
        for j in range(7):
            print(tab[i][j],end='\t')
        print('\n')

def contadorV(lista):
    for i in range(4):
        if lista[i]!=2:
            return False
    return True

def contador3T(lista):
    y,v=0,0
    for i in range(4):
        if lista[i]==2:
            y+=1
        elif lista[i]==0:
            v+=1
    return True if (y==3 and v==1) else False

def contador3F(lista):
    y,v=0,0
    for i in range(4):
        if lista[i]==1:
            y+=1
        elif lista[i]==0:
            v+=1
    return True if (y==3 and v==1) else False

def conecta4(tab,mv,fil):
    if fil<=2:
        if down(fil,mv,4,tab,[2,2,2,2]):
            return True
    for d in range(4):
        if mv>=0+d and mv<=3+d:
            if contadorV(derecha(tab,fil,mv-d)):
                return True
        if (fil>=0+d and fil<=2+d) and (mv>=0+d and mv<=3+d):
            if contadorV(abajoDer(tab,fil-d,mv-d)):
                return True
        if (fil>=0+d and fil<=2+d) and (mv>=3-d and mv<=6-d):
            if contadorV(abajoIzq(tab,fil-d,mv+d)):
                return True
    return False

def conecta3T(tab,i,j):
    if i<=2:
        if contador3T(abajo(tab,i,j)):
            return True
    for d in range(4):
        if j>=0+d and j<=3+d:
            if contador3T(derecha(tab,i,j-d)):
                return True
        if (i>=0+d and i<=2+d) and (j>=0+d and j<=3+d):
            if contador3T(abajoDer(tab,i-d,j-d)):
                return True
        if (i>=0+d and i<=2+d) and (j>=3-d and j<=6-d):
            if contador3T(abajoIzq(tab,i-d,j+d)):
                return True
    return False

def conecta3F(tab,i,j):
    if i<=2:
        if contador3F(abajo(tab,i,j)):
            return True
    for d in range(4):
        if j>=0+d and j<=3+d:
            if contador3F(derecha(tab,i,j-d)):
                return True
        if (i>=0+d and i<=2+d) and (j>=0+d and j<=3+d):
            if contador3F(abajoDer(tab,i-d,j-d)):
                return True
        if (i>=0+d and i<=2+d) and (j>=3-d and j<=6-d):
            if contador3F(abajoIzq(tab,i-d,j+d)):
                return True
    return False

def filCor(tab,listC,c):
    listF=[]
    for i in range(c):
        for j in range(5,-1,-1):
            if tab[j][listC[i]]==0:
                listF.append(j)
                break
    return listF

def borrar(copy,i,j):
    copy[i][j]=0
    return copy
    
def evaluar(tab,mv,fil):
    if conecta4(tab,mv,fil):
        return 4000
    listC,c=movval(tab)
    listF=filCor(tab,listC,c)
    p=0
    for n in range(c):
        i,j=listF[n],listC[n]
        if conecta3T(tab,i,j):
            p+=1
        if conecta3F(tab,i,j):
            p-=100
    return p

def altPt(listam,c,fich):
    alt=pila()
    copy=fich
    for i in range(c):
        m=listam[i]
        copy,fil=insertar(copy,m,True)
        ptj=evaluar(copy,m,fil)
        copy=borrar(copy,fil,m)
        alt.push((m,ptj))
    return alt

def bestmove(alt):
    u,p=None,-1000
    while not alt.empty():
        m,n=alt.pop()
        if (n>p):
            u=m
            p=n
        elif (n==p):
            import random
            u,p=random.choice([(u,p),(m,n)])
    return u

import numpy as np
tab=np.reshape([i*0 for i in range (42)], (6,7))
status=2
turno=False
mostrarTab(tab)
while status==2:
    listam,c=movval(tab)
    if turno:
        alt=altPt(listam,c,tab)
        b=bestmove(alt)
        tab=insertar(tab,b,turno,v=True)
    else:
        u=int(input('Ingrese su movimiento:'))-1
        while validar(listam,u):
            u=int(input("Movimiento no válido. Por favor, vuelva a ingresar su movimiento:"))-1
        tab=insertar(tab,u,turno)
    status=continuidad(tab,turno)
    if turno:
        turno=False
    else:
        turno=True
    mostrarTab(tab)
if status==1:
    print("Lo sentimos. La máquina te ha derrotado.")
elif status==-1:
    print("¡Felicidades, has ganado!")
elif status==0:
    print('La partida ha terminado en tablas. Bien jugado, y suerte para la próxima.')
    
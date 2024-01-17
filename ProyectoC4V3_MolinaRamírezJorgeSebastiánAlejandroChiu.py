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

class raiz:
    
    def __init__(self,m=-1,p=0):
        self.p=p
        self.m=m
        self.ha=None
        self.hb=None
        self.hc=None
        self.hd=None
        self.he=None
        self.hf=None
        self.hg=None
        
    def hijos(self):
        if self.hg is not None:
            return 7
        if self.hf is not None:
            return 6
        if self.he is not None:
            return 5
        if self.hd is not None:
            return 4
        if self.hc is not None:
            return 3
        if self.hb is not None:
            return 2
        if self.ha is not None:
            return 1
        return 0
    
    def minimax(self,tipo,prof,ctrl=False):
        if self.hijos()==0 or prof==0:
            return self.m,self.p
        else:
            mov=None
            k=-10000 if tipo else 10000
            opc=[]
            for i in range(self.hijos()):
                if i==0:
                    opc.append(self.ha.minimax(not tipo, prof-1))
                elif i==1:
                    opc.append(self.hb.minimax(not tipo, prof-1))
                elif i==2:
                    opc.append(self.hc.minimax(not tipo, prof-1))
                elif i==3:
                    opc.append(self.hd.minimax(not tipo, prof-1))
                elif i==4:
                    opc.append(self.he.minimax(not tipo, prof-1))
                elif i==5:
                    opc.append(self.hf.minimax(not tipo, prof-1))
                elif i==6:
                    opc.append(self.hg.minimax(not tipo, prof-1))
            if tipo:
                for i in range(self.hijos()):
                    v,w=opc[i]
                    if w==4000 and ctrl:
                        if i==0:
                            if self.ha.hijos()==0:
                                return v,w
                        elif i==1:
                            if self.hb.hijos()==0:
                                return v,w
                        elif i==2:
                            if self.hc.hijos()==0:
                                return v,w
                        elif i==3:
                            if self.hd.hijos()==0:
                                return v,w
                        elif i==4:
                            if self.he.hijos()==0:
                                return v,w
                        elif i==5:
                            if self.hf.hijos()==0:
                                return v,w
                        elif i==6:
                            if self.hg.hijos()==0:
                                return v,w
                    if (w>k):
                        mov=v
                        k=w
                    elif (w==k):
                        import random
                        mov,k=random.choice([(mov,k),(v,w)])
                    
            else:
                for i in range(self.hijos()):
                    v,w=opc[i]
                    if (w<k):
                        mov=v
                        k=w
                    elif (w==k):
                        import random
                        mov,k=random.choice([(mov,k),(v,w)])
            if self.m==-1:
                return mov,k
            else:
                return self.m,k
                

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
                return fich if v else (fich,i)

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

def contadorV(lista,player):
    n=2 if player else 1
    for i in range(4):
        if lista[i]!=n:
            return False
    return True

def contador3T(lista,player):
    y,v=0,0
    n=2 if player else 1
    for i in range(4):
        if lista[i]==n:
            y+=1
        elif lista[i]==0:
            v+=1
    return True if (y==3 and v==1) else False

def conecta4(tab,mv,fil,player):
    if fil<=2:
        sec=[2,2,2,2] if player else [1,1,1,1]
        if down(fil,mv,4,tab,sec):
            return True
    for d in range(4):
        if mv>=0+d and mv<=3+d:
            if contadorV(derecha(tab,fil,mv-d),player):
                return True
        if (fil>=0+d and fil<=2+d) and (mv>=0+d and mv<=3+d):
            if contadorV(abajoDer(tab,fil-d,mv-d),player):
                return True
        if (fil>=0+d and fil<=2+d) and (mv>=3-d and mv<=6-d):
            if contadorV(abajoIzq(tab,fil-d,mv+d),player):
                return True
    return False

def conecta3T(tab,i,j,player):
    if i<=2:
        if contador3T(abajo(tab,i,j),player):
            return True
    for d in range(4):
        if j>=0+d and j<=3+d:
            if contador3T(derecha(tab,i,j-d),player):
                return True
        if (i>=0+d and i<=2+d) and (j>=0+d and j<=3+d):
            if contador3T(abajoDer(tab,i-d,j-d),player):
                return True
        if (i>=0+d and i<=2+d) and (j>=3-d and j<=6-d):
            if contador3T(abajoIzq(tab,i-d,j+d),player):
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
    
def evaluar(tab,mv,fil,player):
    if conecta4(tab,mv,fil,player):
        return 4000 if player else -4000
    listC,c=movval(tab)
    listF=filCor(tab,listC,c)
    p=0
    for n in range(c):
        i,j=listF[n],listC[n]
        if conecta3T(tab,i,j,player):
            p+=1 if player else -1
        if conecta3T(tab,i,j,not player):
            p-=100 if player else -100
    return p

def generarArbol(tab,r,player,n):
    tope=4000 if player else -4000
    listm,c=movval(tab)
    for i in range(c):
        x=listm[i]
        rep,fil=insertar(tab,x,player)
        ptj=evaluar(rep,x,fil,player)
        if i==0:
            r.ha=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.ha,not player,n-1)
        elif i==1:
            r.hb=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.hb,not player,n-1)
        elif i==2:
            r.hc=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.hc,not player,n-1)
        elif i==3:
            r.hd=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.hd,not player,n-1)
        elif i==4:
            r.he=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.he,not player,n-1)
        elif i==5:
            r.hf=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.hf,not player,n-1)
        elif i==6:
            r.hg=raiz(x,ptj)
            if ptj!=tope and n>1:
                generarArbol(rep,r.hg,not player,n-1)
        borrar(rep,fil,x)

def centinela(tab,player):
    r=raiz()
    generarArbol(tab,r,player,5)
    m,p=r.minimax(player,5,True)
    return m

import numpy as np
tab=np.reshape([i*0 for i in range (42)], (6,7))
status=2
turno=False
mostrarTab(tab)
while status==2:
    listam,c=movval(tab)
    if turno:
        b=centinela(tab,turno)
        tab=insertar(tab,b,turno,v=True)
    else:
        b=centinela(tab,turno)
        tab=insertar(tab,b,turno,v=True)
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
from os import path

class Toplista():
    def __init__(self,pathx:str) -> None:
        self.map = []
        self.betoltve = False
        self.path = pathx

        def olvas(pathx):
            with open(pathx, 'r',encoding='UTF-8') as fajl:

                x = fajl.readlines()
                    
                for i in range(len(x)):
                    if x[i] == '' or x[i] == '\n':
                        x[i] == ''
                    if x[i].endswith('\n'): 
                        x[i] = x[i][0:len(x[i])-1]
                return x

        if path.exists(pathx):
            
            self.map = olvas(pathx)
        
        else:
            with open(pathx, 'w',encoding='UTF-8') as fajl:
                fajl.write('\n')

            self.map = olvas(pathx)

        y = []
        for x in self.map:
            try:
                act = x.split(',')

                if len(act) > 2: raise ValueError('A sor érvénytelen adat!')

                act[0] = int(act[0])

                print(act)

                assert(type(act[0])==int and type(act[1])==str)
                y.append((act[0],act[1]))
            except:print('Hibás sor!')
        
        self.map = y
    
    def __str__(self) -> str:
        ki = 'A legjobb pontok:\n'
        for i in range(len(self.map)):
            ki += f'{i+1}. {self.map[i][1]} - {self.map[i][0]}\n'
            if i >= 10: break
        return ki

    def listaki(self) -> list:
        ki = []
        for i in range(10):
            try:ki.append((self.map[i][0],self.map[i][1]))
            except:ki.append((-1,''))
        return ki

    def rendez(self):
        self.map = sorted(self.map, reverse=True, key=lambda x : x[0])

    def ment(self):
        with open(self.path,'w',encoding='UTF-8') as file:
            for x in range(len(self.map)):
                if x > 49:continue #maximum mentések korlátozása, a sor végén levő eredmények törlésre kerülnek
                file.write(f'{self.map[x][0]},{self.map[x][1]}\n')

    def beszur(self,adat:tuple[int,str]):

        if type(adat)!=tuple:raise ValueError('Ez nem tuple!')
        if len(adat)!=2: raise ValueError('Ez rossz adat.')
        if type(adat[0])!=int:raise ValueError('Első paraméter nem szám')
        if type(adat[1])!=str:raise ValueError('Második paraméter nem szöveg!')

        self.map.append(adat)
        self.rendez()
        self.ment()

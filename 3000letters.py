import re
#code
class amble_petzses3hk():
    def __init__(self):
        self.reeee=''
        self.q={}
        fn=input('put in file read')
        self.fread=open(fn,'r')
        print('provide grounds?')
    def threek_o(self):
        jerp=0
        butt=1
        ella = 2997
        challick = 0
        abc=0
        d=0
        sepia=''
        for chugga in str(self.fread.readlines()):
            sepia+=str(chugga)
            abc+=1
            if abc %3000 == 0:
                d+=1
        d+=1
        for i in sepia:
            challick+=1
            self.reeee+=i
            if challick == 0:
                jerp+=1
                print(jerp)
                self.reeee+=str(jerp)+':'+str(d)
            if challick % ella == 0:
                jerp+=1
                self.reeee+=str(jerp)+':'+str(d)
        
        print(jerp)
        return
    
    def dio_o(self):
        
        ella = 3000
        challick = 0
        jerp=0
        rgxp='[0-9]+:[0-9]+'
        for chugga in re.split(rgxp,self.reeee):
            jerp+=1
            self.q[jerp]=self.q.get(jerp,chugga)
        return
    
    def lland(self,term=True):
        while term:
            a=input('put in key ')
            print(self.q[int(a)])
            if a=='go now':
                print('goodbye')
                return
        if not term:
            fn = input('put in file to write one ')
            op = open(fn,'w')
            op.write(self.reeee)
        op.close()
        return
    
if __name__ == '__main__':
    #run code
    a = amble_petzses3hk()
    a.threek_o()
    a.dio_o()
    a.fread.close()
    a.lland(term=False)
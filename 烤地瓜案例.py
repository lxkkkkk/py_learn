class SweetPotato:
    def __init__(self):
        self.cook_time=0
        self.cook_state='生的'
        self.condiments=[]
    
    def cook(self,time):
        if(time<=0):
            print('无效值！')
        else:
            self.cook_time+=time
            if(self.cook_time>=0 and self.cook_time<3):
                self.cook_state='生的'
            elif(self.cook_time>=3 and self.cook_time<7):
                self.cook_state='半生不熟'
            elif(self.cook_time>=7 and self.cook_time<12):
                self.cook_state='熟了'
            else:
                self.cook_state='糊了'
    
    def add_condiment(self,condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'烘烤时间：{self.cook_time},地瓜状态：{self.cook_state},调料：{self.condiments}'
    
potato=SweetPotato()
print(f'原始地瓜状态：{potato}')

potato.cook(-1)

potato.cook(8)

potato.cook(30)
print(f'地瓜状态：{potato}')

potato.add_condiment('粑粑')
potato.add_condiment('辣椒')
print(f'地瓜状态：{potato}')
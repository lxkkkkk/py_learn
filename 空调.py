class AC:
    def cool(self):
        pass

    def hot(self):
        pass

    def swing(self):
        pass

class XiaoMi(AC):
    def cool(self):
        print('小米制冷技术，开始制冷')

    def hot(self):
        print('小米制热技术，开始制热')

    def swing(self):
        print('小米吹风技术，开始吹风')

class GeLi(AC):
    def cool(self):
        print('格力制冷技术，开始制冷')

    def hot(self):
        print('格力制热技术，开始制热')

    def swing(self):
        print('格力吹风技术，开始吹风')

xiaomi=XiaoMi()
geli=GeLi()

xiaomi.cool()
xiaomi.hot()
xiaomi.swing()
print('-'*80)
geli.cool()
geli.hot()
geli.swing()
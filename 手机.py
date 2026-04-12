class Phone:
    def open(self):
        print(f'{self}手机开机了')
    
    def close(self):
        print(f'{self}手机关机了')

    def take_photo(self):
        print(f'{self}手机拍照了')

p1=Phone()
print(f'p1对象：{p1}')
p1.open()
p1.close()
p1.take_photo()

print('-'*80)

p2=Phone()
print(f'p2对象：{p2}')
p2.open()
p2.close()
p2.take_photo()
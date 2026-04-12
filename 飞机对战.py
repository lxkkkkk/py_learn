class HeroFighter:
    def power(self):
        return 60
    
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
    
class EnemyFighter:
    def power(self):
        return 70
    
def object_play(hero,enemy):
    if hero.power()>=enemy.power():
        print('英雄机赢了！')
    else:
        print('英雄机败了！')
    
h1=HeroFighter()
e1=EnemyFighter()

object_play(h1,e1)

print('-'*80)

h2=AdvHeroFighter()

object_play(h2,e1)
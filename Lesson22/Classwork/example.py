# class Car(object):
#     def __init__(self, wheels):
#         self.wheels = wheels
# minicar = Car(4)
# minicar.wheels


from random import randrange
class Magic(object):
    DAMAGE_SPEC = 'DAMAGE'
    HEAL_SPEC = "HEAL"
    def __init__(self, source, spec):
        self.source = source
        self.spec = spec

    # def damage(self):
    #     if self.spec == self.DAMAGE_SPEC
    #         return self.spec
    #
    # def heal(self):
    #     if self.spec == self.HEAL_SPEC:
    #         return self.spec

    def get_spec(self):
        if self.spec == self.DAMAGE_SPEC:
            return "Is a damage specialization"
        elif self.spec == self.HEAL_SPEC:
            return "Is a hralse specialization"
        else:
            raise TypeError(f'Unknown spec, please choice this one {self.DAMAGE_SPEC} or {self.HEAL_SPEC}')

    def use(self):
        raise NotImplementedError()

class HealMagic(Magic):
    def use(self):
        return f'{self.get_spec()} was used from {self.source}'

class DamageMagic(Magic):
    def use(self):
        return f"{self.get_spec()} was used from {self.source}"

class FireMagic(DamageMagic):
    max_damage = 20
    def use(self):
        print(super().use())
        return f'{self.max_damage} damage from {self}'

    def __repr__(self):
        return f'this is {self.__class__.__name__} max_dmg: {self.max_damage}'

    def __call__(self, target):
        return f'{self.use()} to {target}'

class HolyMagic(HealMagic):
    max_heal = 20
    def use(self):
        print(super().use())
        return f'{self.max_heal} heal from {self}'

    def __repr__(self):
        return f'{self.__class__.__name__}-{self.source}'

class PriusMag(FireMagic, HolyMagic):
    @property
    def max_damage(self):
        return super().max_damage / 2

p = PriusMag(source='Imba magic', spec='DAMAGE')
h = HolyMagic(source='holy light', spec='HEAL')
f = FireMagic(source='fire', spec='DAMAGE')
b = FireMagic(source='bla bla', spec='DAMAGE')

print(f)
print(h)
print(b('VasyaSpirt'))
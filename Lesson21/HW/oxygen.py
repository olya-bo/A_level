class Element(object):
    def agg_state(self, t, scale='C'):
        t = round(self.convert_to_c(t, scale), 2)
        if t < self.t_solidification:
            return f'{t}°C - температура затвердивания'
        elif self.t_melting <= t < self.t_evaporation:
            return f'{t}°C - температура плавления'
        return f'{t}°C - температура испарения'

    def convert_to_c(self, t, scale='C'):
        if scale.upper() not in 'KFC':
            raise ValueError('Такой шкалы нет')
        if scale.upper() == 'K':
            return t - 273.15
        elif scale.upper() == "F":
            return (t - 32) * 5 / 9
        return t


class Oxygen(Element):
    t_solidification = 1538
    t_melting = 1538
    t_evaporation = 2862


test = Oxygen()
print(test.agg_state(1538, "f"))
l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
d = l * a
r = d / 2
print("Sua parede tem a dimensão de {}X{} e sua área é de {:.3f}m².".format(l, a, d))
print("Para pintar essa parede, você precisará de {}l de tinta.".format(r))
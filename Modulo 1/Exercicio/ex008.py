p = float(input("Uma distáncia em metros: "))
print("A medida de {} corresponde a {}km {}hm {}dam {}dm {:.0f}cm e {:.0f}mm".format(p, cm, mm))
km = p *
hm = p *
dam = p *
dm = p * 10
cm = p * 100
mm = p * 1000
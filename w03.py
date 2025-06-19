# BMI Calculator
#result = w / H^2 h*h

w = float(input("นน.(กก.)"))
h = int(input("สส. :(ซม.)"))

#r = w/((h/100)*(h/100))
r2 = w/((h/100)**2)
r3 = f"{r2:.3f}"

print(r3)


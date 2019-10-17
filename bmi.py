berat=float(input("Masukkan berat badan (kg) : "))
tinggi=float(input("Masukkan tinggi badan (m) : "))
bmi = berat/(tinggi**2)
if bmi < 18.5:
    print("Kekurangan berat badan")
elif bmi >=18.5 and bmi <=24.9:
    print("Ideal")
elif  bmi >=25 and bmi<=29.9:
    print("Kelebihan berat badan")
else:
    print("Kegemmukan(obesitas)")
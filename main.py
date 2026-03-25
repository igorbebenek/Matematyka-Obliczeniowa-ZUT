import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
np.set_printoptions(precision=15, suppress=False, formatter={'float': '{: .15e}'.format})

matplotlib.use('TkAgg')

#Zadanie 1
single = np.arange(1,10**6+1,dtype=np.float32)
double = np.arange(1,10**6+1,dtype=np.float64)
#A1 sum

suma_A1_single = 0.0
start = time.perf_counter()
for i in single:
    suma_A1_single += i

end = time.perf_counter()
print("A1 single: ", suma_A1_single, "Time: ", end - start, "seconds")

suma_A1_double = 0.0
start = time.perf_counter()
for i in double:
    suma_A1_double += i
end = time.perf_counter()
print("A1 double: ", suma_A1_double, "Time: ", end - start, "seconds")

#A2
start = time.perf_counter()
suma_A2_single = np.sum(single)
end = time.perf_counter()

print("A2 single: ", suma_A2_single, "Time: ", end - start, "seconds")

start = time.perf_counter()
suma_A2_double = np.sum(double)
end = time.perf_counter()
print("A2 double: ", suma_A2_double, "Time: ", end - start, "seconds")

#A3
def kahan(x):
    n = len(x)
    S = x[0]
    C = 0
    for i in range(1,n):
        Y = x[i] - C
        T = S +Y
        C = (T - S) - Y
        S = T
    return S

start = time.perf_counter()
suma_A3_single = kahan(single)
end = time.perf_counter()
print ("A3 single: ", suma_A3_single, "Time: ", end - start, "seconds")
start = time.perf_counter()

suma_A3_double = kahan(double)
end = time.perf_counter()
print ("A3 double: ", suma_A3_double, "Time: ", end - start, "seconds")

#A4
def gill_moler(x):
    n = len(x)
    S = 0
    U = 0
    P = 0
    for i in range(0,n):
        S = U+x[i]
        P = U - S + x[i] + P
        U = S
    S = S + P
    return S

start = time.perf_counter()
suma_A4_single = gill_moler(single)
end= time.perf_counter()
print("A4 single: ", suma_A4_single, "Time: ", end - start, "seconds")

start = time.perf_counter()
suma_A4_double = gill_moler(double)
end = time.perf_counter()
print("A4 double: ", suma_A4_double, "Time: ", end - start, "seconds")

def suma_ciagow(n):
    return n*(n+1)/2

n = 10 **6
print("Suma ciagow: ", suma_ciagow(n))

#Wykres i błąd

wzorzec = suma_ciagow(n)

blad = np.abs(np.array([wzorzec - suma_A1_single, wzorzec - suma_A2_single, wzorzec - suma_A3_single,wzorzec - suma_A4_single]))
plt.figure()
plt.bar(["A1", "A2", "A3","A4"], blad)
plt.title("Błąd dla pojedynczej precyzji")
plt.xlabel("Metoda")
plt.ylabel("Błąd")
plt.yscale("log")
plt.show()
#Zadanie 2
wektor_single = np.array([10**6,0.2,0.2,0.2,-10**6], dtype=np.float32)
wektor_double = np.array([10**6,0.2,0.2,0.2,-10**6], dtype=np.float64)

#A1
suma_B1_single = 0.0
suma_B1_double = 0.0

for i in wektor_single:
    suma_B1_single += i

print("B1 single: ", suma_B1_single)

for i in wektor_double:
    suma_B1_double += i

print("B1 double: ", suma_B1_double)

#A2
suma_B2_single = np.sum(wektor_single)
print("B2 single: ", suma_B2_single)
suma_B2_double = np.sum(wektor_double)
print("B2 double: ", suma_B2_double)

#A3
suma_B3_single = kahan(wektor_single)
print("B3 single: ", suma_B3_single)
suma_B3_double = kahan(wektor_double)
print("B3 double: ", suma_B3_double)
#A4
suma_B4_single = gill_moler(wektor_single)
print("B4 single: ", suma_B4_single)
suma_B4_double = gill_moler(wektor_double)
print("B4 double: ", suma_B4_double)

#Zad 2 blad i wykres
wzorzec_B = 0.6
blad_B = np.abs(np.array([wzorzec_B - suma_B1_single, wzorzec_B - suma_B2_single, wzorzec_B - suma_B3_single,wzorzec_B - suma_B4_single]))

plt.figure()
plt.bar(["B1", "B2", "B3","B4"], blad_B)
plt.title("Błąd dla pojedynczej precyzji")
plt.xlabel("Metoda")
plt.ylabel("Błąd")
plt.yscale("log")
plt.show()

#Zadanie 3
def f(x,y):
    return 9*x**4-y**4+2*y**2

def f1(x,y):
    return (3*x**2-y**2+1)*(3*x**2+y**2-1)+1

x = 40545
y = 70226

wynik0 = f1(x,y)
print("Zadanie 3 wynik0: ", wynik0)
x1 = np.int64(x)
y1 = np.int64(y)

wynik_1 = f1(x1,y1)
print("Zadanie 3 wynik1: ", wynik_1)

x2 = np.int32(x)
y2 = np.int32(y)
wynik_2 = f1(x2,y2)
print("Zadanie 3 wynik2: ", wynik_2)

x3 = np.float32(x)
y3 = np.float32(y)
wynik_3 = f1(x3,y3)
print("Zadanie 3 wynik3: ", wynik_3)







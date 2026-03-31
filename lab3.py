import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
import scipy.io
from scipy.linalg import lu
import sympy as sp
matplotlib.use('TkAgg')

#format jak long e
np.set_printoptions(precision=15, suppress=False, formatter={'float': '{: .15e}'.format})


#Zadanie 1
def gauss(A):
    A = A.copy().astype(float)
    n = A.shape[0]
    wyz = 1.0
    for i in range(n):
        temp = A[i, i]
        A[i, i:] = A[i, i:] / temp
        wyz = wyz * temp
        for j in range(i + 1, n):
            mnoznik = A[j, i]
            A[j, :] = A[j, :] - A[i, :] * mnoznik
    return wyz

# LICZENIE DLA WYMIARÓW MACIERZY


#ładowanie wygląda tak, bo był z nim problem, ale wczytuje poprawnie


mat = scipy.io.loadmat('A_5000.mat')
zmienne = [k for k in mat.keys() if not k.startswith('__')]

if len(zmienne) > 0:
    nazwa = zmienne[0]
    macierz_5000 = mat[nazwa]
    print(f"Sukces! Wczytano zmienną '{nazwa}' o wymiarach {macierz_5000.shape}")
else:
    print("Plik jest pusty lub nie zawiera zmiennych!")



start = time.perf_counter()
det_5000 = np.linalg.det(macierz_5000)
end = time.perf_counter()

print("Wyznacznik macierzy A_5000: ", det_5000)
print("Time: ", end - start, "seconds")

start = time.perf_counter()
wyz_gauss_5000 = gauss(macierz_5000)
end = time.perf_counter()
print("Wyznacznik macierzy A_5000(Gauss): ", wyz_gauss_5000)
print("Time: ", end - start, "seconds")

#===========================================================================================================================================================

#Zadanie 2
rozmiar = []
czasy = []

for i in range(1,2001,10):
    macierz = np.random.rand(i,i)
    start = time.perf_counter()
    det = np.linalg.det(macierz)
    end = time.perf_counter()
    t_wykonania = end - start
    rozmiar.append(i)
    czasy.append(t_wykonania)


    print(f"Rozmiar {i}x{i} | Wyznacznik: {det} | Czas: {end - start} s")

#2 polyfit, polyval i wykres
x = np.array(rozmiar)
y = np.array(czasy)
rzad = 4
wspolczynniki = np.polyfit(x, y, rzad)
linia_trendu = np.polyval(wspolczynniki, x)
plt.plot(x, y, 'o', label='Dane')
plt.plot(x, linia_trendu, 'r-', label=f'Linia trendu (rząd {rzad})')
plt.xlabel('Rozmiar macierzy (n x n)')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania obliczania wyznacznika w zależności od rozmiaru macierzy')
plt.legend()
plt.show()
#===========================================================================================================================================================

#Zadanie 3
A = np.array([[10**10,20], [5000,0]])
det = np.linalg.det(A)
if(det != 0):
    inv_A = np.linalg.inv(A)
    print("Macierz A jest odwracalna. Odwrotność:\n", inv_A)
    iloczyn = A @ inv_A
    wzorzec = np.eye(2)
    blad = wzorzec - iloczyn
    print("Iloczyn A i A^-1:\n", iloczyn)
    print("Błąd (wzorzec - iloczyn):\n", blad)


uwarunkowanie = np.linalg.cond(A)
print(f"Uwarunkowanie: {uwarunkowanie}")

#===========================================================================================================================================================
#Zadanie 4

#liczenie z numpy
B = np.array([[93190,151311,173403,7602],[1735541,3069840,3509949,153799],[3608434, 8910090, 10115414, 442533],[8815753, 26319961, 29835101, 1304521]])

start = time.perf_counter()
det_B = np.linalg.det(B)
end = time.perf_counter()
print(f"Wyznacznik macierzy B:{det_B}\n Czas: {end-start} ")

# Rozwiązanie problemu, wykorzystamy bibliotekę sympy

sympy_B = sp.Matrix([[93190,151311,173403,7602],[1735541,3069840,3509949,153799],[3608434, 8910090, 10115414, 442533],[8815753, 26319961, 29835101, 1304521]])
start = time.perf_counter()
wyznacznik_sympy = sympy_B.det()
end = time.perf_counter()
print(f"Wyznacznik macierzy B obliczony za pomocą sympy: {wyznacznik_sympy}.\nCzas: {end-start} ")



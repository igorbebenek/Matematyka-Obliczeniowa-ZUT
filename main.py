import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')
np.set_printoptions(precision=15, suppress=False, formatter={'float': '{: .15e}'.format})

#Zadanie 1

# def f1(x):
#     return x-np.sqrt(1+x*x)
#
# def f2(x):
#     return -1/(x+np.sqrt(1+x*x))
#
# def a_w1(x):
#     return np.sqrt(1+x*x)
#
# def a_w2(x):
#     return np.sqrt(1+x*x)
#
# k = np.arange(4,11,1)
#
# def w1(x,a):
#     return x-a
#
# def w2(x,a):
#     return -1/x+a
#
# x = 10**k
#
#
# a = a_w1(x)
#
# w1_double = x-a
# print("w1 double: ", w1_double)
#
# w2_double = -1/x+a
# print("w2 double: ", w2_double)





# def f1(x):
#     return x-np.sqrt(1+x*x)
#
# def f2(x):
#     return -1/(x+np.sqrt(1+x*x))
#
# def a_w1(x):
#     return np.sqrt(1+x*x)
#
# def a_w2(x):
#     return np.sqrt(1+x*x)
#
# k = np.arange(4,11,1,dtype=np.float32)
#
#
# def w1(x,a):
#     return x-a
#
# def w2(x,a):
#     return -1/x+a
#
# x = np.float32(10**k)
#
#
# a = a_w1(x)
#
# w1_single = np.float32(x-a)
# print("w1 single: ", w1_single)
#
# w2_single = -1/x+a
# print("w2 single: ", w2_single)



#Zadanie 2


d = 10**-3
x = np.linspace(2 - d, 2 + d, 1000)
def wielomian(x):
    (x-2)**4

def f1(x):
    return (x - 2)**4
def f2(x):
    return x*x*x*x-8*x*x*x+24*x*x-32*x+16


y1 = f1(x)
y2 = f2(x)



plt.figure(1)
plt.plot(x, y1, label='f1(x)')
plt.plot(x, y2, label='f2(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji')
plt.legend()
plt.grid(True)
plt.show()

blad = np.abs(y1 - y2)
print("Blad: ", np.max(blad))
etykiety = ['Błąd']

plt.figure()
plt.plot(x, blad , marker='o', color='red')
plt.xlabel('Błąd')
plt.ylabel('Wartość błędu')
plt.title('Błąd między f1(x) a f2(x)')
plt.grid(True)
plt.show()


#Zadanie 3

# f1=(np.sqrt(2)-1)**6
#
# f2 = 1 / (np.sqrt(2) + 1)**6
#
# f3 = (3-2*np.sqrt(2))**3
#
# f4 = 1/(3+2*np.sqrt(2))**3
#
# f5 = 99-70*np.sqrt(2)
#
# f6 = 1/(99+70*np.sqrt(2))
#
# tablica_funkcji = np.array([f2,f3,f4,f5,f6])
#
# print("Wszystkie przeksztalcenia", tablica_funkcji)
#
#
# tablica_bledow = np.abs(np.float64(f1) - tablica_funkcji)
#
# print("Bledy",tablica_bledow)
#
# etykiety = ['f2', 'f3', 'f4', 'f5', 'f6']
# plt.figure()
# plt.bar(etykiety, tablica_bledow, color='blue')
# plt.xlabel('Przeksztalcenia')
# plt.ylabel('Blad')
# plt.title("Błędy")
# plt.legend()
# plt.grid(True)
# plt.yscale('log')
# plt.show()


from Util import *
import BezierCurve
import matplotlib.pyplot as plt

print("""
 /$$$$$$$                      /$$                            /$$$$$$                                         
| $$__  $$                    |__/                           /$$__  $$                                        
| $$  \ $$  /$$$$$$  /$$$$$$$$ /$$  /$$$$$$   /$$$$$$       | $$  \__/ /$$   /$$  /$$$$$$  /$$    /$$ /$$$$$$ 
| $$$$$$$  /$$__  $$|____ /$$/| $$ /$$__  $$ /$$__  $$      | $$      | $$  | $$ /$$__  $$|  $$  /$$//$$__  $$
| $$__  $$| $$$$$$$$   /$$$$/ | $$| $$$$$$$$| $$  \__/      | $$      | $$  | $$| $$  \__/ \  $$/$$/| $$$$$$$$
| $$  \ $$| $$_____/  /$$__/  | $$| $$_____/| $$            | $$    $$| $$  | $$| $$        \  $$$/ | $$_____/
| $$$$$$$/|  $$$$$$$ /$$$$$$$$| $$|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/| $$         \  $/  |  $$$$$$$
|_______/  \_______/|________/|__/ \_______/|__/             \______/  \______/ |__/          \_/    \_______/
""")


# =====================================================
# Input data
# =====================================================

prompt_method_choice = """
Pilih metode input yang digunakan:
-------------------------------
| 1. From Keyboard            |
| 2. From File                |
-------------------------------

Pilihan metode: """
pilihan = int(input(prompt_method_choice))
if pilihan == 2:
    namaFile = "../test/" + input("Masukkan nama file: ")
    file = open(namaFile, 'r')

    nControl = int(file.readline())
    strList = file.readline().replace("(","").replace(")","").split(" ")
    iteration = int(file.readline())
else:
    nControl = int(input("Masukkan banyaknya titik kontrol: "))
    strList = [input(f"x{i+1},y{i+1} = ") for i in range(nControl)]
    iteration = int(input("Masukkan jumlah iterasi: "))

controlListTemp = [a.split(',') for a in strList]
controlList = [Point(float(a[0]), float(a[1])) for a in controlListTemp]

BezierCurve.BruteForce(nControl, controlList, iteration)
BezierCurve.DivideNConquer(nControl, controlList, iteration)

plt.legend()
plt.show()
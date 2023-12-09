import sys
import subprocess
import warnings
#n = int(sys.argv[1])
#print(n+1)
A = 123
B = 6

#cmd = f"python C:\\Users\\ohajd\Desktop\\pod.py {A} {B}"
#subprocess.call(cmd, shell=True)
#result = subprocess.check_output(cmd, shell=True)

#result_str = result.decode("utf-8")

#print(result_str)

for i in range(1000,10000000000):
    for j in range(2,11):
        cmd = f"python C:\\Users\\ohajd\Desktop\\pod.py {i} {j}"
        result = subprocess.check_output(cmd, shell=True)

        result_str = result.decode("utf-8")
        result_str = result_str.rstrip("\n")
        #print(result_str)
        cmd2 = f"python C:\\Users\\ohajd\Desktop\\brutal.py {i} {j}"
        result2 = subprocess.check_output(cmd2, shell=True)

        result_str2 = result2.decode("utf-8")
        result_str2 = result_str2.rstrip('\n')
        #print(result_str2)


        zmienna_do_zapisu = f"ciag: {i} dzielnik: {j} wynikMetoda: {result_str} wynikBrutal: {result_str2}"

        with open("C:\\Users\\ohajd\\Desktop\\wyniki.txt", "a") as plik:
            plik.write(zmienna_do_zapisu + "\n")

        if result!=result2 and i!=0:
            warnings.warn(f"WARN! {result}!={result2} for {i}, {j}")
            with open("C:\\Users\\ohajd\\Desktop\\wyniki.txt", "a") as plik2:
               plik2.write("^^^^^^^^^^ THERE IS ERROR" + "\n")
            exit()

        print(f"i: {i}, j: {j}")
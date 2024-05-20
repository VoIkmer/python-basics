HF = HDF = HA = ' '
a = 0
while HF != "FIM" and HDF != "FIM" and HA != "FIM":
    HF, HDF, HA = input().split()
    if HF == "NAO" and HDF == "SIM" and HA == "NAO":
        a = 1 
    

if a == 1:
    print("VITORIA")
else:
    print("DERROTA")
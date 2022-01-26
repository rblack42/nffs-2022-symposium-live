import CM

x = CM.x
y = CM.y

with open("CM.txt",'w') as fout:
    fout.write("name: arc3-CM\n")
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        fout.write(f"{xi} {yi}\n")
        i += 1

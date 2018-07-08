# -*- coding: cp1252 -*-.
import sys
import os


def main():
    print sys.version
    os.chdir(r"/Users/lluisgar16/Desktop/TFM/DATA")

    bbdd = open("BBDD_Preguntas_orales.csv", "rb").readlines()
    dic_diputados = {}
    codes = []
    for line in bbdd[1:]:
        fields = line.split(";")
        codes.append(fields[5].zfill(2))
        name = fields[1]
        if name[-1] == " ":
            name = name[:-1]
        if name not in dic_diputados.keys():
            dic_diputados[name] = (fields[4],[fields[5].zfill(2)])
        else:
            code_list = dic_diputados[name][1]
            dic_diputados[name] = (fields[4], code_list+[fields[5].zfill(2)])

    codes = sorted(list(set(codes)))
    csvlines = []
    line = "DIP;UNI;"
    for code in codes:
        line+=str(code)+";"
    line=line[:-1]
    csvlines.append(line)
    for diputado in dic_diputados.keys():
        line = diputado+";"+str(dic_diputados[diputado][0])+";"
        for code in codes:
            line += str(dic_diputados[diputado][1].count(code))+";"
        line = line[:-1]
        csvlines.append(line)

    with open("Codes_Vectors.csv", "wb") as csv:
        for line in csvlines:
            csv.write(line+"\n")

if __name__ == '__main__':
    main()
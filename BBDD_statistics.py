# -*- coding: cp1252 -*-.
import sys
import os


def main():
    print sys.version
    os.chdir(r"/Users/lluisgar16/Desktop/TFM/DATA")

    bbdd = open("BBDD_Preguntas_orales.csv", "rb").readlines()
    total_questions = len(bbdd)
    uni,no_uni = [0,0]
    for line in bbdd[1:]:
        fields = line.split(";")
        if int(fields[4]) == 1:
            uni+=1
        else:
            no_uni+=1

    print total_questions,uni,no_uni


if __name__ == '__main__':
    main()
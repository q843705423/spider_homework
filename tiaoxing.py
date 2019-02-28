from matplotlib import pyplot as plt
datasCpp = open("c++.txt").readlines()
datasJava =  open("java.txt").readlines()
str='-'
payListCpp = []
payListJava = []
print(len(datasCpp))
print(len(datasJava))
for i in range(len(datasCpp)):
    datasCpp[i].index(str)
    dataCpp = int(datasCpp[i][:datasCpp[i].index(str)])

    payListCpp.append(int(dataCpp/2000)*2000)

for i in range(len(datasJava)):
    datasJava[i].index(str)
    dataJava = int(datasJava[i][:datasJava[i].index(str)])
    payListJava.append(int(dataJava/2000)*2000)


def draw_hist(myList, Title, Xlabel, YLabel,Xmin,Xmax):
    plt.hist(myList, 100)
    plt.xlabel(Xlabel)
    plt.ylabel(YLabel)
    plt.xlim(Xmin, Xmax)
    # plt.ylim(Ymin, Ymax)
    plt.title(Title)
    plt.show()
print(payListCpp)
print(payListJava)
draw_hist(payListCpp," JAVA","Pay","number ",50,30000)
draw_hist(payListJava," C++","Pay","number ",50,30000)

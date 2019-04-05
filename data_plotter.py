from matplotlib import pyplot as plt

def plotter(dados):

    titulos = ['Flexões','Abdominais','Mergulhos','Agachamentos','Prancha']

    dias = [x+1 for x in range(7)]

    aux = 1
    fig = plt.figure()

    for j, i in enumerate(dados):
            print(dias,': ', dados[j])

    for j, i in enumerate(dados):
        plt.plot(dias, i, label = titulos[j])
        aux += 1

    plt.xlabel('Dias')
    plt.ylabel('Repetições')
    plt.legend()
    plt.show()

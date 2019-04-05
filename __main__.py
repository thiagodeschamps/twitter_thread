from data_catcher import catcher
from data_treatment import treatment
from data_plotter import plotter


def main():
    catcher()
    dados = treatment()
    plotter(dados)



if __name__ == '__main__':
    main()

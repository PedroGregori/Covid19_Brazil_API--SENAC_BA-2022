import os
import covid_api
op = 0

while op != 5:
    os.system('cls')
    print('::::::::::|Covid19 Brazil API|:::::::::::')
    print('[1] Casos em todos os estados brasileiros')
    print('[2] Casos por estado brasileiro ')
    print('[3] Casos no Brasil em data específica')
    print('[4] Consultar status da API')
    print('[5] Sair')
    op = int(input('O que deseja fazer?: '))
    
    os.system('cls')
    if op == 1:
        print('::::::::::::|Lista de Casos e Mortes Pelo Brasil|:::::::::::::')
        all = covid_api.getALL()
        for uf in all['data']:
            print(f"{uf['uf']} - Casos: {uf['cases']} - Mortes: {uf['deaths']}")
        
    elif op == 2:
        print('::::::::|Dados Por Estado Escolhido|::::::::|')
        uf = input('Digite a sigla do estado: ')
        state = covid_api.getState(uf)
        if 'error' in state.keys():
            print('Estado não encontrado')
        else:
            print('*********|Boletim Epidemiológico do Estado|*********')
            for k, v in state.items():
                print(f'{k} : {v}') 
    
    elif op == 3:
        print(':::::::::|Casos e Mortes em Data Especifica|:::::::::')
        print('Informe a data no formato AAAA/MM/DD')
        date = input('Digite a data: ')
        date2 = '/-'
        for i in date2:
            date = date.replace(i,'')
        time = covid_api.getDate(date)
        for dt in time['data']:
            print(f"{dt['uf']} - Casos: {dt['cases']} - Mortes: {dt['deaths']}")
            print(f"Data: {dt['datetime']}")
    
    elif op == 4:
        print('::::::::::::|Status da API|::::::::::::')
        status = covid_api.getStatus()
        for k, v in status.items():
            print(f'{k} : {v}') 
    input('Aperte ENTER para continuar')
print('Obrigado por usar o sistema :D')


import json

with open ("C:/Users/sasha/Downloads/log.json") as json_string:
    data = json.load(json_string)

    for key in data:
        if (data[str(key)]['uName'] == 'РЎРµСЂРІРµСЂ РЎР•Р’') and (data[str(key)]['serial'] == '01'): # Сервер CEB 01
            # Место обработки json
            print(data[str(key)]['Date']) 
            print(data[str(key)]['data']['system_SWAP_Used'])
            print(data[str(key)]['data']['system_SWAP_Total'] + '\n')

            print(data[str(key)]['data']['system_RAM_Used'])
            print(data[str(key)]['data']['system_RAM_Total'] + '\n')

            print(data[str(key)]['data']['system_Processes_Total'])
            print(data[str(key)]['data']['system_Processes_Stopped'])
            print(data[str(key)]['data']['system_Processes_Sleeping'])
            print(data[str(key)]['data']['system_Processes_Running'])
            print(data[str(key)]['data']['system_Processes_Zombie'])

            print(data[str(key)]['data']['system_LA1'].replace('.', ','))
            print(data[str(key)]['data']['system_LA5'].replace('.', ','))
            print(data[str(key)]['data']['system_LA15'].replace('.', ','))
            print(data[str(key)]['data']['system_IDLE'].replace('.', ','))

            print(data[str(key)]['data']['system_HDD_xvda1_Used'])
            print(data[str(key)]['data']['system_HDD_xvda1_Total'] + '\n')

            #print(data[str(key)]['data']['system_HDD_vg-root_Used'])
            #print(data[str(key)]['data']['system_HDD_vg-root_Total'] + '\n')

            """
            # Место обработки json
            print(data[str(f_key)]['Date']) 
            print('SWAP Used: ' + data[str(f_key)]['data']['system_SWAP_Used'])
            print('SWAP Total: ' + data[str(f_key)]['data']['system_SWAP_Total'])

            print('RAM Used: ' + data[str(f_key)]['data']['system_RAM_Used'])
            print('RAM Total: ' + data[str(f_key)]['data']['system_RAM_Total'])

            print('Proc. Total: ' + data[str(f_key)]['data']['system_Processes_Total'])
            print('Proc. Stopped: ' + data[str(f_key)]['data']['system_Processes_Stopped'])
            print('Proc. Sleeping: ' + data[str(f_key)]['data']['system_Processes_Sleeping'])
            print('Proc. Running: ' + data[str(f_key)]['data']['system_Processes_Running'])
            print('Proc. Zombie: ' + data[str(f_key)]['data']['system_Processes_Zombie'])

            print('LA1: ' + data[str(f_key)]['data']['system_LA1'])
            print('LA5: ' + data[str(f_key)]['data']['system_LA5'])
            print('LA15: ' + data[str(f_key)]['data']['system_LA15'])
            print('IDLE: ' + data[str(f_key)]['data']['system_IDLE'])

            print('HDD (xvda1) Used: ' + data[str(f_key)]['data']['system_HDD_xvda1_Used'])
            print('HDD (xvda1) Total: ' + data[str(f_key)]['data']['system_HDD_xvda1_Total'] + '\n')
                """




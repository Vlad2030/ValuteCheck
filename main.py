import modules.api
import modules.valute
import modules.install

try:
    import requests
    import json
    import sys
except Exception:
    print('ImportError! Installing...')
    modules.install.installModules(file='requirements.txt"')

def main() -> None:
    print(
'''
=========================================================
 _   _       _       _       _____ _               _    
| | | |     | |     | |     /  __ \ |             | |   
| | | | __ _| |_   _| |_ ___| /  \/ |__   ___  ___| | __
| | | |/ _` | | | | | __/ _ \ |   | '_ \ / _ \/ __| |/ /
\ \_/ / (_| | | |_| | ||  __/ \__/\ | | |  __/ (__|   < 
 \___/ \__,_|_|\__,_|\__\___|\____/_| |_|\___|\___|_|\_\\
=========================================================
Welcome to the ValuteCheck tool!

Available valutes: AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF,
HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY, MDL, NOK, PLN,
RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR,
KRW, JPY.

(1) Check valute.
(2) Exit.
'''
)
    while True:
        choice = input('Choose option: ')
        if choice == '1':
            valute_choice = input('Choose valutes: ')
            modules.valute.showValute(valute_choice)
        elif choice == '2':
            print('Bye!')
            sys.exit()
        else:
            print('TypeError: try again!')

if __name__ == '__main__':
    main()
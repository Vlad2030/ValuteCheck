import modules.api

def getId(valute):
    return modules.api.json_data['Valute'][valute]['ID']

def getNumCode(valute):
    return modules.api.json_data['Valute'][valute]['NumCode']

def getCharCode(valute):
    return modules.api.json_data['Valute'][valute]['CharCode']

def getNominal(valute):
    return modules.api.json_data['Valute'][valute]['Nominal']

def getName(valute):
    return modules.api.json_data['Valute'][valute]['Name']

def getValue(valute):
    return modules.api.json_data['Valute'][valute]['Value']

def getPrevious(valute):
    return modules.api.json_data['Valute'][valute]['Previous']

def getTrend(self):
    if getValue(valute=self) < getPrevious(valute=self):
        return "↓"
    elif getValue(valute=self) > getPrevious(valute=self):
        return "↑"

def showValute(self):
    print(
f'''
==========================={self}===========================
ID: {getId(valute=self)}
NumCode: {getNumCode(valute=self)}
CharCode: {getCharCode(valute=self)}
Nominal: {getNominal(valute=self)}
Name: {getName(valute=self)}
Value: {getValue(valute=self)}₽ {getTrend(self)}
Previous: {getPrevious(valute=self)}₽
'''
    )

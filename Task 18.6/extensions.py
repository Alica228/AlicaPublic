import requests, json, pymorphy2

class APIException(Exception):
    pass

class Rates():
    def __init__(self):
        morph = pymorphy2.MorphAnalyzer()
        self.AllCurrenciesRates = json.loads(requests.get(f"https://api.exchangeratesapi.io/latest?base=RUB").content)['rates']
        self.allCurrenciesNames = {
			"PHP" : [word[0].upper() for word in morph.parse('песо')[0].lexeme],
			"HUF" : [word[0].upper() for word in morph.parse('форинт')[0].lexeme],
			"RON" : [word[0].upper() for word in morph.parse('лей')[0].lexeme],
			"BRL" : [word[0].upper() for word in morph.parse('реал')[0].lexeme],
			"RUB" : [word[0].upper() for word in morph.parse('рубль')[0].lexeme],
			"HRK" : [word[0].upper() for word in morph.parse('куна')[0].lexeme],
			"JPY" : [word[0].upper() for word in morph.parse('иена')[0].lexeme],
			"THB" : [word[0].upper() for word in morph.parse('бат')[0].lexeme],
			"CHF" : [word[0].upper() for word in morph.parse('франк')[0].lexeme],
			"EUR" : [word[0].upper() for word in morph.parse('евро')[0].lexeme],
			"PLN" : [word[0].upper() for word in morph.parse('злотый')[0].lexeme],
			"BGN" : [word[0].upper() for word in morph.parse('лев')[0].lexeme],
			"TRY" : [word[0].upper() for word in morph.parse('лира')[0].lexeme],
			"CNY" : [word[0].upper() for word in morph.parse('жэньминьби')[0].lexeme],
			"ZAR" : [word[0].upper() for word in morph.parse('рэнд')[0].lexeme],
			"USD" : [word[0].upper() for word in morph.parse('доллар')[0].lexeme],
			"ILS" : [word[0].upper() for word in morph.parse('шекель')[0].lexeme],
			"GBP" : [word[0].upper() for word in morph.parse('фунт')[0].lexeme],
			"KRW" : [word[0].upper() for word in morph.parse('вона')[0].lexeme],
			"MYR" : [word[0].upper() for word in morph.parse('ринггит')[0].lexeme]
		}

    def get_price(self, base, quote, amount):
        base = self.FitUnder(base) if self.FitUnder(base) else base
        if base not in self.AllCurrenciesRates.keys(): raise APIException(f"Не знаю такой валюты: \"{base}\"")
        quote = self.FitUnder(quote) if self.FitUnder(quote) else quote
        if quote not in self.AllCurrenciesRates.keys(): raise APIException(f"Не знаю такой валюты: \"{quote}\"")
        try:
            return f"{amount} {base} = {float(amount)*float(self.AllCurrenciesRates[quote])/float(self.AllCurrenciesRates[base]):.4f} {quote}"
        except ValueError:
            raise APIException(f"Не похоже на число: \"{amount}\"")

    def FitUnder(self, word):
        for key in self.allCurrenciesNames.keys():
            if word in self.allCurrenciesNames[key]:
                return key
        return None
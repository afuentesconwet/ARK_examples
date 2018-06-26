import arky.rest
arky.rest.use("ark")

#GET Account information of a given address
a = arky.rest.GET.api.accounts(address="AeLpRK8rFVtBeyBVqBtdQpWDfLzaiNujKr")

#GET Delegate information of a given name
b = arky.rest.GET.api.delegates.get(username="genesis_1", returnKey="delegate")

#GET All transactions
c = arky.rest.GET.api.transactions()

#GET All unconfirmed transactions
d = arky.rest.GET.api.transactions.unconfirmed()

#print(a)
#print(b)
#print(c)


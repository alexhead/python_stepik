
#capital = "London is the capital of Great Britain"
#template = '{1} is the capital of {0}'
#print(template.format("London", "Great Britain"))
#print(template.format("Vaduz", "Lichtenstein"))
#print(template.format.__doc__)

#template = '{capital} is the capital of {country}'
#print(template.format(capital="London", country="Great Britain"))


#import requests
#template = "Response from {0.url} with code {0.status_code}"

#res = requests.get("https://docs.python.org/3.5/")
#print(template.format(res))

#res = requests.get("https://docs.python.org/3.5/random")
#print(template.format(res))


from random import random
x = random()
print(x)
print("{:.3}".format(x))
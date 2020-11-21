from bs4 import BeautifulSoup
import requests

keyword = input("Keyword? ")
source = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={keyword}&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_BIN=1&_samilow=&_samihi=&_sadis=15&_stpos=66085&_sargn=-1%26saslc%3D1&_salic=1&_sop=12&_dmd=1&_ipg=50&LH_Complete=1&_fosrp=1').text
soup = BeautifulSoup(source, 'lxml')
#result(s)
results = soup.find_all('span',class_ = 'bold bidsold')

#parser(s)

i = 1
while i <= 5:
    print(results[i])
    i += 1

# for result in results:
#   if x < 3:
#     print(result.prettify())
#     x += 1

# i = 1
# while i <= 100:
#     print("Today is Sunday")
#     i += 1
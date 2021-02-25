from bs4 import BeautifulSoup
import requests

def getQueryMercadoLibre(query, category=None):
    page = requests.get(f'https://lista.mercadolivre.com.br/{query}#D[A:{query}]').text

    if category:
        if category == 'geladeira':
            page = requests.get(f'https://lista.mercadolivre.com.br/eletrodomesticos/geladeiras-freezers').text
        elif category == 'celular':
            page = requests.get(f'https://celulares.mercadolivre.com.br/#menu=categories').text
        elif category == 'tv':
            page = requests.get(f'https://eletronicos.mercadolivre.com.br/televisores/#menu=categories').text

    soup = BeautifulSoup(page, 'lxml')

    product_list = soup.findAll('ol', class_='ui-search-layout')
    all_products = list()
    verify_product = list()
    products = dict()

    if len(product_list) == 1:
        for c in product_list[0].findAll('li'):
            products = dict()
            # GET LINK PRODUCT
            if c.find('a', class_='ui-search-link'):
                products['link'] = c.find('a', class_='ui-search-link')['href']
                verify_product.append(products['link'])
            # GET NAME PRODUCT

            img = c.find('img')
            if img:
                products['description'] = img.get('alt')
                # GET IMAGE PRODUCT
                if img.get('data-src'):
                    products['photo'] = img.get('data-src')

            if c.find('span', class_='price-tag'):
                priceTag = c.find('span', class_='price-tag')
                price = None
                # GET PRICE PRODUCT

                price = priceTag.find('span', class_='price-tag-symbol').text + " "
                price += priceTag.find('span', class_='price-tag-fraction').text
                if priceTag.find('span', class_='price-tag-decimal-separator'):
                    price += priceTag.find('span', class_='price-tag-decimal-separator').text
                if priceTag.find('span', class_='price-tag-cents'):
                    price += priceTag.find('span', class_='price-tag-cents').text

                products['price'] = price
                all_products.append(products)

    else:
        for c in product_list:
            products = dict()
            # GET NAME PRODUCT
            products['description'] = c.find('li').find('img')['alt']
            # GET LINK PRODUCT
            products['link'] = c.findAll('li')[0].find('a', class_='ui-search-link')['href']
            verify_product.append(products['link'])
            # GET IMAGE PRODUCT
            products['photo'] = c.findAll('li')[0].find('img')['data-src']

            priceTag = c.findAll('li')[0].find('span', class_='price-tag')
            price = None
            # GET PRICE PRODUCT

            price = priceTag.find('span', class_='price-tag-symbol').text + " "
            price += priceTag.find('span', class_='price-tag-fraction').text
            if priceTag.find('span', class_='price-tag-decimal-separator'):
                price += priceTag.find('span', class_='price-tag-decimal-separator').text
            if priceTag.find('span', class_='price-tag-cents'):
                price += priceTag.find('span', class_='price-tag-cents').text

            products['price'] = price
            all_products.append(products)

    return all_products


def getQueryBuscape(query, category=None):
    link = 'https://www.buscape.com.br'

    page = requests.get(f'{link}/search?q={query}').text

    if category:
        if category == 'geladeira':
            page = requests.get(f'{link}/geladeira').text
        elif category == 'celular':
            page = requests.get(f'{link}/celular/smartphone').text
        elif category == 'tv':
            page = requests.get(f'{link}/tv').text

    soup = BeautifulSoup(page, 'lxml')

    all_products = list()
    verify_product = list()
    product = dict()

    product_list = soup.find('div', class_='SearchPage_SearchList__HL7RI')

    if product_list:
        for c in product_list.find_all('div', class_='card'):
            product = dict()
            product['description'] = c.find('a', class_='name')['title']
            product['link'] = link + c.find('a', class_='name')['href']
            product['photo'] = c.find('img')['src']
            product['price'] =  c.find('a', class_='price').find('span', class_='mainValue').text +  c.find('a', class_='price').find('span', class_='centsValue').text

            product['merchant'] = None
            if c.find('a', class_='merchantName'):
                product['merchant'] = {'merchantName': c.find('a', class_='merchantName')['text'],
                                       'merchantLink': link + c.find('a', class_='merchantName')['href']}
            all_products.append(product)
        return all_products



print(getQueryMercadoLibre('televisor'))
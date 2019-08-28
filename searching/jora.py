from bs4 import BeautifulSoup
from .position import Position
from .filters import apply_filters


def j_format_urls(location):
    urls = []
    cities = j_city_for_url(location)
    i = 1
    for city in cities:
        while (i < 51):
            if i == 1:
                URL = f'https://au.jora.com/j?q=&l={city}&button=&sp=search'
            else:
                URL = f'https://au.jora.com/j?button=&l={city}&p={i}&q=&sp=search&surl=0&tk=iZV51kgxeKDufsHC4G7g'
            urls.append(URL)
            i += 1
    return urls


                      
def j_format_positions(soup, search_keywords, avoid_keywords, isfulltime, isparttime, iscasual):
    positions_to_render = []    
    # current_page = 0
    # try:
    #     current_page = int(soup.find('div', class_='pagination').em.text)
    # except AttributeError:
    #     current_page = 0

    positionRows = soup.find_all("li", class_="result")
    
    # if i == current_page:
    for position in positionRows:
        title = position.find("a", class_="jobtitle").get_text()
        description = position.find("div", class_="summary").get_text()
        employer = ''
        try:
            employer = position.find("span", class_="company").get_text()
        except AttributeError:
            employer = ''
        posted = position.find("span", class_="date").get_text()
        location = position.find("span", class_="location").get_text()
        url = position.find('a', class_="jobtitle").get('href')
        full_url = f'https://au.jora.com{url}'
        
        jora_position = Position(title,description,location,posted,'',full_url, 'Jora')
        position_to_render = apply_filters(jora_position, search_keywords, avoid_keywords)
        if position_to_render:
            positions_to_render.append(position_to_render)
    
    # else:
    #     results_end = True
    return positions_to_render


def j_city_for_url(dropboxText):
    if dropboxText == 'All Australia':
        return ([''])

    if dropboxText == 'ATC':
        return (['ACT'])
    if dropboxText == '- Camberra':
        return (['Canberra+ACT'])

    if dropboxText == 'NSW':
        return (['NSW'])
    if dropboxText == '- Sydney':
        return (['Sydney+NSW'])
    if dropboxText == '- Newcastle':
        return (['Newcastle+NSW'])
    if dropboxText == '- Central Coast':
        return (['Central+Coast+NSW'])
    if dropboxText == '- Lismore':
        return (['Lismore+NSW'])
    if dropboxText == '- Wollongong':
        return (['Wollongong+NSW'])
    if dropboxText == '- Tweed Heads':
        return (['Tweed+heads+NSW'])
    if dropboxText == '- Wagga Wagga':
        return (['Wagga+Wagga+NSW'])
    if dropboxText == '- Goulburn':
        return (['Goulburn+NSW'])
    if dropboxText == '- Bathurst-Orange region':
        return (['Orange+NSW'])
    if dropboxText == '- South Coast NSW':
        return (['South+Coast+NSW'])
    if dropboxText == '- Coffs Harbour':
        return (['Coffs+Harbour+NSW'])
    if dropboxText == '- Port Macquarie':
        return (['Port+Macquarie+NSW'])
    if dropboxText == '- Dubbo':
        return (['Dubbo+NSW'])
    if dropboxText == '- Tamworth':
        return (['Tamworth+NSW'])
    if dropboxText == '- Armidale':
        return (['Armidale+NSW'])
    if dropboxText == '- Cooma':
        return (['Cooma+NSW'])
    if dropboxText == '- Broken Hill':
        return (['Broken+Hill+NSW'])

    if dropboxText == 'NT':
        return (['NT'])
    if dropboxText == '- Darwin':
        return (['Darwin+NT'])

    if dropboxText == 'QLD':
        return (['QLD+'])
    if dropboxText == '- Brisbane':
        return (['Brisbane+QLD'])
    if dropboxText == '- Gold Coast':
        return (['Gold+Coast+QLD'])
    if dropboxText == '- Sunshine Coast':
        return (['Sunshine+Coast+QLD'])
    if dropboxText == '- Cairns':
        return (['Cairns+QLD'])
    if dropboxText == '- Toowoomba':
        return (['Toowoomba+QLD'])
    if dropboxText == '- Townsville':
        return (['Townsville+QLD'])
    if dropboxText == '- Hervey Bay':
        return (['Hervey+Bay+QLD'])
    if dropboxText == '- Ipswich':
        return (['Ipswich+QLD'])
    if dropboxText == '- Mackay':
        return (['Mackay+QLD'])
    if dropboxText == '- Rockhampton':
        return (['Rockhampton+QLD'])
    if dropboxText == '- Central QLD':
        return (['Mount+Isa+QLD','Camooweal+QLD','Cloncurry+QLD','Maxwelton+QLD','Bedourie+QLD','Winton+QLD','Hughenden+QLD','McKinlay+QLD','Tambo+QLD','Longreach+QLD','Cunnamulla+QLD','Augathella+QLD','Eromanga+QLD'])

    if dropboxText == 'SA':
        return  (['SA'])
    if dropboxText == '- Adelaide':
        return  (['Adelaide+SA'])
    if dropboxText == '- Port Augusta':
        return  (['Port+Augusta+SA'])
    if dropboxText == '- Mt Gambier':
        return  (['Mount+Gambier+SA'])
    if dropboxText == '- Port Lincoln':
        return  (['Port+Lincoln+SA'])

    if dropboxText == 'TAS':
        return  (['TAS'])
    if dropboxText == '- Hobart':
        return  (['Hobart+TAS'])
    if dropboxText == '- Launceston':
        return  (['Launceston+TAS'])
    if dropboxText == '- Scottsdale':
        return  (['Scottsdale+TAS'])
    if dropboxText == '- Branxholm':
        return  (['Brantholm+TAS'])
    if dropboxText == '- Bridport':
        return  (['Bridport+TAS'])
    if dropboxText == '- Meander Valley':
        return  (['Meander+Valley+TAS'])
    if dropboxText == '- Devonport':
        return  (['Devonport+TAS'])
    if dropboxText == '- Burnie':
        return  (['Burnie+TAS'])
    if dropboxText == '- Central Coast':
        return  (['Central+Coast+TAS'])
    if dropboxText == '- Circular Head':
        return  (['Circular+Head+TAS'])
    if dropboxText == '- Kentish':
        return  (['Kentish+TAS'])
    if dropboxText == '- Latrobe':
        return  (['Latrobe+TAS'])
    if dropboxText == '- Waratah':
        return  (['Waratah+TAS'])
    if dropboxText == '- West Coast':
        return  (['West+Coast+TAS'])


    if dropboxText == 'VIC':
        return  (['VIC'])
    if dropboxText == '- Melbourne':
        return  (['Melbourne+VIC'])
    if dropboxText == '- Geelong':
        return  (['Geelong+VIC'])
    if dropboxText == '- LaTrobe':
        return  (['Latrobe+VIC'])
    if dropboxText == '- Bendigo':
        return  (['Bendigo+VIC'])
    if dropboxText == '- Shepparton':
        return  (['Shepparton+VIC'])
    if dropboxText == '- Ballarat':
        return  (['Ballarat+VIC'])
    if dropboxText == '- Mildura':
        return  (['Mildura+VIC'])
    if dropboxText == '- Warrnambool':
        return  (['Warrnambool+VIC'])
    if dropboxText == '- Wodonga':
        return  (['Wodonga+VIC'])
    if dropboxText == '- Horsham':
        return  (['Horsham+VIC'])

    if dropboxText == 'WA':
        return  (['WA'])
    if dropboxText == '- Perth':
        return  (['Perth+WA'])
    if dropboxText == '- Bunbury':
        return  (['Bunbury+WA'])
    if dropboxText == '- Broome':
        return  (['Broome+WA'])
    if dropboxText == '- Northam':
        return  (['Northam+WA'])
    if dropboxText == '- Albany':
        return  (['Albany+WA'])
    if dropboxText == '- Carnarvon':
        return  (['Carnarvon+WA'])
    if dropboxText == '- Kalgoorlie':
        return  (['Kalgoorlie+WA'])
    if dropboxText == '- Geraldton':
        return  (['Geraldton+WA'])
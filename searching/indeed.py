from bs4 import BeautifulSoup
from .position import Position
from .filters import apply_filters  


def i_format_urls(location):
    cities = i_city_for_url(location)
    urls = []
    i = 0
    for city in cities:
        while (i < 500):
            URL = f'https://au.indeed.com/jobs?q=&l={city}&sort=date&limit=50&radius=50&start={i}'
            urls.append(URL)
            i += 10
    return urls


def i_format_positions(soup, words_to_search, words_to_avoid, fulltime, parttime, casual):
    positions_to_render = []

    # results_end = False         #TODO - 
    # while (not results_end):    #TODO - 

    result_table = soup.find("td", id="resultsCol")
    # looking for for the postion rows in table  by the div class doesnt seam to work..
    # alternatively, it gets all divs and filters by its divs class title, description...
    divs = result_table.find_all("div")

    # get pagination div to look for the last page of results. It stops looking for positions when it gets to the last page or 50th
    # first page previous_next = ['Next >>'] 
    # from second on previous_next = ['<< Previous', 'Next >>']
    # last page previous_next = ['<< Previous']
    # div_pagination = result_table.find("div", class_="pagination") #TODO - 
    # previous_next = div_pagination.find_all("span", class_="np")   #TODO - 
    
    # if (len(previous_next) == 2) or ('Next' in previous_next[0].get_text()):  #TODO - 
    for div in divs:
        try:
            title_div = div.find('div', class_='title')
            title = title_div.get_text()
            url_a = title_div.a['href']
            url = f'https://au.indeed.com/{url_a}'
            description = div.find('div', class_='summary').get_text()
            posted = div.find('span', class_='date').get_text()
            location = div.find('span', class_='location').get_text()
            #TODO: see if show company as optional or not
            #company = div.find('span', class_='company').get_text()
            indeed_position = Position(title,description,location,posted,'',url, 'Indeed')
            position_to_render = apply_filters(indeed_position, words_to_search, words_to_avoid)

            if position_to_render:
                positions_to_render.append(position_to_render)
            
        except AttributeError:
            pass 
    # else:                     #TODO - 
    #     results_end = True    #TODO - 
    return positions_to_render


def i_city_for_url(dropboxText):
    if dropboxText == 'All Australia':
        return (['Australia'])

    if dropboxText == 'ATC':
        return (['Australian+Capital+Territory'])
    if dropboxText == '- Camberra':
        return (['Canberra+ACT'])

    if dropboxText == 'NSW':
        return (['New+South+Wales'])
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
        return (['Northern+Territory'])
    if dropboxText == '- Darwin':
        return (['Darwin+NT'])

    if dropboxText == 'QLD':
        return (['Queensland'])
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
        return  (['South+Australia'])
    if dropboxText == '- Adelaide':
        return  (['Adelaide+SA'])
    if dropboxText == '- Port Augusta':
        return  (['Port+Augusta+SA'])
    if dropboxText == '- Mt Gambier':
        return  (['Mount+Gambier+SA'])
    if dropboxText == '- Port Lincoln':
        return  (['Port+Lincoln+SA'])

    if dropboxText == 'TAS':
        return  (['Tasmania'])
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
        return  (['Victoria'])
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
        return  (['Western+Australia'])
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
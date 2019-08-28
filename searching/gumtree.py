from bs4 import BeautifulSoup
from .position import Position
from .filters import apply_filters, apply_job_type


def g_format_urls(location):
    (location_url, city_id) = g_city_for_url(location)
    urls = []
    resultPageNumber = ''
    i = 1
    while i < 51:
        if i > 1:
            resultPageNumber = f'page-{i}/'
        URL = f'https://www.gumtree.com.au/s-jobs/{location_url}{resultPageNumber}c9302l{city_id}?ad=offering'
        urls.append(URL)
        i += 1
    return urls

    
def g_format_positions(soup, search_keywords, avoid_keywords, isfulltime, isparttime, iscasual):
    positions_to_render = []
    positionRow = soup.find_all("a", class_="user-ad-row")
    for row in positionRow:
        rowTitle = row.p.get_text()
        description =''
        try:
            description = row.find("p", class_="user-ad-row__description user-ad-row__description--regular").get_text()
        except AttributeError:
            try: 
                description = row.find("p", class_="user-ad-row__description user-ad-row__description--premium").get_text()
            except AttributeError:
                description = ''    
        
        location = row.find("span", class_="user-ad-row__location-area").get_text()
        date_posted = row.find("p", class_="user-ad-row__age").get_text()
        attributes = row.find_all("li", class_="user-ad-attributes__attribute")
        attributes_str = []
        for a in attributes:
            att = a.get_text()
            attributes_str.append(att)

        positionURL = row['href']
        fullPositionURL = f'https://www.gumtree.com.au{positionURL}'

        gumtree_position = Position(rowTitle, description, location, date_posted, attributes_str, fullPositionURL, 'Gumtree')
        position_job_type = apply_job_type(gumtree_position, isfulltime, isparttime, iscasual)

        if position_job_type:
            position_to_render = apply_filters(gumtree_position, search_keywords, avoid_keywords)
            if position_to_render:
                positions_to_render.append(position_to_render)

    return positions_to_render


def g_city_for_url(dropboxText):
    if dropboxText == 'All Australia':
        return ('', '')

    if dropboxText == 'ATC':
        return ('act/', '3008838')
    if dropboxText == '- Camberra':
        return ('canberra/', '3002977')

    if dropboxText == 'NSW':
        return ('nsw/', '3008839')
    if dropboxText == '- Sydney':
        return ('sydney/', '3003435')
    if dropboxText == '- Newcastle':
        return ('newcastle/', '3003104')
    if dropboxText == '- Central Coast':
        return ('central-coast-nsw/', '3002327')
    if dropboxText == '- Lismore':
        return ('lismore/', '3002856')
    if dropboxText == '- Wollongong':
        return ('wollongong/', '3004782')
    if dropboxText == '- Tweed Heads':
        return ('tweed-heads/', '3002140')
    if dropboxText == '- Wagga Wagga':
        return ('wagga-wagga/', '3004502')
    if dropboxText == '- Goulburn':
        return ('goulburn/', '3004550')
    if dropboxText == '- Bathurst-Orange region':
        return ('bathurst-orange/', '3002746')
    if dropboxText == '- South Coast NSW':
        return ('south-coast-nsw/', '3004257')
    if dropboxText == '- Coffs Harbour':
        return ('coffs-harbour/', '3002445')
    if dropboxText == '- Port Macquarie':
        return ('port-macquarie/', '3004152')
    if dropboxText == '- Dubbo':
        return ('dubbo/', '3002599')
    if dropboxText == '- Tamworth':
        return ('tamworth/', '3004397')
    if dropboxText == '- Armidale':
        return ('armidale/', '3002057')
    if dropboxText == '- Cooma':
        return ('cooma/', '3002563')
    if dropboxText == '- Broken Hill':
        return ('broken-hill/', '3002302')

    if dropboxText == 'NT':
        return ('nt/', '3008840')
    if dropboxText == '- Darwin':
        return ('darwin/', '3004863')

    if dropboxText == 'QLD':
        return ('qld/', '3008841')
    if dropboxText == '- Brisbane':
        return ('brisbane/', '3005721')
    if dropboxText == '- Gold Coast':
        return ('gold-coast/', '3006035')
    if dropboxText == '- Sunshine Coast':
        return ('sunshine-coast/', '3006273')
    if dropboxText == '- Cairns':
        return ('cairns/', '3004937')
    if dropboxText == '- Toowoomba':
        return ('toowoomba/', '3006427')
    if dropboxText == '- Townsville':
        return ('townsville/', '3006693')
    if dropboxText == '- Hervey Bay':
        return ('hervey-bay/', '3005249')
    if dropboxText == '- Ipswich':
        return ('ipswich/', '3005501')
    if dropboxText == '- Mackay':
        return ('mackay/', '3005608')
    if dropboxText == '- Rockhampton':
        return ('rockhampton/', '3006115')
    if dropboxText == '- Central QLD':
        return ('central-qld/', '3005170')

    if dropboxText == 'SA':
        return ('sa/', '3008842')
    if dropboxText == '- Adelaide':
        return ('adelaide/', '3006878')
    if dropboxText == '- Port Augusta':
        return ('port-augusta/', '3007614')
    if dropboxText == '- Mt Gambier':
        return ('mt-gambier/', '3006819')
    if dropboxText == '- Port Lincoln':
        return ('port-lincoln/', '3007701')

    if dropboxText == 'TAS':
        return ('tas/', '3008843')
    if dropboxText == '- Hobart':
        return ('hobart/', '3000211')
    if dropboxText == '- Launceston':
        return ('launceston/', '3000435')
    if dropboxText == '- Scottsdale':
        return ('scottsdale-launceston/', '3000419')
    if dropboxText == '- Branxholm':
        return ('branxholm-launceston/', '3000409')
    if dropboxText == '- Bridport':
        return ('bridport-launceston/', '3000410')
    if dropboxText == '- Meander Valley':
        return ('meander-valley/', '3000463')
    if dropboxText == '- Devonport':
        return ('devonport-burnie-devonport/', '3000154')
    if dropboxText == '- Burnie':
        return ('burnie-burnie-devonport/', '3000101')
    if dropboxText == '- Central Coast':
        return ('central-coast/', '3000122')
    if dropboxText == '- Circular Head':
        return ('circular-head/', '3000139')
    if dropboxText == '- Kentish':
        return ('kentish/', '3000164')
    if dropboxText == '- Latrobe':
        return ('latrobe-burnie-devonport/', '3000183')
    if dropboxText == '- Waratah':
        return ('waratah/', '3000189')
    if dropboxText == '- West Coast':
        return ('west-coast/', '3000204')

    if dropboxText == 'VIC':
        return ('vic/', '3008844')
    if dropboxText == '- Melbourne':
        return ('melbourne/', '3001317')
    if dropboxText == '- Geelong':
        return ('geelong/', '3000884')
    if dropboxText == '- Latrobe':
        return ('la-trobe/', '3001067')
    if dropboxText == '- Bendigo':
        return ('bendigo/', '3000748')
    if dropboxText == '- Shepparton':
        return ('shepparton/', '3001814')
    if dropboxText == '- Ballarat':
        return ('ballarat/', '3000616')
    if dropboxText == '- Mildura':
        return ('mildura/', '3001274')
    if dropboxText == '- Warrnambool':
        return ('warrnambool/', '3001965')
    if dropboxText == '- Wodonga':
        return ('wodonga/', '3000525')
    if dropboxText == '- Horsham':
        return ('horsham/', '3000981')

    if dropboxText == 'WA':
        return ('wa/', '3008845')
    if dropboxText == '- Perth':
        return ('perth/', '3008303')
    if dropboxText == '- Bunbury':
        return ('bunbury/', '3007919')
    if dropboxText == '- Broome':
        return ('broome/', '3007868')
    if dropboxText == '- Northam':
        return ('northam/', '3008661')
    if dropboxText == '- Albany':
        return ('albany/', '3007764')
    if dropboxText == '- Carnarvon':
        return ('carnarvon/', '3008083')
    if dropboxText == '- Kalgoorlie':
        return ('kalgoorlie/', '3008248')
    if dropboxText == '- Geraldton':
        return ('geraldton/', '3008139')


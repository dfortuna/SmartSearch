from flask import Flask, render_template, request
import searching
import asyncio

app = Flask(__name__)

dropbox_cities = ['All Australia','All ATC','- Camberra','All NSW','- Sydney','- Newcastle','- Central Coast','- Lismore','- Wollongong','- Tweed Heads','- Wagga Wagga','- Goulburn','- Bathurst-Orange region','- South Coast NSW','- Coffs Harbour','- Port Macquarie','- Dubbo','- Tamworth','- Armidale','- Cooma','- Broken Hill','All NT','- Darwin','All QLD','- Brisbane','- Gold Coast','- Sunshine Coast','- Cairns','- Toowoomba','- Townsville','- Hervey Bay','- Ipswich','- Mackay','- Rockhampton','- Central QLD','All SA','- Adelaide','- Port Augusta','- Mt Gambier','- Port Lincoln','All TAS','- Hobart','- Launceston','- Scottsdale','- Branxholm','- Bridport','- Meander Valley','- Devonport','- Burnie','- Central Coast','- Circular Head','- Kentish','- Latrobe','- Waratah','- West Coast','All VIC','- Melbourne','- Geelong','- Latrobe','- Bendigo','- Shepparton','- Ballarat','- Mildura','- Warrnambool','- Wodonga','- Horsham','All WA','- Perth','- Bunbury','- Broome','- Northam','- Albany','- Carnarvon','- Kalgoorlie','- Geraldton']
positions    = []

@app.route("/")
def main():
    return render_template('index.html', cities=dropbox_cities)\

@app.route("/help")
def getHelpPage():
    return render_template('help.html')\

@app.route("/find-Jobs", methods=['POST'])
def findJobsButton():
    search_for = request.form['search-for']
    avoiding = request.form['avoiding']
    location = request.form['location']
    fulltime = request.form.get("fulltime") != None
    parttime = request.form.get("parttime") != None
    casual = request.form.get("casual") != None
    gumtree = request.form.get("gumtree") != None
    indeed = request.form.get("indeed") != None
    jora = request.form.get("seek") != None

    # find User-Agent of current browser for Beautiful Soup 
    # user_agent =  request.user_agent.string
    # HEADERS = {"User-Agent":f"{user_agent}"}

    # create a words array from words in text field that were separated by commas
    words_to_search = format_text_field(search_for)
    words_to_avoid = format_text_field(avoiding)

    positions_to_render = searching.search(gumtree, jora, indeed, words_to_search, words_to_avoid, location, fulltime, parttime, casual)
    return render_template('results.html', positions=positions_to_render)\
    
    
def format_text_field(text_n_commas):
    txt_commas_upper = text_n_commas.upper()
    no_commas = txt_commas_upper.split(',')
    if no_commas[0] == '':
        return []
    else:
        return no_commas


if __name__ == "__main__":
    app.run()
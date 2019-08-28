class Position:       
    def __init__(self, title, description, location, posted, attributes, url, source):
        self.title = title
        self.title_upper = title.upper()
        
        self.description = description
        self.description_upper = description.upper()

        self.location = location
        self.posted = posted
        
        self.attributes = attributes
        self.attributes_upper = []
        for a in attributes:
            a_upper = a.upper()
            self.attributes_upper.append(a_upper)

        self.url = url

        self.source = source
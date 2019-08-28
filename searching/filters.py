def apply_filters(position, search_keywords, search_avoiding_words):
    position_to_render = ''      
    if len(search_keywords) != 0:
        for keyword in search_keywords:
            if (keyword in position.title_upper) or (keyword in position.description_upper) or (keyword in position.attributes_upper):
                position_to_render = apply_avoiding_filter(position, search_avoiding_words)
    else:
        position_to_render = apply_avoiding_filter(position, search_avoiding_words)    

    return position_to_render


def apply_avoiding_filter(position, search_avoiding_words):
    # If no 'avoinding words', postion returns to be rendered
    # if the 'avoiding word', is not in Title, Description or Attributes, reads next word
    # if 'avoiding word' is found, the loop stops
    if len(search_avoiding_words) != 0:    
        print('apply_avoiding_filter')    
        for av_word in search_avoiding_words:
            print('avoid word: ', av_word)
            if (av_word in position.title_upper) or (av_word in position.description_upper) or (av_word in position.attributes_upper):
                print('AVOIDED!')
                return None
    return position


def apply_job_type(position, isfulltime, isparttime, iscasual):

    #if all selected or none selected 
    if (isfulltime and isparttime and iscasual) or (not isfulltime and not isparttime and not iscasual):
        return position

    #if fulltime and parttime selected
    elif isfulltime and isparttime:
        if ('Full-time' in position.attributes) or ('Part-time' in position.attributes):
            return position

    #if fulltime and casual selected
    elif isfulltime and iscasual:
        if ('Full-time' in position.attributes) or ('Casual' in position.attributes):
            return position

    #if parttime and casual selected
    elif isparttime and iscasual:
        if ('Part-time' in position.attributes) or ('Casual' in position.attributes):
            return position

    #if only fulltime selected                   
    elif isfulltime:
        if ('Full-time' in position.attributes):
            return position                   
    
    #if only partime selected
    elif isparttime:
        if ('Part-time' in position.attributes):
            return position
    else:
        #if only casual selected
        if ('Casual' in position.attributes):
            return position
    
    #if everything above fails:
    return None
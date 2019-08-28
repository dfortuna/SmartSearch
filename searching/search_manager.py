import asyncio
import aiohttp
import async_timeout
from time import perf_counter                       #test
from bs4 import BeautifulSoup
from .gumtree import g_format_urls, g_format_positions
from .jora import j_format_urls, j_format_positions
from .indeed import i_format_urls, i_format_positions

async def get_url(URL):
    async with aiohttp.ClientSession() as session:
        # async with async_timeout.timeout(30):             #TODO - timeout(10)
        try:                                          #TODO - try?
            async with session.get(URL) as response:
                return await response.text()
        except Exception as e:
            print(URL)
            print(e)
            return None
                

starting_time = 0.0
async def append_tasks(URLS, loop):
    tasks = []
    for url in URLS:
        page_content = loop.create_task(get_url(url))
        tasks.append(page_content)
    await asyncio.wait(tasks)
    return tasks 


def event_loop_for_URLS(URLS):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        start_tasks = perf_counter()   #test
        tasks = loop.run_until_complete(append_tasks(URLS, loop))
        finish_tasks = perf_counter()  #test
        print()
        print('**************************************************************')
        print('tasks downloaded in ', finish_tasks - start_tasks, ' seconds')
        loop.close()
        return tasks
    except:
        return None


def format_urls_for_requests(gumtree, jora, indeed, location):
    urls = []
    if gumtree:
        gumtree_urls = g_format_urls(location)
        urls += gumtree_urls
    if jora:
        jora_urls = j_format_urls(location)
        urls += jora_urls
    if indeed:
        indeed_urls = i_format_urls(location)
        urls += indeed_urls
    return urls
    

def search(gumtree, jora, indeed, words_to_search, words_to_avoid, location, fulltime, parttime, casual):
    
    urls = format_urls_for_requests(gumtree, jora, indeed, location)
    tasks = event_loop_for_URLS(urls)
    positions = []
    format_tasks = perf_counter()
    for task in tasks:
        task_result = task.result()

        #TODO - Beautiful Soup should not be here. Get the url requested in the task and do the next validations by it
        soup = BeautifulSoup(task_result, 'html.parser')
        title = soup.find('head').find('title').get_text()

        if 'Gumtree' in title:
            gumtree_position = g_format_positions(soup, words_to_search, words_to_avoid, fulltime, parttime, casual)
            if gumtree_position:
                positions += gumtree_position

        if ('Gumtree' not in title) and ('Jora' not in title):
            indeed_positions = i_format_positions(soup, words_to_search, words_to_avoid, fulltime, parttime, casual)
            if indeed_positions:
                positions += indeed_positions

        if 'Jora' in title:
            jora_positions = j_format_positions(soup, words_to_search, words_to_avoid, fulltime, parttime, casual)
            if jora_positions:
                positions += jora_positions
    format_tasks_end = perf_counter()
    print()
    print ('finishing' , format_tasks_end - format_tasks, 'seconds *****')                               
    print('**************************************************************')
    print()

    return positions

# def delete_comp(array, word):
#     message = False
#     time_start = time.time()
#     try:
#         array.remove(word)
#         message = True
#     except ValueError:
#         message = False
#     time_finish = time.time()
#     return (message, array, time_start, time_finish)

# if thing in some_list: some_list.remove(thing)

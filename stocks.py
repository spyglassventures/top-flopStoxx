from selenium import webdriver
import time
import pandas as pd

from IPython import embed


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(executable_path=r"C:\dev\chromedriver83.04.exe")

#week
nasdaq_w = 'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=325104&TIME_SPAN=W1'
dax_w = 'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=W1'
dax_d = 'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=INTRADAY'


urls = [
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=325104&TIME_SPAN=W1',   # Fehler
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=W1',
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=INTRADAY', # p1 dax gut
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=323547&TIME_SPAN=INTRADAY', # p1 mdax gut
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=324724&TIME_SPAN=INTRADAY', # ?? p2
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=193736&TIME_SPAN=INTRADAY', # p1 gut
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=92866&TIME_SPAN=INTRADAY', #p2
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=324965&TIME_SPAN=INTRADAY', # ?? p1 bad
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=1555183&TIME_SPAN=INTRADAY' # p2
        ]

#driver.get(nasdaq_w)

import os
#os.remove("C:\Users\Praxis\PycharmProjects\scraper\stocks.txt")
try:
    os.remove("stocks.txt")
    print("File Removed!")
except:
    pass


for url in urls:
    driver.get(url)

    # each element in seperate columns
    content_list = []
    content_list = driver.find_elements_by_class_name("table__column--top")

    names = content_list[1::8]
    prices = content_list[2::8]
    changes = content_list[3::8]

    df_names = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in names:
        #print (i.text)
        df_names.append(i.text)
    print ("........................................")





    df_prices = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in prices:
        #print (i.text)
        df_prices.append(i.text)
    #print ("........................................")


    df_changes = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in changes:
        #print (i.text)
        df_changes.append(i.text)
    #print ("........................................")


    df_names = pd.DataFrame(df_names)
    df_prices = pd.DataFrame(df_prices)
    df_changes = pd.DataFrame(df_changes)

    result = pd.concat([df_names, df_changes, df_prices], axis=1, sort=False)
    result.columns = ['___________________________', '_________', '_________']

    print(result.head(5))
    print(result.tail(5))
    # Append-adds at last
    file1 = open(r'C:\Users\Praxis\PycharmProjects\scraper\stocks.txt', "a")  # append mode
    file1.write(('\n'))
    file1.write(('\n'))
    file1.write("BEST PERFORMER")
    file1.write(('\n'))
    file1.write(result.head(5).to_string())
    file1.write(('\n'))
    file1.write(('\n'))
    file1.write("WORST PERFORMER")
    file1.write(('\n'))
    file1.write(result.tail(5).to_string())
    file1.close()
    #embed()



###############


urls = [
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=325104&TIME_SPAN=W1',   # Fehler
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=W1',
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=20735&TIME_SPAN=INTRADAY', # p1 dax gut
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=323547&TIME_SPAN=INTRADAY', # p1
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=324724&TIME_SPAN=INTRADAY', # gut
    #'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=193736&TIME_SPAN=INTRADAY', p1
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=92866&TIME_SPAN=INTRADAY', # p2 Austria gut
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=324965&TIME_SPAN=INTRADAY',
    'https://www.comdirect.de/inf/aktien/topflop/topflop.html?ID_NOTATION_INDEX=1555183&TIME_SPAN=INTRADAY' # p2 SMI gut
        ]

#driver.get(nasdaq_w)

for url in urls:
    driver.get(url)

    # each element in seperate columns
    content_list = []
    content_list = driver.find_elements_by_class_name("table__column--top")

    names = content_list[1::7]
    prices = content_list[2::7]
    changes = content_list[3::7]

    df_names = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in names:
        #print (i.text)
        df_names.append(i.text)
    print ("........................................")



    df_prices = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in prices:
        #print (i.text)
        df_prices.append(i.text)
    #print ("........................................")


    df_changes = []
    #print (" ########### BEST PERFORMER TODAY ###########")
    for i in changes:
        #print (i.text)
        df_changes.append(i.text)
    #print ("........................................")


    df_names = pd.DataFrame(df_names)
    df_prices = pd.DataFrame(df_prices)
    df_changes = pd.DataFrame(df_changes)

    result = pd.concat([df_names, df_changes, df_prices], axis=1, sort=False)
    result.columns = ['___________________________', '_________', '_________']

    print(result.head(5))
    print(result.tail(5))
    # Append-adds at last
    file1 = open(r'C:\Users\Praxis\PycharmProjects\scraper\stocks.txt', "a")  # append mode
    file1.write(('\n'))
    file1.write(('\n'))
    file1.write("BEST PERFORMER")
    file1.write(('\n'))
    file1.write(result.head(5).to_string())
    file1.write(('\n'))
    file1.write(('\n'))
    file1.write("WORST PERFORMER")
    file1.write(('\n'))
    file1.write(result.tail(5).to_string())
    file1.close()





driver.close()

#embed()

#
# df_content = pd.DataFrame(content_list)
# df_content
#
#
# row_list = [];
# row_list = driver.find_elements_by_class_name("table__row")
#
# df_row = pd.DataFrame(row_list)
# df_row

# df = pd.DataFrame(content_list)

# Loop to get text from Top
#print (" ########### BEST PERFORMER TODAY ###########")
#for i in content_list[0:25]:
#    print (i.text)
#print ("........................................")

# Loop to get text from Bottom
#print (" ########### WORST PERFORMER TODAY ###########")
#for i in content_list[(len(content_list)-23):len(content_list)]:
#    print (i.text)

# Less
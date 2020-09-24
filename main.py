from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

def count_articles(filter_field, value):
    reader = CSV_Manager(“./articles.csv”)
    articles = reader.get_csv_as_dicts()
    counter =0
    key = filter_field
    for article in articles:
        if article[key]==value:
            counter = counter+1
    return int(counter)
    
def is_article(filter_field, value):
    reader = CSV_Manager(“./articles.csv”)
    articles = reader.get_csv_as_dicts()
    status = False
    key = filter_field
    for article in articles:
        if article[key]==value:
            status = True
    return bool(status)    

def longest_article(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    del articles[0]
    filtered_articles = filter_CSV(filter_field, value)
    lng_article = filtered_articles[0]
    for article in filtered_articles:
        if article["pages"] > lng_article["pages"]:
            lng_article = article       
    return lng_article        


# print("Articles with a title of t4:")
# print(filter_CSV("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(filter_CSV("author", "a1"))
print(longest_article("author", "a1"))

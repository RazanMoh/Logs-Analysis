# "Database code" for the DB Forum.

import psycopg2


def get_most_popular_three_articles():
    """This Query returns the most popular three articles of all time."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT articles.title, count( * ) FROM articles,"
              " log WHERE log.path = CONCAT( '/article/', articles.slug) "
              " GROUP BY articles.title ORDER BY count( * ) DESC LIMIT 3 ")
    articles = c.fetchall()
    db.close()
    print('----- The most popular three articles of all time -----')
    print('#####################################################')
    for article in articles:
        print('"{title}" --> {count} views'.format(title=article[0],
              count=article[1]))
    print()
    return


def get_most_popular_three_article_authors():
    """This Query returns the most popular three article authors of all time"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT authors.name, count(*) FROM authors, articles, log "
              "WHERE log.path = CONCAT('/article/', articles.slug) AND "
              "authors.id=articles.author GROUP BY authors.name ORDER BY "
              "count(*) DESC LIMIT 3")
    authors = c.fetchall()
    db.close()
    print('----- The most popular article authors of all time -----')
    print('#####################################################')
    for author in authors:
        print('"{name}" --> {count} views'.format(name=author[0],
              count=author[1]))
    return


def get_all_days_did_more_than_1_of_requests_lead_to_errors():
    """This Query returns the days did more"""
    """than 1% of requests lead to errors."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from (select total.day, round(cast((error.hits*100) "
              "as numeric) /cast(total.hits as numeric), 3) as errors from "
              "(select date(time) as day,count(*) as hits from log group by "
              "day) as total inner join (select date(time) as day, count(*) "
              "as hits from log where status = '404 NOT FOUND' group by day) "
              "as error on total.day = error.day) as ans where errors > 1.0")
    days = c.fetchall()
    db.close()
    print('----- The days did more than 1% of requests lead to errors. -----')
    print('#####################################################')
    for day in days:
        print('"{date}" --> {count} error'.format(date=day[0],
              count=day[1]))
    print()
    return

if __name__ == "__main__":
    get_most_popular_three_articles()
    get_most_popular_three_article_authors()
    get_all_days_did_more_than_1_of_requests_lead_to_errors()

#!/usr/bin/env python3
import psycopg2


def q1():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''SELECT articles.title,
       count(*) AS number_of_views
FROM articles,
     log
WHERE log.path='/article/' || articles.slug
GROUP BY articles.title
ORDER BY number_of_views DESC
LIMIT 3''')
    posts = c.fetchall()
    db.close()
    return posts


def q2():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''SELECT authors.name,
       count(log.path) AS VIEWS
FROM authors,
     log,
     articles
WHERE log.path='/article/' || articles.slug
  AND authors.id=articles.author
GROUP BY authors.name
ORDER BY VIEWS DESC;''')
    posts = c.fetchall()
    db.close()
    return posts


def q3():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
#     # CREATE VIEW up AS
# SELECT date(log.time)AS date,
#        count(status) AS cnt
# FROM log
# WHERE status LIKE '404 NOT FOUND'
# GROUP BY date
#     # CREATE VIEW down AS
# SELECT date(log.time) AS date,
#        count(status) AS cnt
# FROM log
# GROUP BY date
#     # CREATE VIEW error AS
# SELECT down.date,
#        CAST(up.cnt AS FLOAT)*100/down.cnt AS errorperc
# FROM up,
#      down
# WHERE up.date=down.date
# ORDER BY errorperc
    c.execute('''SELECT *
FROM error
WHERE errorperc > 1''')
    posts = c.fetchall()
    db.close()
    return posts


if __name__ == '__main__':

    # this is to prevent executing
    # the code when imported, ignore.
    answer1 = q1()
    print('Q1: What are the most popular three articles of all time?')
    for article in enumerate(answer1):
        print('name: %s - views %d' % (article[1][0], article[1][1]))
    print('\n')

    answer2 = q2()
    print('Q2: Who are the most popular authors of all time?')
    for author in enumerate(answer2):
        print('name: %s - views %d' % (author[1][0], author[1][1]))
    print('\n')

    answer3 = q3()
    print('Q3: Which days have errors exceeding 1%?')
    for error in enumerate(answer3):
        print('day: %s - error percentage %f' % (error[1][0], error[1][1]))
    print('\n')

    print('The End')


else:
    print('importing...')

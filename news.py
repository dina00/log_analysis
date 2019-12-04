import psycopg2

def q1():
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select articles.title , count(*) as number_of_views from articles,log where log.path='/article/' || articles.slug group by articles.title order by number_of_views desc limit 3")
  posts = c.fetchall()
  db.close()
  return posts

def q2():
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select authors.name , count(log.path) as views from authors,log, articles where log.path='/article/' || articles.slug and authors.id=articles.author group by authors.name order by views desc;")
  posts = c.fetchall()
  db.close()
  return posts

def q3():
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  #create view up as select date(log.time)as date,count(status) as cnt from log where status like '404 NOT FOUND' group by date
  #create view down as select date(log.time) as date,count(status) as cnt from log group by date
  #create view error as select down.date ,CAST(up.cnt as FLOAT)*100/down.cnt as errorperc from up,down where up.date=down.date order by errorperc")
  c.execute("select * from error where errorperc>1")

  posts = c.fetchall()
  db.close()
  return posts


answer1=q1()
print('Q1: What are the most popular three articles of all time?')
for article in enumerate(answer1):
  print('name: %s - views %d' % (article[1][0], article[1][1]))

answer2=q2()
print('Q2: Who are the most popular authors of all time?')
for author in enumerate(answer2):
  print('name: %s - views %d' % (author[1][0], author[1][1]))

answer3=q3()
print('Q3: Which days have errors exceeding 1%?')
for error in enumerate(answer3):
  print('day: %s - error percentage %f' % (error[1][0], error[1][1]))

print('The End')

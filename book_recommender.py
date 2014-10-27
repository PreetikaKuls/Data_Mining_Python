import math

file = open("/Users/preetikataly/Documents/Courses/Mining Massive Data Sets/Recommender Systems/BX-CSV-Dump/BX-Book-Ratings.csv")
#ratings = file.read()
head = file.readlines(10)
#print head

#ratings = pandas.DataFrame(columns = ['UserID', 'ISBN', 'Rating'])
user_ratings = {}
#book = {}
i = 0
for line in file:
    #print "Entered line"
    line = line.replace('"', '')
    (user, ISBN, rating) = line.split(";")
    rating = float(rating)
    if rating == 0.0:
        continue
    if user in user_ratings: 
        user_ratings[user][ISBN] = rating     
    else:
        user_ratings[user] = {ISBN: rating}
    #print user_ratings[user]
    i = i + 1


file.close
book_file = open("/Users/preetikataly/Documents/Courses/Mining Massive Data Sets/Recommender Systems/BX-CSV-Dump/BX-Books.csv")

head = book_file.readlines(10)
#print head
book_info = {}

for line in book_file:
    line = line.replace('"', '')
    ISBN, title = line.split(";") [0:2]
    #print ISBN, title
    if ISBN not in book_info:
        book_info[ISBN] = title
count = 0

       
def norm_ratings(user_ratings):
   for user in user_ratings:
       total = 0
       count = 0
       user_avg = 0
       count = sum(1 for ISBN in user_ratings[user] if user_ratings[user][ISBN] != 0.0)
       total = sum(user_ratings[user][ISBN] for ISBN in user_ratings[user] if user_ratings[user][ISBN] != 0)
       if (count != 0):
           user_avg = total/count
       for ISBN in user_ratings[user]:
           user_ratings[user][ISBN] = user_ratings[user][ISBN] - user_avg
     
           
norm_ratings(user_ratings)


def cosine_sim(user_ratings, userA, userB):
    (dotAB, magA, magB) = 0, 0, 0
    for ISBN, ratingA in user_ratings[userA].iteritems():
          magA = magA + ratingA**2
          if ISBN in user_ratings[userB]:
              dotAB = dotAB + ratingA*user_ratings[userB][ISBN]
    for ISBN, ratingB in user_ratings[userB].iteritems():
            magB = magB + ratingB**2
    magA = math.sqrt(magA)
    magB = math.sqrt(magB)
    if(magA != 0 and magB != 0):
        simAB = dotAB/(magA*magB)
    else:
        simAB = 0
    return simAB    


def find_similar(user_ratings, userA):
    similarities = {}
    recommend = {}
    results = {}
    for user in user_ratings:  
        if(user == userA):
            continue
        sim = cosine_sim(user_ratings, userA, user)
        if(sim <= 0):
            continue
        
        for ISBN, rating in user_ratings[user].iteritems():
            if ISBN in user_ratings[userA].iteritems():
                continue
            
            recommend.setdefault(ISBN, 0)
            similarities.setdefault(ISBN, 0)
            recommend[ISBN] += rating*sim
            similarities[ISBN] += sim
            
    for ISBN in recommend:
        results[ISBN] = recommend[ISBN]/similarities[ISBN]
    results = sorted(results.items(), key = lambda x:x[1], reverse = True)
    return results[0:10]
    
    
def find_avgsimilar(user_ratings, userA):
    similarities = {}
    recommend = {}
    results = {}
    for user in user_ratings:  
        if(user == userA):
            continue
        sim = cosine_sim(user_ratings, userA, user)
        if(sim <= 0):
            continue
        
        for ISBN, rating in user_ratings[user].iteritems():
            if ISBN in user_ratings[userA].iteritems():
                continue
            
            recommend.setdefault(ISBN, 0)
            similarities.setdefault(ISBN, 0)
            recommend[ISBN] += rating*sim
            similarities[ISBN] += sim
            
    for ISBN in recommend:
        results[ISBN] = recommend[ISBN]/similarities[ISBN]
    results = sorted(results.items(), key = lambda x:x[1], reverse = True)
    return results[0:10]
    
def print_recommendations(results, book_info):
    ISBN = [x[0] for x in results]
    print ISBN
    for val in ISBN:
        print book_info[val]
        
output = find_similar(user_ratings, "243879")
print print_recommendations(output, book_info)
            
"""for user in user_ratings:
    count = 0
    total = 0
    for ISBN in user_ratings[user]:
        if user_ratings[user][ISBN] != 0.0:
            total = total + user_ratings[user][ISBN]
            count = count  + 1
            
    #print count
    
count = sum(1 for user in user_ratings for ISBN in user_ratings[user] if user_ratings[user][ISBN] != 0.0)
total = sum(user_ratings[user][ISBN] for user in user_ratings for ISBN in user_ratings[user] if user_ratings[user][ISBN] != 0)
#print total/count
# print book_info"""  


"""            #print cosine_sim(user_ratings, userA, user)
            result.append((user, cosine_sim(user_ratings, userA, user)))
    
    result = sorted(result, key = lambda x:x[1], reverse = True)
    return result[0:20]
            
mylist = find_similar(user_ratings, "243879")
print mylist
for user in mylist:
    for ISBN in user_rankings[user].iteritems():
        if ISBN not in user_rankings[me].iteritems():
        """


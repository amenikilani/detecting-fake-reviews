from __future__ import division
from sklearn.metrics.pairwise import cosine_similarity
from pandas.io.json import json_normalize
import pandas 
from pandas.io.json import json_normalize
import numpy as np

data = [
	{
		"reviewerID": "A1YJEY40sssYUW4SE",
		"asin": "7806397051",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "Very oily and creamy. Not at all what I expected... ordered this to try to highlight and contour and it just looked awful!!! Plus, took FOREVER to arrive.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391040000,
		"reviewTime": "01 30, 2014"
	},
{
		"reviewerID": "A1YJEYhhh40YUW4SE",
		"asin": "7806397053",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391044444,
		"reviewTime": "02 30, 2014"
	},
{
		"reviewerID": "A1jjjYJEY40YjjSE",
		"asin": "7806397051",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391044444,
		"reviewTime": "02 30, 2014"
	},
	{
		"reviewerID": "A60XNB876KllljjYML",
		"asin": "7806397051",
		"reviewerName": "Jessica H.",
		"helpful": [1,1],
		"reviewText": "This palette was a decent price and I was looking for a few different shades.",
		"overall": 3,
		"summary": "OK Palette!",
		"unixReviewTime": 1397779200,
		"reviewTime": "04 18, 2014"
	},
{
		"reviewerID": "A60ddXNB8jjj7kkk6KYML",
		"asin": "7806397051",
		"reviewerName": "Jessica H.",
		"helpful": [1,1],
		"reviewText": "This palette was a decent price and I was looking for a few other shades",
		"overall": 3,
		"summary": "OK Palette!",
		"unixReviewTime": 1397779600,
		"reviewTime": "05 18, 2014"
	},
	{
		"reviewerID": "A3G6XNM2ddddd40RMWA",
		"asin": "7806397052",
		"reviewerName": "Karen",
		"helpful": [1],
		"reviewText": "The texture of this concealer pallet is fantastic, it has great coverage and a wide variety of uses, I guess it's meant for professional makeup artists and a lot of the colours are of no use to me but I use at least two of them on a regular basis, and two more occasionally, which is the only reason I'm giving it for stars, I feel like the range of colors is kind of a waste for me, but the  product itself  is wonderful, it's not cakey, gives me a natural for and concealed my imperfections, therefore I highly recommend it :)",
		"overall": 4,
		"summary": "great quality",
		"unixReviewTime": 1378425600,
		"reviewTime": "09 6, 2013"
	},
	{
		"reviewerID": "A1YJEY4jjjjj0YUdddW4SE",
		"asin": "7806397052",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "Very oily and creamy. Not at all what I expected... ordered this to try to highlight and contour and it just looked awful!!! Plus, took FOREVER to arrive.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391040000,
		"reviewTime": "01 30, 2014"
	},
{
		"reviewerID": "A1YJEY4jjjj0YUW4Sfddd",
		"asin": "7806397052",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391044444,
		"reviewTime": "02 30, 2014"
	},
{
		"reviewerID": "A1YJEdddY40YjjjjjjUW4SE",
		"asin": "7806397052",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 1,
		"summary": "Don't waste your money",
		"unixReviewTime": 1391044444,
		"reviewTime": "02 30, 2014"
	},
	{
		"reviewerID": "A60XNddddB87kkkk6KYML",
		"asin": "7806397051",
		"reviewerName": "Jessica H.",
		"helpful": [1,1],
		"reviewText": "This palette was a decent price and I was looking for a few different shades.",
		"overall": 3,
		"summary": "OK Palette!",
		"unixReviewTime": 1397779200,
		"reviewTime": "04 18, 2014"
	},
{
		"reviewerID": "A60XNddddB87kkkk6KYML",
		"asin": "7806397054",
		"reviewerName": "Jessica H.",
		"helpful": [1,1],
		"reviewText": "This palette was a decent price and I was looking for a few other shades",
		"overall": 3,
		"summary": "OK Palette!",
		"unixReviewTime": 1397779600,
		"reviewTime": "05 18, 2014"
	},
	{
		"reviewerID": "A60XNddddB87kkkk6KYML",
		"asin": "7806397055",
		"reviewerName": "Karen",
		"helpful": [1],
		"reviewText": "The texture of this concealer pallet is fantastic, it has great coverage and a wide variety of uses, I guess it's meant for professional makeup artists and a lot of the colours are of no use to me but I use at least two of them on a regular basis, and two more occasionally, which is the only reason I'm giving it for stars, I feel like the range of colors is kind of a waste for me, but the  product itself  is wonderful, it's not cakey, gives me a natural for and concealed my imperfections, therefore I highly recommend it :)",
		"overall": 4,
		"summary": "great quality",
		"unixReviewTime": 1378425600,
		"reviewTime": "09 6, 2013"
	}
]

df = pandas.DataFrame.from_dict(json_normalize(data), orient='columns')


#fonction hethy t7seblk 9addeh 3anna mn auteur fy dataset (distinct)
 
x = json_normalize(data) 
t= len(x)
def NB_Auteur(t) :
   listeAuteur= []
   for i in range(t):
      y = x['reviewerID'][i]
      if y not in listeAuteur:
         listeAuteur.append(y)
   print(listeAuteur)
   return len(listeAuteur)
#print(NB_Auteur(t)) 

#fonction hethy t7seblk 9addeh 3anna mn review fy dataset (auteur distinct)
def NB_review(t) :
   cpt=0
   listeAuteur= []
   for i in range(t):
      y = x['reviewerID'][i]
      if y not in listeAuteur:
         listeAuteur.append(y)
         cpt = cpt + 1
   #print(listeAuteur)
   return cpt
print(NB_review(t)) 


#score t7seblk sum mt3 rating exclu les mem auteur 
#kima 9olt enty fy tafsyr "select score form table where auteurs differents" n3mlou somme mt3hom fy score 
def score(t) :
   scr = 0
   listeAuteur= []
   for i in range(t):       
       if x['reviewerID'][i] not in listeAuteur :
           scr = scr + x['overall'][i]  
           listeAuteur.append(x['reviewerID'][i])    
   return scr
print(score(t))

def Smean(t) :
   return score(t)/ NB_review(t) 
print(Smean(t))


def RD(r,t) :
     for i in range(t) :
         if x['reviewText'][i] == r :
              rate = x['overall'][i]
     d = abs(rate - Smean(t))
     rate_dev = d / 4
     return rate_dev  
r = x['reviewText'][0]
print(RD(r,t))




 







from __future__ import division
from sklearn.metrics.pairwise import cosine_similarity
from pandas.io.json import json_normalize
import pandas 
from pandas.io.json import json_normalize
import numpy as np

data = [
	{
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A60XNB876KYML",
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
		"reviewerID": "A60XNB876KYML",
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
		"reviewerID": "A3G6XNM240RMWA",
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
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A1YJEY40YUW4SE",
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
		"reviewerID": "A60XNB876KYML",
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
		"reviewerID": "A60XNB876KYML",
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
		"reviewerID": "A3G6XNM240RMWA",
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


#fonction hethy t7seblk 9addeh 3anna mn produit fy dataset .. eny lhne badalt bl3ani 7atyt 3 produit
#3malt liste w boucle tparcouri dataset w win tal9a produit jdyd tzydou lel liste w b3d 7sabt  longueur mt3 liste bch n3ref 9adeh 3anna mn produit 
x = json_normalize(data) 
t= len(x)
def NB_Pro(t) :
   listePro= []
   for i in range(t):
      y = x['asin'][i]
      if y not in listePro:
         listePro.append(y)
  # print(listePro)
   return len(listePro)
print(NB_Pro(t)) 
#t3tyk lliste de produit fi dataset heki 
def Liste_Pro(t) :
   listePro= []
   for i in range(t):
      y = x['asin'][i]
      if y not in listePro:
         listePro.append(y)
  # print(listePro)
   return listePro
print(Liste_Pro(t))
def NB_Pro(t) :
   listePro= []
   for i in range(t):
      y = x['asin'][i]
      if y not in listePro:
         listePro.append(y)
  # print(listePro)
   return len(listePro)
#print(NB_Pro(t))

#fi 9addehmn produit (distinct)l auteur hetha 3ta rayou 
def Hist(y,t) :
   cpt=0
   listePro= []
   for i in range(t):
       if y == x['reviewerID'][i] :
           z = x['asin'][i]
           if z not in listePro :
                cpt= cpt+1   
           listePro.append(z)    
   return cpt
#z= x['reviewerID'][0]
#print(Hist(z,t))

def NRP(y,t) :
  return Hist(y,t) / NB_Pro(t)


z= x['reviewerID'][0]


print(NRP(z,t))











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
		"reviewerID": "A1YJEY40YUW4SE",
		"asin": "7806397051",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 3,
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
		"asin": "7806397051",
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
		"reviewerID": "A1YJEY40YUW4SE",
		"asin": "7806397051",
		"reviewerName": "Andrea",
		"helpful": [3,4],
		"reviewText": "oooooooooo i like it e.",
		"overall": 2,
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
		"asin": "7806397051",
		"reviewerName": "Karen",
		"helpful": [1],
		"reviewText": "The texture of this concealer pallet is fantastic, it has great coverage and a wide variety of uses, I guess it's meant for professional makeup artists and a lot of the colours are of no use to me but I use at least two of them on a regular basis, and two more occasionally, which is the only reason I'm giving it for stars, I feel like the range of colors is kind of a waste for me, but the  product itself  is wonderful, it's not cakey, gives me a natural for and concealed my imperfections, therefore I highly recommend it :)",
		"overall": 4,
		"summary": "great quality",
		"unixReviewTime": 1378425600,
		"reviewTime": "09 6, 2013"
	}
]

#NbElems = Object.keys(data).length
#print(NbElems)
df = pandas.DataFrame.from_dict(json_normalize(data), orient='columns')
#print(type(df))

# print json_normalize(data)


#foction t3tyha y li howa reviewer_id  w length mt3 dataset  trj3lk nombre entre 0 et 1 (9addech mn marra l auteur hetheka 7att 0 ou 4 / 9addech mn marra 7att rayou ) 
x = json_normalize(data) 
t= len(x)
def NR2(y,t) :
   cpt=0
   for i in range(t):
      if y == x['reviewerID'][i]:
          cpt= cpt+1     
   return cpt
def EXR(y,t) :
   cpt=0
   for i in range(t):
      if y == x['reviewerID'][i]:
          if x['overall'][i] == 1 or x['overall'][i] == 4 : 
              cpt= cpt+1    
   m = NR2(y,t)
   print(m)
   print(cpt)
   return float(cpt/m)
   
 

#boucle t9ollk pour chaque auteur 9addech kteb mn review 3al produit heka 
#appel de fct 
z= x['reviewerID'][1] 
k = EXR(z,t)
print(k) 


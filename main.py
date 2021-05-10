#Another variation can be after ppl enter all their secrets at random the secrets r distributed among playes.
	#Meaning each player gets only one confession it can even be the same persons confession (collision).
	#so preferably ppl will b forced to play in huger grps to avoid collision.
	#All this will also make the whole matter more mysterious. cause udk who got yr secret or 
	#if anyone even did as ppl after getting disqualified will stop getting real confessions.
#Another variation is having turns lieing. so one person at random will be choosen to lie once in the grp.
	#his task is to lie best he can so that ppl cant catch it.
	#everyone other than the lier will read all confessions which will contain N-1 truth and 1 false and try to predict the false one.
	#ppl who guess right will get a point and the lier will get the point from those who got it wrong.
	#If everyone can guess the false answer the lier loses N points.


#thinking of putting a feature where u try to guess to whom does the confession belong too.
	#If u guess correct we dont tell anyone just that the person caught will lose some points.
	#Since the points r not shown ppl wont know if they r getting caught.
#thinking of putting a button to report if they feel any of the confession is false.
	#this will impact the score of person who lies in place of telling the truth.
	#this will b added to a vanity matrix
		#((((reputation to give u a general reputation, thinking of doing this to may b block a bad aggent or
		#to build high enough credibility so that when we introduce the stranger aggent we can club strangers with a similar reputation.))))
	#and too many reports may affect yr overall reputation.
	#this will also tell us how bad the lies r getting and v can inform others that they need to lie better cause others r doubting.
	#If u chose something is a lie u cant rank that confession.
#there will b 2 prizes one for normal point(which may include lie point) and the second for the best lier. 
#there will b an option to abot which ppl can use incase they think they r already disqualified or
#dey will automatically disqualify if they do not respond on time.
	#But if they wer not actually disqualified they forfitted their victory and all the following round secrets.
	#if u r disqualified in this manner everyone will b notified u r no longer playing.
#option to ask random questions anonymously ((based on some confession u read)) which others in yr circle will reply with.
	#No one knows knows who asked that question who answered what? 

#types of data collected:
	#we use some api to verify yr identity thats it.
		#we dont store yr email/phone(prefably) id as it is, we store a hash of it (to check if same user is creating new acc)
		#which means we cant spam u. we also do not collect any other personal data.
	#when u r verified v tell u to chose a username and passphrase(recomended) since v dont have yr email/phone v cant recover yr passphrase.
		#incase you forget yr passphrase u will have to try creating a new acc which we will flag as a new attempt.
		#so we will task u that u already r a user do u want to delete the old ac and create a new one?
		#we need to put warning saying we don't spend "much" on safety of login credentials so dont use passphrases and usernams of othr accs.
	#when u put in yr confessions we just transmit it over to yr friends and do not store it with us once transmission is complete.
		#The confessions are end-to-end encrypted in transit.
		#these confessions will be deleted frm yr frnds phones after everyone has answered nd ranked other ppls answers or after 48 hrs whchever happens first.
		#the data We will be collecting is yr scores from yr confessions.


#types of scores r:
	#Victor: ranking based score which is calculated based on how spicy yr revelation is.
	#Deceptor: ranking based on how high r yr lies ranked by the disqualified ppl.

	#Reputation: this matric will include all the other score in a way. 


class user:
	def __init__(self,truth,lies):			#make the variable name more ambigious so that ppl dont know what is truth and what is lies
		self.truth=truth
		self.lies=lies
		self.score=0
		self.feed=[]		#this will have all the confessions to be shown to u based on the whether u 'IN' or 'OUT'
		self.status=True	#true status means u still in game. 

class circle:
	def __init__(self,noOfPlayers,round,):

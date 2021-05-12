# class representing each node of the decision tree
class Node:
	def __init__(self, text, childs, isResult = False):
		self.isResult = isResult
		self.text = text
		self.childs = childs
	
	def dfs(self):
		if(self.isResult == True):
			return (self.text,"")
		
		userInput = input(self.text)
		val = userInput[:1]
		
		if(self.text == "What is your name? "):
			val = ""	
		elif(self.text == "What kind of cough?(dry/productive): "):
			if(val != "d" and val != "D" and val != "p" and val != "P"):
				print("Wrong input detected!")
				exit(0)
			if(val == "d" or val == "D"):
				val = "dry"
			if(val == "p" or val == "P"):
				val = "productive"
		else :
			val = checkYesOrNo(val)
		
		ret,_ = v[self.childs[val]].dfs()
		return (ret,userInput)

# Function to check if input provided is yes or no in a valid manner. 
def checkYesOrNo(val):
	val = val[:1]
	if(val != "n" and val != "N" and val != "y" and val != "Y"):
		print("Wrong input detected!")
		exit(0)
	if(val == "n"):
		val = "N"
	if(val == "y"):
		val = "Y"
	return val
		
if __name__ == "__main__":
	print("Covid Expert system \n\nKindly take this test if you have any of the these symptoms: \nChest pain, Cough, Fever, Rapid breathing, Rapid heartbeat, Shortness of breath, Wheezing\n")

	# Creating the decision tree graph
	v = []
	v.append(Node("What is your name? ", {"": 1}))
	v.append(Node("Do you have wheezing?(Y/N): ", {"Y": 2,"N": 3}))
	v.append(Node("Do you have smoking history?(Y/N): ", {"N": 4,"Y": 5}))
	v.append(Node("What kind of cough?(dry/productive): ", {"dry": 24,"productive": 25}))
	v.append(Node("Do you have rapid breathing?(Y/N): ", {"N": 6,"Y": 7}))
	v.append(Node("What kind of cough?(dry/productive): ", {"dry": 16,"productive": 17}))
	v.append(Node("Do you have chest pain?(Y/N): ", {"Y": 8,"N": 9}))
	v.append(Node("What kind of cough?(dry/productive): ", {"dry": 12,"productive": 13}))
	v.append(Node("Do you cough of blood?(Y/N): ", {"N": 10,"Y": 11}))
	v.append(Node("you may have Common Cold.", None, True))
	v.append(Node("you may have acute Bronchitis.", None, True))
	v.append(Node("you may have Bronchiectasis.", None, True))
	v.append(Node("you may have Asthma.", None, True))
	v.append(Node("Do you have fever?(Y/N): ", {"Y": 14,"N": 15}))
	v.append(Node("you may have Cystic Fibrosis.", None, True))
	v.append(Node("you may have Asthma.", None, True))
	v.append(Node("Do you have chest pain?(Y/N): ", {"N": 18,"Y": 19}))
	v.append(Node("Do you cough of blood?(Y/N): ", {"N": 20,"Y": 21}))
	v.append(Node("you may have Bronchitis.", None, True))
	v.append(Node("you may have occupational Lung Diseases.", None, True))
	v.append(Node("Do you have chest pain?(Y/N): ", {"N": 22,"Y": 23}))
	v.append(Node("you may have Lung Cancer.", None, True))
	v.append(Node("you may have Copd.", None, True))
	v.append(Node("you may have Pneumonia.", None, True))
	v.append(Node("Do you have rapid breathing?(Y/N): ", {"Y": 26,"N": 27}))
	v.append(Node("Do you have smoking history?(Y/N): ", {"N": 36,"Y": 37}))
	v.append(Node("Do you have rapid heartbeat?(Y/N): ", {"Y": 28,"N": 29}))
	v.append(Node("Do you have chest pain?(Y/N): ", {"N": 32,"Y": 33}))
	v.append(Node("you may have Influenza.", None, True))
	v.append(Node("Do you have chest pain?(Y/N): ", {"Y": 30,"N": 31}))
	v.append(Node("you may have Covid-19.", None, True))
	v.append(Node("you may have Influenza.", None, True))
	v.append(Node("Do you have rapid heartbeat?(Y/N): ", {"Y": 34,"N": 35}))
	v.append(Node("you may have Influenza.", None, True))
	v.append(Node("you may have Pertussis/Influenza.", None, True))
	v.append(Node("you may have Influenza.", None, True))
	v.append(Node("Do you have chest pain?(Y/N): ", {"N": 38,"Y": 39}))
	v.append(Node("you may have Rhinosinusitis.", None, True))
	v.append(Node("you may have Croup.", None, True))
	v.append(Node("you may have Tuberculosis.", None, True))
	
	text,name = v[0].dfs()
	if(text == "you may have Covid-19."):
		other_factors = []
		other_factors.append(checkYesOrNo(input("Do you have sore throat?(Y/N): ")))
		other_factors.append(checkYesOrNo(input("Have you lost some sense of taste or smell?(Y/N): ")))
		other_factors.append(checkYesOrNo(input("Are you feeling tired a lot? (Loss of speech and movement)(Y/N): ")))
		
		# Calculating the weighted average score to predict the chance of covid-19.
		scoreObtained = 2*1 + 2*1 + (1 if(other_factors[0] == 'Y') else 0) + (1 if(other_factors[1] == 'Y') else 0) + (2 if(other_factors[2] == 'Y') else 0)
		totalScorePossible = 2 + 2 + 1 + 1 + 2
		score = 1.0*scoreObtained/totalScorePossible
		if(score <= 0.75):
			print("{} you have high chances of being Covid +ve. Kindly get yourself checked and take care.".format(name))
		else:
			print("Covid warning! {} you have very high chances of being Covid +ve. Kindly get yourself checked and take care.".format(name))
		
	else :
		print("{} {}".format(name,text))

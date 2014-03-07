# Answer class
class Answer:
	def __init__(self, options, correct_answers): # List:options, List:correctAnswers
		# Answer Constructor
		self.options = options # Type: List
		self.correct_answers = correct_answers # Type: List
		self.selected_answers = [] # Type: List
	def selectAnswer(self, answer): # int:answer
		self.selected_answers.append(self.options[answer]) # Appends answer selected to selectedAnswers list
	def getSelectedAnswers(self):
		return self.selected_answers # Returns selectedAnswers variable
	def getOptions(self):
		return self.options # Returns options variable
	def countCorrect(self):
		count = 0
		for answer in self.selected_answers:
			if answer in self.correct_answers:
				count += 1
		return count
	def __str__(self):
		return "Answer: " + str(self.correct_answers)

if __name__ == '__main__':
	answer = Answer(['A','B','C','D','E'],['A','C'])
	print "answer: " + str(answer)
	print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
	print "answer.selectAnswer(0) # 0 = 'A'"
	answer.selectAnswer(0) # 0 = 'A'
	print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
	print "answer.getOptions(): " + str(answer.getOptions())
	print "answer.countCorrect(): " + str(answer.countCorrect())
	print "answer.selectAnswer(2) # 2 = 'C'"
	answer.selectAnswer(2) # 2 = 'C'
	print "answer.getSelectedAnswers(): " + str(answer.getSelectedAnswers())
	print "answer.countCorrect(): " + str(answer.countCorrect())

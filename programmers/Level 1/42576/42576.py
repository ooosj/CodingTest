def solution(participant, completion):
	
	dict = {}

	sumdict = 0

	for i in participant:

		dict[hash(i)] = i
		sumdict += hash(i)

	for i in completion:
		
		sumdict -= hash(i)
	
	return dict[sumdict]

import random 

def huffman(prob):
    if len(prob) == 0:
        return None
    elif len(prob) == 1:
        return ['0']
    elif len(prob) == 2:
        return ['0', '1']
    else:
        prob1 = min(prob)              # extracting minimum probability and it's index
        for i in range(0, len(prob)): 
            if prob1 == prob[i]:
                idx1 = i
                break
        prob.pop(idx1)                 
        prob2 = min(prob)           # extracting second minimum probability and it's index assuming that 1st one is removed
        for i in range(len(prob)):
            if prob2 == prob[i]:
                idx2 = i
                break
        prob.pop(idx2)
        prob.append(prob1+prob2)  # adding the added probability at the end
        code = huffman(prob)
        last_code = code.pop()    
        code.insert(idx2, last_code+'0')  # adding 0 and 1 to the added probability code and putting them in their respective places 
        code.insert(idx1, last_code+'1')
        return code

N = 100
prob_0 = [random.random() for _ in range(N)]
normalization_factor = sum(prob_0)
prob = [prob_0[i]/normalization_factor for i in range(N)]
print(prob)
print(huffman(prob))


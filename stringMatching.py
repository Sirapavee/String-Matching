#-----------------init-------------------
file = open('test2.txt', 'r')
fromText = []

for line in file:
    fromText.append(line.strip().split())

alphabet = fromText[0]
pattern = fromText[2]
text = fromText[3]
#-----------------------------------------

class naïve:
    def __init__(self, pattern, text):
        print("\n> I'm Naive ~")
        self.pattern = pattern
        self.text = text

    def matchLR(self):
        count = 0
        for i in range(len(self.text)-len(self.pattern)):
            for j in range(len(self.pattern)):
                if(text[i+j]!=pattern[j]):
                    count = 0
                    break
                elif(text[i+j]==pattern[j]):
                    count += 1
                    if(count==len(self.pattern)):
                        print(f'Pattern occur with shift {i+1} from Left to Right')
                        count = 0
    
    def matchRL(self):
        count = 0
        for i in range(len(self.text)-1, len(self.pattern)-2, -1):
            for j in range(len(self.pattern)):
                if(text[i-j]!=pattern[j]):
                    count = 0
                    break
                elif(text[i-j]==pattern[j]):
                    count += 1
                    if(count==len(self.pattern)):
                        print(f'Pattern occur with shift {i+1} from Right to Left')
                        count = 0
                        break

class KMP:
    def __init__(self, pattern, text):
        print("> I'm KMP !")
        self.pattern = pattern
        self.text = text
        self.prefTable = [0 for i in range(len(self.pattern))]

    def prefixFunc(self):
        k = 0
        for i in range(1, len(self.pattern)):
            while k > 0 and self.pattern[k+1] != self.pattern[i-1]:
                k = self.prefTable[k]
            if(self.pattern[k+1] == self.pattern[i-1]):
                k += 1
            self.prefTable[i] = k
            
    def matcherLR(self):
        q = 0
        for i in range(len(self.text)):
            while q > 0 and self.pattern[q] != self.text[i]:
                q = self.prefTable[q-1]
            if(self.pattern[q] == self.text[i]):
                q += 1
            if(q == len(self.pattern)):
                print(f'Pattern occur with shift {i-len(self.pattern)+2} from Left to Right')
                q = self.prefTable[q-1]

    def matcherRL(self):
        q = 0
        for i in range(len(self.text)-1, -1, -1):
            while q > 0 and self.pattern[q] != self.text[i]:
                q = self.prefTable[q-1]
            if(self.pattern[q] == self.text[i]):
                q += 1
            if(q == len(self.pattern)):
                print(f'Pattern occur with shift {i+len(self.pattern)} from Right to Left')
                q = self.prefTable[q-1]

kmp = KMP(pattern, text)
kmp.prefixFunc()
kmp.matcherLR()
kmp.matcherRL()

naive = naïve(pattern, text)
naive.matchLR()
naive.matchRL()
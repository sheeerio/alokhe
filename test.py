'''A=[' ', 'C', 'V', 'V', ' ', 'C', 'V', 'V', 'C', 'V', 'C', 'V', 'C', ' ']
for i in range(len(A)):
    if A[i] == 'V' and A[i+1]!='V':
        B=A[i+1:]
        for j in range(len(B)):
            if B[j]=='V' and B[j-1]=='C':
                B[j-1]='|C'
        Final = "".join(B)
        Start = A[:i+1]
        Start = "".join(Start)
        Word = Start+Final
        print(Word)
    if A[i]=='V' and A[i+1]=='V' and A[i+2]!=' ':
        A[i]='V|'''

import eng_to_ipa as ipa
yeah = ipa.syllable_count(input()) 
print(yeah)
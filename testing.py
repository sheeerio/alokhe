import eng_to_ipa as ipa
input = input()
V = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
IPA_V = ['ɑ', 'a', 'æ', 'ɔ', 'i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'aɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ',
         'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ä', 'ɑ', 'ɒ']

input_list = list(input)
ipa_word = ipa.convert(input)
ipa_word_list = list(ipa_word)
for i in range(len(ipa_word_list)):
    if ipa_word_list[i] == 'ˈ':
        ipa_word_list[i] = ''
    if ipa_word_list[i] == 'ˌ':
        ipa_word_list[i] = ''
    new_ipa_word = "".join(ipa_word_list)
    new_ipa_word = ' '+new_ipa_word+' '
new_ipa_word_list = list(new_ipa_word)
new_ipa_word_list_ref = list(new_ipa_word)
season_ticket = list(new_ipa_word)


def ipa_syl():
    for i in range(len(new_ipa_word_list)):
        if new_ipa_word_list[i] in IPA_V and new_ipa_word_list[i] != 'a' and new_ipa_word_list[i] != 'e':
            new_ipa_word_list[i] = 'V'
        elif new_ipa_word_list[i] not in IPA_V and new_ipa_word_list[i] != ' ' and new_ipa_word_list[i] != 'ɪ' and new_ipa_word_list[i] != '':
            new_ipa_word_list[i] = 'C'
        elif new_ipa_word_list_ref[i] == 'a' and new_ipa_word_list_ref[i+1] == 'ɪ':
            new_ipa_word_list[i] = 'V'
            new_ipa_word_list[i+1] = ''
        elif new_ipa_word_list_ref[i] == 'e' and new_ipa_word_list_ref[i+1] == 'ɪ':
            new_ipa_word_list[i] = 'V'
            new_ipa_word_list[i+1] = ''
        elif new_ipa_word_list_ref[i] == 'o' and new_ipa_word_list_ref[i+1] == 'ʊ':
            new_ipa_word_list[i] = 'V'
            new_ipa_word_list[i+1] = ''
        elif new_ipa_word_list_ref[i] == 'a' and new_ipa_word_list_ref[i+1] == 'ʊ':
            new_ipa_word_list[i] = 'V'
            new_ipa_word_list[i+1] = ''


ipa_syl()

A = new_ipa_word_list

V_index = A.index('V')
S_V_firstinstance = season_ticket[V_index]
S_V_firstinstance_index = season_ticket.index(S_V_firstinstance)
B = A[V_index+1:]
season_ticket_B = season_ticket[S_V_firstinstance_index+1:]
for j in range(len(B)):
    if B[j] == 'V' and B[j-1] == 'C':
        B[j-1] = '|C'
    elif B[j] == 'V' and B[j-1] == ' ':
        B[j] = '|V'
    elif B[j] == 'V' and B[j-1] == 'V' and B[j-2] == '|C':
        B[j] = '|V'
for x in range(len(B)):
    if B[x] == '|C' or B[x] == '|V':
        season_ticket_B[x] = ' '+season_ticket_B[x]
season_final = "".join(season_ticket_B)
season_start = season_ticket[:S_V_firstinstance_index+1]
season_start = "".join(season_start)
season_word = season_start+season_final
season_word = ' '+season_word+' '

season_list = list(season_word)
input = ' '+input+' '
input_list = list(input)
season_word = season_word.strip()
season_syl = season_word.split(" ")
print(season_syl)
Final = "".join(B)
Start = A[:V_index+1]
Start = "".join(Start)
Word = Start+Final
Word = Word.strip()
Syl = Word.split("|")

if len(season_list) < len(input_list):
    n = len(input_list)-len(season_list)
    for i in range(n):
        season_list.append(' ')
if len(input_list) < len(season_list):
    n = len(season_list)-len(input_list)
    for i in range(n):
        input_list.append(' ')

A = season_list
B = input_list
for x in range(len(B)):
    if A[x] == 'ʃ' and A[x+1] == 'ə' and A[x+2] == 'n':
        A[x] = 't'
        A[x+1] = 'io'
        A[x+2] = 'n'
    if A[x] == 'ʃ' and A[x+1] == 'ə' and A[x+2] != 'n':
        A[x] = 't'
        A[x+1] = 'io'
    elif B[x] == 't' and B[x+1] == 'i' and B[x+2] == 'o' and B[x+3] == 'n':
        B[x] = 't'
        B[x+1] = 'io'
        B[x+2] = 'n'
        B[x+3] = ''
    if B[x] == 't' and B[x+1] == 'u' and B[x+2] == 'r' and B[x+3] == 'e':
        B[x+1] = 'ur'
        B[x+2] = 'e'
        B[x+3] = ''
    elif A[x] == 'ʧ' and A[x+1] == 'ə' and A[x+2] == 'r':
        A[x] = 't'
        A[x+1] = 'ur'
        A[x+2] = 'e'
    if A[x] == 'k' and A[x] not in B:
        A[x] = 'c'
    if A[x] == 'ʤ' and 'j' not in B and 'g' not in B:
        A[x] = 'd'
    if A[x] == 'ʤ' and 'j' not in B and 'd' not in B:
        A[x] = 'g'
    if A[x] == 'ʤ' and 'g' not in B and 'd' not in B:
        A[x] = 'j'
    if A[x] == 'f' and 'f' not in B:
        A[x] = 'p'
        A[x+1] = 'h'+A[x+1]
    if A[x] == 'z' and 'z' not in B:
        A[x] = 's'
    if A[x] == 'ɪ' and 'i' not in B:
        A[x] = 'a'


def be():
    for i in range(len(A)):
        if A[i] == ' ' and A[i-1] != ' ' and A[i+1] != ' ':
            if A[i-1] in B and A[i+1] not in B:
                idx = B.index(A[i-1])
                B.insert(idx+1, ' ')
                
            if A[i+1] in B and A[i-1] not in B:
                global index
                index = B.index(A[i+1])
                B.insert(index, ' ')
            if A[i+1] in B and A[i-1] in B:
                idx = B.index(A[i+1])
                B.insert(idx, ' ')
                global B_crop
                B_crop = B[idx+1:]
                for f in range(len(B_crop)):
                    if B_crop[f]==A[i+1]:
                        idx = B_crop.index(A[i+1])
                        B_crop.insert(idx,' ')
                
be()


def correct_be():
    for i in range(len(B)):
        if i != len(B)-2:
            if B[i] == 't' and B[i+1] == ' ' and B[i+2] == 'io':
                B[i] = ''
                B[i+1] = 't'
        elif B[i] == 't' and B[i+1] == 'io':
            B[i] = ' '
            B[i+1] = 'tio'
        if B[i] == 's' and B[i+1] == ' ' and B[i+2] == 'i' and B[i+3] == 'o':
            B[i] = ''
            B[i+1] = 's'
        if B[i] == 'i' and B[i+1] == ' ' and B[i+2] == 'n' and B[i+3] == 'd':
            B[i] = ''
            B[i+1] = 'i'
        if B[i] == 't' and B[i+1] == ' ' and B[i-1] == ' ':
            B[i-1] = ''


correct_be()

for i in range(len(B)-1, -1, -1):
    if B[i] == ' ':
        B[i] = ''
    if B[i] != ' ':
        break
flag = 0
def correct_all():
    # write code such that the loop sums up the number of spaces(n) behind
    # each syllable start and then distributes it to the next same-starting-
    # alphabet (n-1) times
    count = 0
    for i in range(len(B)):
        if B[i] != ' ' and B[i-1] == ' ':
            temp = B[i]
            if B[i-1] == ' ' and B[i-2] != ' ':
                count = 0
                global B_
                B_ = B
            elif B[i-1] == ' ' and B[i-2] == ' ' and B[i-3] != ' ':
                count = 1
                B_ = B
            elif B[i-2] == ' ' and B[i-3] == ' ' and B[i-4] != ' ':
                count = 2
                B_ = B

            elif B[i-2] == ' ' and B[i-3] == ' ' and B[i-4] == ' ' and B[i-4] != ' ':
                count = 3
                B_ = B

            if count == 1:
                B_crop = B[i+1:]
                if temp in B_crop:
                    temp_idx = B_crop.index(temp)
                    B_crop.insert(temp_idx, ' ')
                B_ = B[:i+1]+B_crop
                B_join = "".join(B_)
                B_join.strip()
                B_list = B_join.split(" ")
                for i in range(len(B_list)):
                    while '' in B_list:
                        B_list.remove('')
                print(B_list)
                global flag
                flag = 1
correct_all()
B_join = "".join(B_)
B_join.strip()
B_list = B_join.split(" ")
for i in range(len(B_list)):
    while '' in B_list:
        B_list.remove('')
if flag==0:
    print(B_list)

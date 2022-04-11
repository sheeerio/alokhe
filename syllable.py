import eng_to_ipa as ipa
V = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
IPA_V = ['ɑ', 'a', 'æ', 'ɔ', 'i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'aɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ',
         'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ä', 'ɑ', 'ɒ']
input = input()
input_list = list(input)
print(input_list)
ipa_word = ipa.convert(input)
print(ipa_word)
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
print(new_ipa_word_list)
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
    print(new_ipa_word_list)


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
print(season_ticket_B)
print(B)
for x in range(len(B)):
    if B[x] == '|C' or B[x] == '|V':
        season_ticket_B[x] = ' '+season_ticket_B[x]
season_final = "".join(season_ticket_B)
season_start = season_ticket[:S_V_firstinstance_index+1]
season_start = "".join(season_start)
season_word = season_start+season_final
print(season_word)
season_word = season_word.strip()
season_syl = season_word.split(" ")
print(season_syl)
Final = "".join(B)
Start = A[:V_index+1]
Start = "".join(Start)
Word = Start+Final
print(Word)
Word = Word.strip()
Syl = Word.split("|")
print(Syl)
from flask import Flask, jsonify
import eng_to_ipa as ipa
IPA = ['a', 'ɪ', 'j', 'u', 'z', 'd', 't', 'i', 'ʧ', 'ɪx', 'k', 'ə', 'n', 'ð', 'ɛ', 'r', 'ɔ', 'v',
       's', 'l', 'w', 'ʊ', 'ð', 'ɦ', 'θ', 'ɑ', 'p', 'ʃ', 'b', 'ɡ', 'æ', 'm', 'ŋ', 'f', 'o', 'ʤ', 'ʒ']
Dev = ['ā', 'e', 'y', 'ū', 'z', 'ḍ', 'ṭ', 'ī', 'c', 'i', 'k', '\'', 'n', 'd', 'X', 'r', 'O', 'v',
       's', 'l', 'v', '0', 'd', 'h', 'F', 'ɑ', 'p', 'ś', 'b', 'g', 'æ', 'm', 'ŋ', 'f', 'o', 'j', 'j']
Hin = ['आ', 'इ', 'ह्य', 'ऊ', 'ज़', 'ड', 'ट', 'ई', 'च', 'इ', 'क', 'अ', 'न', 'द', 'ऐ', 'र', 'औ', 'व',
       'स', 'ल', 'व', 'ओ', 'द', 'ह', 'थ', 'आ', 'प', 'श', 'ब', 'ग', 'ऐ', 'म', ' ं', 'फ', 'ओ', 'ज', 'ज']

V = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
IPA_V = ['ɑ', 'a', 'æ', 'ɔ', 'i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'aɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ',
         'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ä', 'ɑ', 'ɒ']


app = Flask(__name__)

def ipatodev(a):
    letters = list(a)
    for i in range(len(letters)):
        for j in range(len(IPA)):
            if letters[i] == IPA[j]:
                letters[i] = Dev[j]
    global dev
    dev = "".join(letters)
    #deva = "".join(letters)
def nice(v):
    no = ipa.convert(v)
    yes = no.split()

    for i in range(len(yes)):
        if yes[i] == 'tɪ':
            yes[i] = 'tu'
        if yes[i] == 'ðət':
            yes[i] = 'ðæt'
        if yes[i] == 'dɪz':
            yes[i] = 'dəz'
        if yes[i] == 'fər':
            yes[i] = 'fɔr'
        if yes[i] == 'ˈgreɪtnəs':
            yes[i] = 'ˈgreɪtnɪs'
        if yes[i] == 'ənd':
            yes[i] = 'ænd'
        if yes[i] == 'frəm':
            yes[i] = 'frɔm'
        if yes[i] == 'ər':
            yes[i] = 'ar'
        if yes[i] == 'ˈjuˈɛs':
            yes[i] = 'əs'
        if yes[i] == 'ðən':
            yes[i] = 'ðæn'
        if yes[i] == 'ɪm':
            yes[i] = 'jɪm'
        if yes[i] == 'rɛd':
            yes[i] = '[rɛd, rid]'
        global goodinput
        goodinput = " ".join(yes)

def devtohin(b):
    dev_letters = list(b)
    for i in range(len(dev_letters)):
        for j in range(len(Dev)):
            if dev_letters[i] == Dev[j]:
                dev_letters[i] = Hin[j]
    global hind
    hind = "".join(dev_letters)
    hind = '  '+hind+'  '

def hincorrect(c):
    global hin_letters
    hin_letters = list(c)
    for i in range(len(hin_letters)):
        if hin_letters[i] == 'ˈ':
            hin_letters[i] = ''
        if hin_letters[i] == ' ' and hin_letters[i-1] == ' ':
            hin_letters[i] = ''
        if hin_letters[i] == 'ओ' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'ए' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'ऊ' and hin_letters[i-1] != ' ' and hin_letters[i+1] != 'ओ':
            hin_letters[i] = 'ो'
        if hin_letters[i] == 'ओ' and hin_letters[i+1] == 'ओ':
            hin_letters[i+1] = ''
        if hin_letters[i] == 'क' and hin_letters[i+1] == 'व':
            hin_letters[i] = 'क्'
        if hin_letters[i] == 'ए' and hin_letters[i-1] != 'ए' and hin_letters[i+1] != 'ए' and i != 0 and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ऊ' and hin_letters[i-1] != 'औ' and hin_letters[i-1] != ' ':
            hin_letters[i] = hin_letters[i-1]+'े'
            hin_letters[i-1] = ''
        if hin_letters[i] == 'ए' and hin_letters[i+1] == 'ए':
            hin_letters[i+1] = ''
        if hin_letters[i] == 'ऐ' and hin_letters[i-1] != ' ' and hin_letters[i-1] != '' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'आ' and hin_letters[i+1] != 'ट' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ऊ' and hin_letters[i-1] != 'औ' and hin_letters[i-1] != ' ':
            hin_letters[i] = hin_letters[i-1]+'ै'
            hin_letters[i-1] = ''
        if hin_letters[i] == 'ऊ' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ए':
            hin_letters[i] = hin_letters[i-1]+'ू'
            hin_letters[i-1] = ''
        if hin_letters[i] == 'आ' and hin_letters[i+1] != 'े' and hin_letters[i-1] != '' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ए' and hin_letters[i+1] != 'ए' and hin_letters[i-1] != 'औ' and hin_letters[i-1] != ' ' and hin_letters[i-1] != 'ˈ':
            hin_letters[i] = 'ा'
        if hin_letters[i] == 'औ' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'ए' and hin_letters[i-1] != 'औ' and hin_letters[i-1] != ' ':
            hin_letters[i] = 'ौ'
        if hin_letters[i] == 'ई' and hin_letters[i-1] != 'ˈ' and hin_letters[i-1] != ' ' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'औ' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'ए' and hin_letters[i-1] != 'औ':
            hin_letters[i] = 'ी'
        if hin_letters[i] == 'उ' and hin_letters[i-1] != 'ओ' and hin_letters[i-1] != 'ई' and hin_letters[i-1] != 'आ' and hin_letters[i-1] != 'अ' and hin_letters[i-1] != 'ए' and hin_letters[i-1] != 'ऊ':
            hin_letters[i] = hin_letters[i-1]+'ु'
            hin_letters[i-1] = ''
        if hin_letters[i] == 'औ' and hin_letters[i+1] == 'ओ':
            hin_letters[i] = 'ओ'
            hin_letters[i+1] = ''
        if hin_letters[i] == 'ग' and hin_letters[i+1] == 'र':
            hin_letters[i] = 'ग्र'
            hin_letters[i+1] = ''
        if hin_letters[i] == 'प' and hin_letters[i+1] == 'र':
            hin_letters[i] = 'प'+'्र'
            hin_letters[i+1] = ''
        if hin_letters[i] == 'ब' and hin_letters[i+1] == 'र':
            hin_letters[i] = 'ब'+'्र'
            hin_letters[i+1] = ''
        if hin_letters[i] == 'ौ' and hin_letters[i+1] == 'ौ':
            hin_letters[i+1] = ''
        if hin_letters[i] == 'थ' and hin_letters[i+1] == 'र':
            hin_letters[i] = 'थ'+'्र'
            hin_letters[i+1] = ''
        if hin_letters[i] == 'ै' and hin_letters[i-1] == '':
            hin_letters[i-2] = hin_letters[i-2]+'ै'
            hin_letters[i] = ''
        if hin_letters[i] == 'न' and hin_letters[i+1] == '':
            hin_letters[i+1] = ' '
        if hin_letters[i] == 'ट' and hin_letters[i+1] == 'र':
            hin_letters[i] = 'ट्'
    global hindi
    hindi = "".join(hin_letters)
    global better_hindi
    better_hindi = ' '+hindi+' '

def hincorrect2(d):
    badhindi = list(d)
    for i in range(len(badhindi)):
        if badhindi[i] == 'ˈ':
            badhindi[i] = ''
        if badhindi[i] == 'ˌ':
            badhindi[i] = ''
        if badhindi[i] == 'े' and badhindi[i-1] == '':
            badhindi[i] = 'ए'
        if badhindi[i] == 'ो' and badhindi[i-1] == '':
            badhindi[i] = 'ओ'
        if badhindi[i] == 'ौ' and badhindi[i-1] == '':
            badhindi[i] = 'औ'
        if badhindi[i] == 'ं' and badhindi[i-1] != ' ':
            badhindi[i] = badhindi[i+1]+'ं'
            badhindi[i+1] = ''
            badhindi[i-1] = ''
        if badhindi[i] == 'क' and badhindi[i+1] == 'र':
            badhindi[i] = 'क'+'्र'
            badhindi[i+1] = ''
        if badhindi[i] == 'ं' and badhindi[i-1] == ' ':
            if badhindi[i+1] == ' ' or badhindi[i+1] == ',' or badhindi[i+1] == '.' or badhindi[i+1] == '?' or badhindi[i+1] == '!':
                badhindi[i-1] = badhindi[i-2]+'ं'
                badhindi[i] = 'ग'
                badhindi[i-2] = ''
        if badhindi[i] == 'ो' and badhindi[i+1] == 'ो':
            badhindi[i] = 'ो'
            badhindi[i+1] = ''
        if badhindi[i] == 'न' and badhindi[i+1] != ' ' and badhindi[i+1] != 'अ' and badhindi[i+1] != 'ी' and badhindi[i+1] != 'ा' and badhindi[i+1] != 'े' and badhindi[i+1] != 'ो' and badhindi[i-1] != '' and badhindi[i+1] != 'आ' and badhindi[i+1] != 'ो' and badhindi[i+1] != 'ा' and badhindi[i+1] != 'े' and badhindi[i-1] != ' ' and badhindi[i-1] != 'ी' and badhindi[i+1] != '' and badhindi[i+2] != '' and badhindi[i-1] != '' and badhindi[i+1] != '' and badhindi[i-1] != 'े' and badhindi[i-1] != 'ो' and badhindi[i+1] != 'ी' and badhindi[i+1] != 'ौ' and badhindi[i+1] != 'ो' and badhindi[i+1] != 'े':
            badhindi[i] = badhindi[i-1]+'ं'
            badhindi[i-1] = ''
        if badhindi[i] == 'ए' and badhindi[i-1] == '' and badhindi[i-2] != ' ':
            badhindi[i-2] = badhindi[i-2]+'े'
            badhindi[i] = ''
        if badhindi[i] == 'ए' and badhindi[i+1] == 'ए':
            badhindi[i+1] = ''
        if badhindi[i] == 'ा' and badhindi[i+1] == 'ो':
            badhindi[i] = 'आ'+'ो'
            badhindi[i+1] = ''
        if badhindi[i] == 'र' and badhindi[i-1] != ' ' and badhindi[i+1] != 'इ' and badhindi[i+1] != '' and badhindi[i+1] != 'ी' and badhindi[i+1] != 'ा' and badhindi[i+1] != 'े' and badhindi[i+1] != 'ो' and badhindi[i-1] != '' and badhindi[i+1] != 'आ' and badhindi[i+1] != 'ो' and badhindi[i+1] != 'ा' and badhindi[i+1] != 'े' and badhindi[i+1] != ' ':
            badhindi[i] = 'र्'+badhindi[i+1]
            badhindi[i+1] = ''
        if badhindi[i] == 'स' and badhindi[i+1] == 'ट':
            badhindi[i] = 'स्'
        if badhindi[i] == 'आ' and badhindi[i+1] != 'े' and badhindi[i-1] != 'ओ' and badhindi[i-1] != 'ई' and badhindi[i-1] != 'अ' and badhindi[i-1] != 'ए' and badhindi[i-1] != 'औ' and badhindi[i-1] != ' ':
            badhindi[i] = 'ा'
        if badhindi[i] == 'ट' and badhindi[i+1] == 'स':
            badhindi[i] = 'ट्'
        if badhindi[i] == 'प' and badhindi[i+1] == 'ट':
            badhindi[i] = 'प्'
        if badhindi[i] == 'व' and badhindi[i+1] == 'ड':
            badhindi[i] = 'व्'
        if badhindi[i] == 'ल' and badhindi[i+1] == 'फ':
            badhindi[i] = 'ल्'
        if badhindi[i] == 'क' and badhindi[i+1] == 'ट':
            badhindi[i] = 'क्'
        if badhindi[i] == 'े' and badhindi[i-1] == ' ':
            badhindi[i] = 'ए'
        if badhindi[i] == 'ी' and badhindi[i-1] == ' ':
            badhindi[i] = 'ई'
        if badhindi[i] == 'र्' and badhindi[i+1] == '':
            badhindi[i] = 'र'
        if badhindi[i] == 'ब' and badhindi[i+1] == 'ल':
            badhindi[i] = 'ब्'
        if badhindi[i] == 'ड' and badhindi[i+1] == 'ज' and badhindi[i+2] == '़':
            badhindi[i] = 'ड्'
        if badhindi[i] == 'इ' and badhindi[i+1] == 'इ':
            badhindi[i] = 'ए'
            badhindi[i+1] = ''
        if badhindi[i] == 'र्ˌ' and badhindi[i+1] == '':
            badhindi[i] = 'र्'
    global final
    final = "".join(badhindi)


def hin_perf(e):
    finalist = list(e)
    for i in range(len(finalist)):
        if finalist[i] == 'इ' and finalist[i-1] != ' ' and finalist[i+1] != ' ' and finalist[i-1] != 'ो' and finalist[i-1] != 'ै' and finalist[i-1] != 'ा':
            finalist[i] = finalist[i-1]+'ि'
            finalist[i-1] = ''
        if finalist[i] == 'ओ' and finalist[i-1] != 'आ' and finalist[i-1] != 'ए' and finalist[i-1] != 'अ' and finalist[i-1] != 'ई' and finalist[i-1] != 'ऊ' and finalist[i-1] != ' ' and finalist[i+1] != ' ' and finalist[i+1] != 'ओ':
            finalist[i] = 'ो'
        if finalist[i] == 'ै' and finalist[i-1] == ' ':
            finalist[i] = 'ऐ'
        if finalist[i] == 'अ' and finalist[i+1] == ' ' and finalist[i-1] != ' ':
            finalist[i] = 'ा'
        if finalist[i] == 'ए' and finalist[i-1] != ' ' and finalist[i-1] != 'ू' and finalist[i-1] != 'ो' and finalist[i-1] != 'ै' and finalist[i-1] != 'ा' and finalist[i-1] != 'ी':
            finalist[i] = finalist[i-1]+'े'
            finalist[i-1] = ''
        if finalist[i] == 'अ' and finalist[i-1] != ' ' and finalist[i+1] == ' ':
            finalist[i] = 'ा'
        if finalist[i] == 'अ' and finalist[i-1] != ' ' and finalist[i+1] != ' ' and finalist[i-1] != 'ू' and finalist[i-1] != 'ी':
            finalist[i] = ''
        if finalist[i] == 'र' and finalist[i+1] == '्':
            if finalist[i+2] == 'ो' or finalist[i+2] == 'ै' or finalist[i+2] == 'े' or finalist[i+2] == 'ी':
                finalist[i+1] = ''
        if finalist[i] == 'र' and finalist[i-1] == '्' and finalist[i+1] == '्':
            finalist[i+1] = ''
        if finalist[i] == 'ऐ' and finalist[i-1] != ' ':
            finalist[i] = finalist[i-1]+'ै'
            finalist[i-1] = ''
        if finalist[i] == 'ं' and finalist[i+1] == 'इ':
            finalist[i] = 'न'
        if finalist[i] == 'ं' and finalist[i-1] == ' ':
            finalist[i-1] = ''
        if finalist[i] == 'आ' and finalist[i+1] == 'ो':
            finalist[i] = 'ा'
            finalist[i+1] = 'उ'
        if finalist[i] == 'व' and finalist[i+1] == 'ज':
            finalist[i] = 'व्'
    global finall
    finall = "".join(finalist)
    return finall

def inputprop(k):
    global input_list
    input_list = list(k)
    global inputta
    inputta = "".join(input_list)
    ipa_word = ipa.convert(k)
    ipa_word_list = list(ipa_word)
    for i in range(len(ipa_word_list)):
        if ipa_word_list[i] == 'ˈ':
            ipa_word_list[i] = ''
        if ipa_word_list[i] == 'ˌ':
            ipa_word_list[i] = ''
        new_ipa_word = "".join(ipa_word_list)
        new_ipa_word = ' '+new_ipa_word+' '
    global new_ipa_word_list
    new_ipa_word_list = list(new_ipa_word)
    global new_ipa_word_list_ref
    new_ipa_word_list_ref = list(new_ipa_word)
    global season_ticket
    season_ticket = list(new_ipa_word)

def ipa_syl(l):
    for i in range(len(l)):
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
    global A
    A = new_ipa_word_list





def ipa_syl_break():
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
    global season_word
    season_word = season_start+season_final
    season_word = ' '+season_word+' '
    global season_list
    season_list = list(season_word)
    input = ''+inputta+' '
    global input_list
    input_list = list(input)
    season_word = season_word.strip()
    season_syl = season_word.split(" ")
    print(season_syl)
    hin_syl_list = []
    print(hin_syl_list)
    Final = "".join(B)
    Start = A[:V_index+1]
    Start = "".join(Start)
    Word = Start+Final
    Word = Word.strip()
    global Syl
    Syl = Word.split("|")

def eng_break1():
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
        if A[x] == 'ʃ' and A[x+1] == 'ə' and A[x+2] != 'n' and 'c' not in B:
            A[x] = 't'
            A[x+1] = 'io'
        if A[x] == 'ʃ' and A[x+1] == 'ə' and 'c' in B and B[B.index('c')+1] == 'i':
            A[x] = 'c'
            A[x+1] = 'ia'
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
        if A[x] == 'k' and 'k' and 'q' not in B:
            A[x] = 'c'
        elif A[x] == 'k' and A[x] not in B and 'c' not in B:
            A[x] = 'q'
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
        if A[x]=='s' and 'c' in B:
            A[x]='c'
        if A[x] == 'i' and A[x+1]==' ' and A[x-1]!=' ' and 'ee' not in B:
            A[x]='y'

    for i in range(len(A)):
        if i!=len(A)-1:
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
                        if B_crop[f] == A[i+1]:
                            idx = B_crop.index(A[i+1])
                            B_crop.insert(idx, ' ')

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



    for i in range(len(B)-1, -1, -1):
        if B[i] == ' ':
            B[i] = ' '
        if B[i] != ' ':
            break
    flag = 0
    global B_
    B_ = B


    # write code such that the loop sums up the number of spaces(n) behind
    # each syllable start and then distributes it to the next same-starting-
    # alphabet (n-1) times
    flag1=0
    count = 0
    for i in range(len(B)):
        if B[i] != ' ' and B[i-1] == ' ' and i != 0:
            if B[i-1] == ' ' and B[i-2] != ' ':
                count = 0
                B_ = B
            elif B[i-1] == ' ' and B[i-2] == ' ' and B[i-3] != ' ':
                count = 0
                B_ = B
            elif B[i-2] == ' ' and B[i-3] == ' ' and B[i-4] != ' ':
                count = 2
                B_ = B

            elif B[i-2] == ' ' and B[i-3] == ' ' and B[i-4] == ' ' and B[i-4] != ' ':
                count = 3
                B_ = B

            if count == 0:
                B_crop = B[i+2:]
                if B[i] in B_crop and B[i+1] != B[i]:
                    temp_idx = B_crop.index(B[i])
                    if B_crop[temp_idx+1] != ' ':
                        B_crop.insert(temp_idx, ' ')
                        B_ = B[:i+2]+B_crop
                        temp_index_remove = B_.index(B[i])
                        B_.pop(temp_index_remove-1)
                        B_join = "".join(B_)
                        B_join.strip()
                        global B_list1
                        B_list1 = B_join.split(" ")
                        for i in range(len(B_list1)):
                            while '' in B_list1:
                                B_list1.remove('')
                        print(B_list1)
                        flag1 = 1
    if flag1 == 0:
        B_join = "".join(B_)
        B_join.strip()
        global B_list
        B_list = B_join.split(" ")
        for i in range(len(B_list)):
            while '' in B_list:
                B_list.remove('')
    elif flag1==1:
        B_list = B_list1
    global B_final
    B_final = B_list
@app.route("/<string:input>")
def hello_world(input):
    nice(input)
    ipatodev(goodinput)
    devtohin(dev)
    hincorrect(hind)
    hincorrect2(better_hindi)
    FINALISTA = hin_perf(final)
    inputprop(input)
    ipa_syl(new_ipa_word_list)
    ipa_syl_break()
    eng_break1()
    season_syl = season_word.split(" ")
    hin_syl_list = []
    for k in range(len(season_syl)):
        temp = season_syl[k]
        ipatodev(temp)
        devtohin(dev)
        hincorrect(hind)
        hincorrect2(better_hindi)
        hin_perf(final)
        hin_syl_list.append(finall)
    return  jsonify({'text': {'hinout': FINALISTA,'engin':input}, 'useless_syl' : {'wordsyl':Syl,  'ipasyl':season_syl}, 'useful_syl' : {'engsyl':B_final, 'hinsyl':hin_syl_list}})

if __name__ == "__main__":
    app.run(debug=True)
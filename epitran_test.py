import epitran
from epitran.backoff import Backoff
bruh = input()
backoff = Backoff(['hin-Deva','ben-Beng'])
haha = backoff.transliterate(bruh)
print(haha)
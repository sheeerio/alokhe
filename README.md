# English to Hindi Transliteration
Uses rule-based transliteration using IPA and [eng_to_ipa](https://pypi.org/project/eng-to-ipa/) library. 

*Note: The output is based on the CMU-DICT IPA which is entirely based off the american accent* 

## How to use?
Put your word in after `https://alokhe.herokuapp.com/`. For example, `https://alokhe.herokuapp.com/machine%20translation` outputs `मशीन ट्रैनज़लेशन`.

## Examples
`https://alokhe.herokuapp.com/extravagant` outputs:
`ऐकस्ट्रैवगंट` and other potentially (and mostly buggy) useful syllable lists.

`https://alokhe.herokuapp.com/What%20should%20be%20the%20input%20here?%20Interestingly,%20we%20don%27t%20know%20man` outputs:
`वट शोड बी दा इंपोट हीर` while google transliterate outputs `व्हाट शुड बे थे आंसर हेरे? इन्टरेस्टिंगली, वे डॉन'टी मन` which has quite a few mistakes

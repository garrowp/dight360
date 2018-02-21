import nltk
import re

from glob import glob
from nltk import word_tokenize
from nltk.probability import FreqDist

# define a dictionary of FreqDists
word_lists = {
    'IN': FreqDist(),
    'IP': FreqDist(),
    'LY': FreqDist(),
    'NA': FreqDist(),
    'OP': FreqDist(),
    'SP': FreqDist(),
}

# string of funciton words
func_string = "A ABOUT ABOVE AFTER AGAIN AGO ALL ALMOST ALONG ALREADY ALSO ALTHOUGH ALWAYS AM AMONG AN AND ANOTHER ANY ANYBODY ANYTHING ANYWHERE ARE AREN'T AROUND AS AT BACK ELSE BE BEEN BEFORE BEING BELOW BENEATH BESIDE BETWEEN BEYOND BILLION BILLIONTH BOTH EACH BUT BY CAN CAN'T COULD COULDN'T DID DIDN'T DO DOES DOESN'T DOING DONE DON'T DOWN DURING EIGHT EIGHTEEN EIGHTEENTH EIGHTH EIGHTIETH EIGHTY EITHER ELEVEN ELEVENTH ENOUGH EVEN EVER EVERY EVERYBODY EVERYONE EVERYTHING EVERYWHERE EXCEPT FAR FEW FEWER FIFTEEN FIFTEENTH FIFTH FIFTIETH FIFTY FIRST FIVE FOR FORTIETH FORTY FOUR FOURTEEN FOURTEENTH FOURTH HUNDRED FROM GET GETS GETTING GOT HAD HADN'T HAS HASN'T HAVE HAVEN'T HAVING HE HE'D HE'LL HENCE HER HERE HERS HERSELF HE'S HIM HIMSELF HIS HITHER HOW HOWEVER NEAR HUNDREDTH I I'D IF I'LL I'M IN INTO IS I'VE ISN'T IT ITS IT'S ITSELF JUST LAST LESS MANY ME MAY MIGHT MILLION MILLIONTH MINE MORE MOST MUCH MUST MUSTN'T MY MYSELF NEAR NEARBY NEARLY NEITHER NEVER NEXT NINE NINETEEN NINETEENTH NINETIETH NINETY NINTH NO NOBODY NONE NOONE NOTHING NOR NOT NOW NOWHERE OF OFF OFTEN ON OR ONCE ONE ONLY OTHER OTHERS OUGHT OUGHTN'T OUR OURS OURSELVES OUT OVER QUITE RATHER ROUND SECOND SEVEN SEVENTEEN SEVENTEENTH SEVENTH SEVENTIETH SEVENTY SHALL SHAN'T SHE'D SHE SHE'LL SHE'S SHOULD SHOULDN'T SINCE SIX SIXTEEN SIXTEENTH SIXTH SIXTIETH SIXTY SO SOME SOMEBODY SOMEONE SOMETHING SOMETIMES SOMEWHERE SOON STILL SUCH TEN TENTH THAN THAT THAT THAT'S THE THEIR THEIRS THEM THEMSELVES THESE THEN THENCE THERE THEREFORE THEY THEY'D THEY'LL THEY'RE THIRD THIRTEEN THIRTEENTH THIRTIETH THIRTY THIS THITHER THOSE THOUGH THOUSAND THOUSANDTH THREE THRICE THROUGH THUS TILL TO TOWARDS TODAY TOMORROW TOO TWELFTH TWELVE TWENTIETH TWENTY TWICE TWO UNDER UNDERNEATH UNLESS UNTIL UP US VERY WHEN WAS WASN'T WE WE'D WE'LL WERE WE'RE WEREN'T WE'VE WHAT WHENCE WHERE WHEREAS WHICH WHILE WHITHER WHO WHOM WHOSE WHY WILL WITH WITHIN WITHOUT WON'T WOULD WOULDN'T YES YESTERDAY YET YOU YOUR YOU'D YOU'LL YOU'RE YOURS YOURSELF YOURSELVES YOU'VE 'S"

func_list = func_string.lower().split()
func_set = set(func_list)

# regex for getting the text for the p and h tags
h_re = r'<h>(.*?)<'
p_re = r'<p>(.*?)<'

# get the files names from the Mini-CORE
filenames = glob('Mini-CORE/*.txt')


# loop through each file name
for filename in filenames:

    # find the register for the file
    register_search = r'Mini-CORE/1\+(\w{2})'
    register = re.findall(register_search, filename)[0]

    # open the file
    with open(filename, 'r') as f:
        # get the text from the file
        raw_text = f.read()
        h_text = ' '.join(re.findall(h_re, raw_text, re.S))
        p_text = ' '.join(re.findall(p_re, raw_text, re.S))
        file_text = h_text + ' ' + p_text
        file_tokens = word_tokenize(file_text)

        # filter out the funciton words
        file_words = [word for word in file_tokens
                      if word.lower() not in func_set]

        # udpate each FreqDist
        word_lists[register].update(file_words)

        # sort each FreqDist
        sorted(word_lists[register].most_common(), key=lambda x: x[1])
        # print(word_lists[register])


# loop through each list
for key, value in word_lists.items():
    out_file = key + '.txt'

    # output results
    with open(out_file, 'w') as f:
        print(str(value.most_common()), file=f)

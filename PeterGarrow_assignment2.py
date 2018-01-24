import re

myText = """Cambodia  officially known as the Kingdom of Cambodia is a country located in the southern portion of the Indochina Peninsula in Southeast Asia.t is 181,035 square kilometres (69,898 square miles) in area, bordered by Thailand to the northwest, Laos to the northeast, Vietnam to the east, and the Gulf of Thailand to the southwest.

Cambodia has a population of over 15 million. The official religion is Theravada Buddhism, practiced by approximately 95 percent of the population. The country's minority groups include Vietnamese, Chinese, Chams, and 30 hill tribes.[8] The capital and largest city is Phnom Penh, the political, economic, and cultural centre of Cambodia. The kingdom is an elective constitutional monarchy with Norodom Sihamoni, a monarch chosen by the Royal Throne Council, as head of state. The head of government is Hun Sen, who is currently Prime minister and the longest serving non-royal leader in South East Asia and has ruled Cambodia for over 30 years.

In 802 AD, Jayavarman II declared himself king, uniting the warring Khmer princes of Chenla under the name "Kambuja".[9] This marked the beginning of the Khmer Empire which flourished for over 600 years, allowing successive kings to control and exert influence over much of Southeast Asia and accumulate immense power and wealth. The Indianized kingdom built monumental temples including Angkor Wat, now a World Heritage Site, and facilitated the spread of first Hinduism, then Buddhism to much of Southeast Asia. After the fall of Angkor to Ayutthaya in the 15th century, a reduced and weakened Cambodia was then ruled as a vassal state by its neighbours. In 1863 Cambodia became a protectorate of France which doubled the size of the country by reclaiming the north and west from Thailand.

Cambodia gained independence in 1953. The Vietnam War extended into the country with the US bombing of Cambodia from 1969 until 1973. Following the Cambodian coup of 1970, the deposed king gave his support to his former enemies, the Khmer Rouge. The Khmer Rouge emerged as a major power, taking Phnom Penh in 1975 and later carrying out the Cambodian Genocide from 1975 until 1979, when they were ousted by Vietnam and the Vietnamese-backed People's Republic of Kampuchea in the Cambodian–Vietnamese War (1979–91).

Following the 1991 Paris Peace Accords, Cambodia was governed briefly by a United Nations mission (1992–93). The UN withdrew after holding elections in which around 90 percent of the registered voters cast ballots. The 1997 coup placed power solely in the hands of Prime Minister Hun Sen and the Cambodian People's Party, who remain in power as of 2017.

The country faces numerous challenges. Important sociopolitical issues includes widespread poverty,[10] pervasive corruption,[11] lack of political freedoms,[12] low human development,[13] and a high rate of hunger.[14][15][16] Cambodia has been described by Human Rights Watch's Southeast Asian Director, David Roberts, as a "vaguely communist free-market state with a relatively authoritarian coalition ruling over a superficial democracy." [17]

While per capita income remains low compared to most neighboring countries, Cambodia has one of the fastest growing economies in Asia with growth averaging 6 percent over the last decade. Agriculture remains the dominant economic sector, with strong growth in textiles, construction, garments, and tourism leading to increased foreign investment and international trade.[18] Cambodia scored dismally in an annual index (2015) ranking the rule of law in 102 countries, placing 99th overall and the worst in the region.[19]

Cambodia also faces environmental destruction as an imminent problem. The most severe activity in this regard is considered to be the countrywide deforestation, which also involves national parks and wildlife sanctuaries. Overall, environmental destruction in Cambodia comprise many different activities, including illegal logging, poaching of endangered and endemic species, and destruction of important wildlife habitats from large scale construction projects and agricultural businesses. The degrading activities involve the local population, Cambodian businesses and political authorities, as well as foreign criminal syndicates and many transnational corporations from all over the world."""


def checkIng(text):
    result = []
    str_re = r'(?:\bthe\b\s)?(?:\b\w*?\b\s)?(\w{2,}ing\b)\s\bof\b'
    result = re.findall(str_re, text)
    str_re = r'\s(\w{2,}ing\b),'
    result.extend(re.findall(str_re, text))
    print('ing:', result)
    print('count:', len(result))
    print()
    return result


def checkOr(text):
    str_re = r'(\w{2,}ors?)\b'
    exceptions = ['Angkor', 'major', 'sector']
    result = re.findall(str_re, text)
    result1 = [x for x in result if x not in exceptions]
    print('or:', result1)
    print('count:', len(result1))
    print()
    return result1


def checkEr(text):
    str_re = r'(\w{3,}ers?)\b'
    result = re.findall(str_re, text)
    ex = ['khmer', 'over', 'under', 'after', 'later', 'hunger', 'former']
    result1 = [x for x in result if x.lower() not in ex]
    print('er:', result1)
    print('count:', len(result1))
    print()
    return result1


def checkTion(text):
    str_re = r'(\w{2,}tions?)\b'
    exceptions = ['nations']
    result = re.findall(str_re, text)
    result1 = [x for x in result if x.lower() not in exceptions]
    print('tion:', result1)
    print('count:', len(result1))
    print()
    return result1


def checkEnce(text):
    str_re = r'\b(\w{2,}ences?)\b'
    result = re.findall(str_re, text)
    print('ence:', result)
    print('count:', len(result))
    print()
    return result


def checkMent(text):
    str_re = r'\b(\w{2,}ment)\b'
    result = re.findall(str_re, text)
    print('ment:', result)
    print('count:', len(result))
    print()
    return result


def checkNominalization(text):
    nominalized = []
    nominalized.extend(checkIng(text))
    nominalized.extend(checkOr(text))
    nominalized.extend(checkTion(text))
    nominalized.extend(checkEr(text))
    nominalized.extend(checkEnce(text))
    nominalized.extend(checkMent(text))
    print('final:', nominalized)
    print('count:', len(nominalized))

checkNominalization(myText)

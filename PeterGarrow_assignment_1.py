"""Template for Assignment 1."""

from collections import defaultdict  # just like dict, but returns default if key not found  # noqa

# Singular-plural pairs to be used for evaluation
pairs = [('snake', 'snakes'),
         ('window', 'windows'),
         ('box', 'boxes'),
         ('boy', 'boys'),
         ('lorry', 'lorries'),
         ('potato', 'potatoes'),
         ('knife', 'knives'),
         ('girl', 'girls'),
         ('window', 'windows'),
         ('witch', 'witches'),
         ('gas', 'gases'),
         ('bus', 'buses'),
         ('kiss', 'kisses'),
         ('way', 'ways'),
         ('baby', 'babies'),
         ('hero', 'heroes'),
         ('echo', 'echoes'),
         ('embargo', 'embargoes'),
         ('tomato', 'tomatoes'),
         ('torpedo', 'torpedoes'),
         ('veto', 'vetoes'),
         ('auto', 'autos'),
         ('kangaroo', 'kangaroos'),
         ('kilo', 'kilos'),
         ('memo', 'memos'),
         ('photo', 'photos'),
         ('piano', 'pianos'),
         ('pimento', 'pimentos'),
         ('pro', 'pros'),
         ('solo', 'solos'),
         ('soprano', 'sopranos'),
         ('studio', 'studios'),
         ('tattoo', 'tattoos'),
         ('video', 'videos'),
         ('zoo', 'zoos'),
         ('buffalo', 'buffalos'),
         ('buffalo', 'buffaloes'),
         ('cargo', 'cargos'),
         ('cargo', 'cargoes'),
         ('halo', 'halos'),
         ('halo', 'haloes'),
         ('mosquito', 'mosquitos'),
         ('mosquito', 'mosquitoes'),
         ('motto', 'mottos'),
         ('motto', 'mottoes'),
         ('no', 'nos'),
         ('no', 'noes'),
         ('tornado', 'tornados'),
         ('tornado', 'tornadoes'),
         ('volcano', 'volcanos'),
         ('volcano', 'volcanoes'),
         ('zero', 'zeros'),
         ('zero', 'zeroes'),
         ('knife', 'knives'),
         ('leaf', 'leaves'),
         ('hoof', 'hooves'),
         ('life', 'lives'),
         ('self', 'selves'),
         ('elf', 'elves'),
         ('fish', 'fish'),
         ('sheep', 'sheep'),
         ('barracks', 'barracks'),
         ('foot', 'feet'),
         ('tooth', 'teeth'),
         ('goose', 'geese'),
         ('child', 'children'),
         ('man', 'men'),
         ('woman', 'women'),
         ('person', 'people'),
         ('mouse', 'mice'),
         ('deer', 'deer'),
         ('alga', 'algae'),
         ('amoeba', 'amoebae'),
         ('amoeba', 'amoebas'),
         ('antenna', 'antennae'),
         ('antenna', 'antennas'),
         ('formula', 'formulae'),
         ('formula', 'formulas'),
         ('larva', 'larvae'),
         ('nebula', 'nebulae'),
         ('nebula', 'nebulas'),
         ('vertebra', 'vertebrae'),
         ('corpus', 'corpora'),
         ('genus', 'genera'),
         ('alumnus', 'alumni'),
         ('bacillus', 'bacilli'),
         ('cactus', 'cacti'),
         ('cactus', 'cactuses'),
         ('focus', 'foci'),
         ('fungus', 'fungi'),
         ('fungus', 'funguses'),
         ('nucleus', 'nuclei'),
         ('octopus', 'octopi'),
         ('octopus', 'octopuses'),
         ('radius', 'radii'),
         ('stimulus', 'stimuli'),
         ('syllabus', 'syllabi'),
         ('syllabus', 'syllabuses'),
         ('terminus', 'termini'),
         ('addendum', 'addenda'),
         ('bacterium', 'bacteria'),
         ('curriculum', 'curricula'),
         ('curriculum', 'curriculums'),
         ('datum', 'data'),
         ('erratum', 'errata'),
         ('medium', 'media'),
         ('memorandum', 'memoranda'),
         ('memorandum', 'memorandums'),
         ('ovum', 'ova'),
         ('stratum', 'strata'),
         ('symposium', 'symposia'),
         ('symposium', 'symposiums'),
         ('apex', 'apices'),
         ('apex', 'apexes'),
         ('appendix', 'appendices'),
         ('appendix', 'appendixes'),
         ('cervix', 'cervices'),
         ('cervix', 'cervixes'),
         ('index', 'indices'),
         ('index', 'indexes'),
         ('matrix', 'matrices'),
         ('matrix', 'matrixes'),
         ('vortex', 'vortices'),
         ('analysis', 'analyses'),
         ('axis', 'axes'),
         ('basis', 'bases'),
         ('crisis', 'crises'),
         ('diagnosis', 'diagnoses'),
         ('emphasis', 'emphases'),
         ('hypothesis', 'hypotheses'),
         ('neurosis', 'neuroses'),
         ('oasis', 'oases'),
         ('parenthesis', 'parentheses'),
         ('synopsis', 'synopses'),
         ('thesis', 'theses'),
         ('criterion', 'criteria'),
         ('phenomenon', 'phenomena'),
         ('automaton', 'automata'),
         ('news', ''),
         ('gymnastics', ''),
         ('economics', ''),
         ('mathematics', ''),
         ('statistics', ''),
         ('luggage', ''),
         ('baggage', ''),
         ('furniture', ''),
         ('information', '')]

# dicts that map sg to list of pl, and pl to list of sg
sgpl_dict = defaultdict(list)
plsg_dict = defaultdict(list)
for sg, pl in pairs:
    sgpl_dict[sg].append(pl)
    plsg_dict[pl].append(sg)

irr_dict = {'tooth': 'teeth',
            'genus': 'genera',
            'fish': 'fish',
            'barracks': 'barracks',
            'child': 'children',
            'person': 'people',
            'mouse': 'mice',
            'goose': 'geese', }


def evaluate(func, input_type='sg'):
    """Evaluate the performance of pluralize function based on pairs data.

    func -- function that changes input word (default=pluralize)
    input_type -- 'sg' or 'pl'
    """
    assert input_type in ['sg', 'pl']
    if input_type == 'sg':
        pair_dict = sgpl_dict
    elif input_type == 'pl':
        pair_dict = plsg_dict
    total = len(pair_dict)
    # Determine how many lexemes have more than one plural form.
    # duplicates = len(set([i for i, j in pair_data]))
    correct = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for k, v in pair_dict.items():
        v = set(v)
        predicted = set(func(k))
        if v == predicted:
            print('correct:', k, '/'.join(predicted),
                  '({})'.format('/'.join(v)), sep='\t')
            tp += len(v)
            correct += 1
        else:
            print('INcorrect:', k, '/'.join(predicted),
                  '({})'.format('/'.join(v)), sep='\t')
        if len(v.difference(predicted)) > 0:
            fn += len(v.difference(predicted))
        if len(predicted.difference(v)) > 0:
            fp += len(predicted.difference(v))
        if len(v) == 0 and len(predicted) == 0:
            tn += 1
    print('accuracy:', correct, '/', total, '{:.2%}'.format(correct / total),
          '(for how many words did you get all plurals correct?)')
    print('precision:', tp, '/', tp + fp, '{:.2%}'.format(tp / (tp + fp)),
          '(of all predicted plurals, how many are correct?)')
    print('recall:', tp, '/', tp + fn, '{:.2%}'.format(tp / (tp + fn)),
          '(of all correct plural forms, how many do you predict?)')


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    if sg in irr_dict:
        return[irr_dict[sg]]
    elif sg.endswith('man'):
        return [sg[0:-3] + 'men']
    elif sg.endswith('us'):
        if sg == 'bus':
            return ['buses']
        elif sg.endswith('rpus'):
            return [sg[:-2] + 'ora']
        elif sg.endswith('tus') or sg.endswith('gus'):
            return [sg + 'es', sg[0:-2] + 'i']
        elif sg.endswith('opus') or sg.endswith('abus'):
            return [sg + 'es', sg[0:-2] + 'i']
        else:
            return [sg[0:-2] + 'i']
    elif sg.endswith('ews') or sg.endswith('ics'):
        return ['']
    elif sg.endswith('ggage') or sg.endswith('ure') or sg.endswith('tion'):
        return ['']
    elif sg.endswith('on'):
        return [sg[:-2] + 'a']
    elif sg.endswith('x'):
        if sg.endswith('pex') or sg.endswith('dex') or sg.endswith('ix'):
            return [sg[:-2] + 'ices', sg + 'es']
        elif sg.endswith('ex'):
            return [sg[:-2] + 'ices']
        else:
            return [sg + 'es']
    elif sg.endswith('um'):
        if sg.endswith('lum') or sg.endswith('andum'):
            return [sg + 's', sg[0:-2] + 'a']
        elif sg.endswith('sium'):
            return [sg[0:-2] + 'a', sg + 's']
        else:
            return [sg[0:-2] + 'a']
    elif sg.endswith('is'):
        return [sg[0:-2] + 'es']
    elif sg.endswith('f'):
        return [sg[0:-1] + 'ves']
    elif sg.endswith('fe'):
        return [sg[0:-2] + 'ves']
    elif 'ee' in sg:
        return [sg]
    elif 'oo' in sg[:-1]:
        return [sg.replace('oo', 'ee')]
    elif sg.endswith('s') or sg.endswith('x') or sg.endswith('ch'):
        return [sg + 'es']
    elif sg.endswith('y'):
        if sg[-2] in vowels:
            return [sg + 's']
        else:
            return [sg[0:-1] + 'ies']
    elif sg.endswith('o'):
        if sg.endswith('oo') or len(sg) == 3:
            return [sg + 's']
        elif sg.endswith('alo') or sg.endswith('tto') or sg.endswith('ito'):
            return [sg + 's', sg + 'es']
        elif sg.endswith('ado') or sg.endswith('cano'):
            return [sg + 's', sg + 'es']
        elif sg == 'no' or sg == 'cargo' or sg == 'zero':
            return [sg + 's', sg + 'es']
        elif sg.endswith('io') or sg.endswith('eo') or sg.endswith('nto'):
            return [sg + 's']
        elif (sg[-3] in vowels and sg[-3] not in ['a', 'e']):
            return [sg + 's']
        elif sg[-3] in vowels and sg[-4] in vowels:
            return [sg + 's']
        elif sg[-3] in vowels and sg[-2] in ['m', 'n']:
            return [sg + 's']
        else:
            return [sg + 'es']
    elif sg.endswith('a'):
        if sg.endswith('eba') or sg.endswith('ula') or sg.endswith('nna'):
            return [sg + 'e', sg + 's']
        else:
            return [sg + 'e']
    else:
        return [sg + 's']


print('evaluate pluralize function...')
evaluate(pluralize)

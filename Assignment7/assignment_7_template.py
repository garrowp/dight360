"""Template for assignment 8. (machine-learning)."""

import glob
import re
from string import punctuation as punct  # string of common punctuation chars

import matplotlib.pyplot as plt
import nltk
import pandas
from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# import model classes
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# TODO change to the location of your Mini-CORE corpus
MC_DIR = 'Mini-CORE/'


def clean(in_file):
    """Remove headers from corpus file."""
    out_str = ''
    for line in in_file:
        if re.match(r'<[hp]>', line):
            out_str += re.sub(r'<[hp]>', '', line)
    return out_str


def subcorp(name):
    """Extract subcorpus from filename.

    name -- filename

    The subcorpus is the first abbreviation after `1+`.
    """
    return name.split('+')[1]


def ttr(in_Text):
    """Compute type-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    return len(set(in_Text)) / len(in_Text)


def pro1_tr(in_Text):
    """Compute 1st person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    regex = r'(?:i|me|my|mine)$'
    pro1_count = len([i for i in in_Text if re.match(regex, i, re.I)])
    return pro1_count / len(in_Text)


def pro2_tr(in_Text):
    """Compute 2nd person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    regex = r'(?:ye|you(?:rs?)?)$'
    pro2_count = len([i for i in in_Text if re.match(regex, i, re.I)])
    return pro2_count / len(in_Text)


def pro3_tr(in_Text):
    """Compute 3rd person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    regex = r'(?:he|him|his|she|hers?|its?|they|them|theirs?)$'
    pro3_count = len([i for i in in_Text if re.match(regex, i, re.I)])
    return pro3_count / len(in_Text)


def punct_tr(in_Text):
    """Compute punctuation-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    punct_count = len([i for i in in_Text if re.match('[' + punct + ']+$', i)])
    return punct_count / len(in_Text)

def years_tr(in_Text):
    """Compute number of years

    in_Text -- nltk.Text object or list of strings
    """
    re_year = r'[0-9]{4}'

    year_count = len([x for x in in_Text if re.match(re_year, x)])

    return year_count / len(in_Text)

def end_punct_tr(in_Text):
    """Compute number of ending puncuation

    in_Text -- nltk.Text object or list of strings
    """

    re_punct = r'\b(\?|\.|!|\?|(?:\.\.\.))'

    end_punct_count = len([x for x in in_Text if re.match(re_punct, x)])

    return end_punct_count / len(in_Text)

def cont_tr(in_Text):
    """Compute number of contactions

    in_Text -- nltk.Text object or list of strings
    """

    re_cont = r'(\w\'(?:s|t|(?:ll)|(?:ve)|m|d))'

    cont_count = len([x for x in in_Text if re.match(re_cont, x)])

    return cont_count / len(in_Text)

def pro_total_tr(in_Text):
    """Compute total pronoun ratio

    in_Text -- nltk.Text object or list of strings
    """

    regex = r'(?:i|me|my|mine|ye|you(?:rs?)?|he|him|his|she|hers?|its?|they|them|theirs?)$'

    pro_count = len([x for x in in_Text if re.match(regex, x)])
    
    return pro_count / len(in_Text)

def noun_tr(in_Text):
    """Compute noun ratio

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    noun_count = len([x for x, y in in_Text_tagged if y.startswith('N')])

    return noun_count / len(in_Text)

def verb_tr(in_Text):
    """Count verb ratio

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    verb_count = len([x for x, y in in_Text_tagged if y.startswith('V')])

    return verb_count / len(in_Text)

def verb_noun(in_Text):
    """Verb to noun ration

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    verb_count = len([x for x, y in in_Text_tagged if y.startswith('V')])
    noun_count = len([x for x, y in in_Text_tagged if y.startswith('N')])

    return verb_count / noun_count

def adj_tr(in_Text):
    """Adjective ratio

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    adj_count = len([x for x, y in in_Text_tagged if y.startswith('J')])

    return adj_count / len(in_Text)

def adj_noun(in_Text):
    """Adjective to noun ratio

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    adj_count = len([x for x, y in in_Text_tagged if y.startswith('J')])
    noun_count = len([x for x, y in in_Text_tagged if y.startswith('N')])

    return adj_count  / noun_count

def adv_tr(in_Text):
    """Adverb ratio

    in_Text -- nltk.Text object or list of strings
    """    

    in_Text_tagged = nltk.pos_tag(in_Text)

    adv_count = len([x for x, y in in_Text_tagged if y.startswith('R')])

    return adv_count / len(in_Text)

def adv_verb(in_Text):
    """Adverb to verb ratio

    in_Text -- nltk.Text object or list of strings
    """  

    in_Text_tagged = nltk.pos_tag(in_Text)

    adv_count = len([x for x, y in in_Text_tagged if y.startswith('R')])
    verb_count = len([x for x, y in in_Text_tagged if y.startswith('V')])

    return adv_count / verb_count



def wh_tr(in_Text):
    """wh- ratio

    in_Text -- nltk.Text object or list of strings
    """

    in_Text_tagged = nltk.pos_tag(in_Text)

    wh_count = len([x for x, y in in_Text_tagged if y.startswith('W')])

    return wh_count / len(in_Text)
    
# add feature names HERE
feat_names = ['ttr', '1st-pro', '2nd-pro', '3rd-pro', 'punct', 'years', 'end-punct',
              'cont', 'total-pro', 'nouns', 'verbs', 'adj', 'adv', 'verb-noun', 'adj-noun',
              'adv_verb', 'wh-', 'genre']
with open('mc_feat_names.txt', 'w') as name_file:
    name_file.write('\t'.join(feat_names))

with open('mc_features.csv', 'w') as out_file:
    for f in glob.glob(MC_DIR + '*.txt'):
        print('.', end='', flush=True)  # show progress; print 1 dot per file
        with open(f) as the_file:
            raw_text = clean(the_file)
        tok_text = nltk.word_tokenize(raw_text)
        # call the function HERE
        print(ttr(tok_text), pro1_tr(tok_text), pro2_tr(tok_text),
              pro3_tr(tok_text), punct_tr(tok_text), years_tr(tok_text),
              end_punct_tr(tok_text), cont_tr(tok_text),
              pro_total_tr(tok_text), noun_tr(tok_text),
              verb_tr(tok_text), adj_tr(tok_text), adv_tr(tok_text), verb_noun(tok_text),
              adj_noun(tok_text), adv_verb(tok_text), wh_tr(tok_text), subcorp(f),
              sep=',', file=out_file)
    print()  # newline after progress dots

###############################################################################
# Do not change anything below this line! The assignment is simply to try to
# design useful features for the task by writing functions to extract those
# features. Simply write new functions and add a label to feat_names and call
# the function in the `print` function above that writes to out_file. MAKE SURE
# TO KEEP the order the same between feat_names and the print function, ALWAYS
# KEEPING `'genre'` AND `subcorp(f)` AS THE LAST ITEM!!

###############################################################################
# Load dataset
with open('mc_feat_names.txt') as name_file:
    names = name_file.read().strip().split('\t')
len_names = len(names)
with open('mc_features.csv') as mc_file:
    dataset = pandas.read_csv(mc_file, names=names,  # pandas DataFrame object
                              keep_default_na=False, na_values=['_'])  # avoid 'NA' category being interpreted as missing data  # noqa
print(type(dataset))

# Summarize the data
print('"Shape" of dataset:', dataset.shape,
      '({} instances of {} attributes)'.format(*dataset.shape))
print()
print('"head" of data:\n', dataset.head(20))  # head() is a method of DataFrame
print()
print('Description of data:\n:', dataset.describe())
print()
print('Class distribution:\n', dataset.groupby('genre').size())
print()

# Visualize the data
print('Drawing boxplot...')
grid_size = 0
while grid_size ** 2 < len_names:
    grid_size += 1
dataset.plot(kind='box', subplots=True, layout=(grid_size, grid_size),
             sharex=False, sharey=False)
fig = plt.gcf()  # get current figure
fig.savefig('boxplots.png')

# histograms
print('Drawing histograms...')
dataset.hist()
fig = plt.gcf()
fig.savefig('histograms.png')

# scatter plot matrix
print('Drawing scatterplot matrix...')
scatter_matrix(dataset)
fig = plt.gcf()
fig.savefig('scatter_matrix.png')
print()

print('Splitting training/development set and validation set...')
# Split-out validation dataset
array = dataset.values  # numpy array
feats = array[:,0:len_names - 1]  # to understand comma, see url in next line:
labels = array[:,-1]  #  https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#advanced-indexing
print('\tfull original data ([:5]) and their respective labels:')
print(feats[:5], labels[:5], sep='\n\n', end='\n\n\n')
validation_size = 0.20
seed = 7
feats_train, feats_validation, labels_train, labels_validation = model_selection.train_test_split(feats, labels, test_size=validation_size, random_state=seed)
# print('\ttraining data:\n', feats_train[:5],
#       '\ttraining labels:\n', labels_train[:5],
#       '\tvalidation data:\n', feats_validation[:5],
#       '\tvalidation labels:\n', labels_validation[:5], sep='\n\n')

# Test options and evaluation metric
seed = 7  # seeds the randomizer so that 'random' choices are the same in each run
scoring = 'accuracy'
print()

print('Initializing models...')
# Spot Check Algorithms
models = [('LR', LogisticRegression()),
          ('LDA', LinearDiscriminantAnalysis()),
          ('KNN', KNeighborsClassifier()),
          ('CART', DecisionTreeClassifier()),
          ('NB', GaussianNB()),
          ('SVM', SVC())]
print('Training and testing each model using 10-fold cross-validation...')
# evaluate each model in turn
results = []
names = []
for name, model in models:
    # https://chrisjmccormick.files.wordpress.com/2013/07/10_fold_cv.png
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, feats_train, labels_train,
                                                 cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = '{}: {} ({})'.format(name, cv_results.mean(), cv_results.std())
    print(msg)
print()

print('Drawing algorithm comparison boxplots...')
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
fig = plt.gcf()
fig.savefig('compare_algorithms.png')
print()

# Make predictions on validation dataset
# best_model = KNeighborsClassifier()
# best_model.fit(feats_train, labels_train)
# predictions = best_model.predict(feats_validation)
# print('Accuracy:', accuracy_score(labels_validation, predictions))
# print()
# print('Confusion matrix:')
# cm_labels = 'Iris-setosa Iris-versicolor Iris-virginica'.split()
# print('labels:', cm_labels)
# print(confusion_matrix(labels_validation, predictions, labels=cm_labels))
# print()
# print('Classification report:')
# print(classification_report(labels_validation, predictions))

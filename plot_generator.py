# Jonathan Lynch
# 5/23/20
# https://youtu.be/Vmr6pPs5snY
# "I have not given or received any unauthorized assistance on this assignment."

import random

class SimplePlotGenerator:
    'class that registers PlotViewer and generates a simple line'
    def registerPlotViewer(self, pv):                                              # create method registerPlotViewer that accepts an argument
        self.pv = pv                                                               # initialize argument pv
    def generate(self):                                                            # create method generate
        line = 'Something happens'                                                 # create string set to variable line
        return line                                                                # return line

class RandomPlotGenerator(SimplePlotGenerator):
    'class that inherits SimplePlotGenerator class and generates a random plot from seven files'
    def generate(self):                                                            # overwrite method generate
        name_list = open('plot_names.txt').readlines()                             # open plot_names.txt and read into a list of strings
        ran_name = random.choice(name_list)[:-1]                                   # choose random string from list, remove last character, and set to ran_name
        adjective_list = open('plot_adjectives.txt').readlines()                   # open plot_adjectives.txt and read into a list of strings
        ran_adj = random.choice(adjective_list)[:-1]                               # choose random string from list, remove last character, and set to ran_adj
        profession_list = open('plot_profesions.txt').readlines()                  # open plot_profesions.txt and read into a list of strings
        ran_prof = random.choice(profession_list)[:-1]                             # choose random string from list, remove last character, and set to ran_prof
        verb_list = open('plot_verbs.txt').readlines()                             # open plot_verbs.txt and read into a list of strings
        ran_verb = random.choice(verb_list)[:-1]                                   # choose random string from list, remove last character, and set to ran_verb
        evil_adjective_list = open('plot_adjectives_evil.txt').readlines()         # open plot_adjectives_evil.txt and read into a list of strings
        ran_evil = random.choice(evil_adjective_list)[:-1]                         # choose random string from list, remove last character, and set to ran_evil
        villian_job_list = open('plot_villian_job.txt').readlines()                # open plot_villian_job.txt and read into a list of strings
        ran_job = random.choice(villian_job_list)[:-1]                             # choose random string from list, remove last character, and set to ran_job                             
        villian_list = open('plot_villains.txt').readlines()                       # open plot_villains.txt and read into a list of strings
        ran_vil = random.choice(villian_list)[:-1]                                 # choose random string from list, remove last character, and set to ran_vil
        random_plot = ran_name + ', a ' + ran_adj + ' ' + ran_prof + ', must ' + ran_verb + ' the ' + ran_evil + ' ' + ran_job + ', ' + ran_vil + '.'      # concatenate seven strings to form a sentence
        return random_plot                                                                                                                                 # return sentence

def removeN(lst):                                                      # create function that accepts a list as input
    random.shuffle(lst)                                                # shuffle list
    new_list = []                                                      # create empty list new_list
    for string in lst:                                                 # iterate through list
        new_list.append(string[:-1])                                   # append each character of every string except last to new_list
    return str(new_list[:5])                                           # return the first five items in new_list as type string

class InteractivePlotGenerator(SimplePlotGenerator):
    'class that inherits SimplePlotGenerator class and generates a plot based on user responses'
    def generate(self):                                                                                      # overwrite method generate
        name_list = open('plot_names.txt').readlines()                                                       # open plot_names.txt and read into a list of strings
        names = removeN(name_list)                                                                           # use function removeN to retrieve five random list items saved as a string 
        res_name = self.pv.queryUser('Enter a name from the following list: ' + names + ': ')                # get user response via method queryUser of class PlotViewer, save as res_name
        adj_list = open('plot_adjectives.txt').readlines()                                                   # open plot_adjectives.txt and read into a list of strings
        adjs = removeN(adj_list)                                                                             # use function removeN to retrieve five random list items saved as a string
        res_adj = self.pv.queryUser('Enter an adjective from the following list: ' + adjs + ': ')            # get user response via method queryUser of class PlotViewer, save as res_adj
        prof_list = open('plot_profesions.txt').readlines()                                                  # open plot_profesions.txt and read into a list of strings
        profs = removeN(prof_list)                                                                           # use function removeN to retrieve five random list items saved as a string
        res_prof = self.pv.queryUser('Enter a profession from the following list: ' + profs + ': ')          # get user response via method queryUser of class PlotViewer, save as res_prof
        verb_list = open('plot_verbs.txt').readlines()                                                       # open plot_verbs.txt and read into a list of strings
        verbs = removeN(verb_list)                                                                           # use function removeN to retrieve five random list items saved as a string
        res_verb = self.pv.queryUser('Enter a verb from the following list: ' + verbs + ': ')                # get user response via method queryUser of class PlotViewer, save as res_verb
        evil_adj_list = open('plot_adjectives_evil.txt').readlines()                                         # open plot_adjectives_evil.txt and read into a list of strings
        evil_adjs = removeN(evil_adj_list)                                                                   # use function removeN to retrieve five random list items saved as a string
        res_evil = self.pv.queryUser('Enter an adjective from the following list: ' + evil_adjs + ': ')      # get user response via method queryUser of class PlotViewer, save as res_evil
        job_list = open('plot_villian_job.txt').readlines()                                                  # open plot_villian_job.txt and read into a list of strings
        jobs = removeN(job_list)                                                                             # use function removeN to retrieve five random list items saved as a string
        res_job = self.pv.queryUser('Enter a job from the following list: ' + jobs + ': ')                   # get user response via method queryUser of class PlotViewer, save as res_job
        villian_list = open('plot_villains.txt').readlines()                                                 # open plot_villains.txt and read into a list of strings
        vils = removeN(villian_list)                                                                         # use function removeN to retrieve five random list items saved as a string
        res_vils = self.pv.queryUser('Enter a name from the following list: ' + vils + ': ')                 # get user response via method queryUser of class PlotViewer, save as res_vils
        random_plot = res_name + ', a ' + res_adj + ' ' + res_prof + ', must ' + res_verb + ' the ' + res_evil + ' ' + res_job + ', ' + res_vils + '.'   # concatenate seven strings to form a sentence
        return random_plot                                                                                                                               # return sentence



    
        

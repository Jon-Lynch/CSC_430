# Jonathan Lynch
# Date
# _______
# "I have not given or received any unauthorized assistance on this assignment."

import random

class SimplePlotGenerator:
    def registerPlotViewer(self, pv):
        self.pv = pv
    def generate(self):
        line = 'Something happens'
        return line

class RandomPlotGenerator(SimplePlotGenerator):
    def generate(self):
        name_list = open('plot_names.txt').readlines()
        ran_name = random.choice(name_list)[:-1]
        adjective_list = open('plot_adjectives.txt').readlines()
        ran_adj = random.choice(adjective_list)[:-1]
        profession_list = open('plot_profesions.txt').readlines()
        ran_prof = random.choice(profession_list)[:-1]
        verb_list = open('plot_verbs.txt').readlines()
        ran_verb = random.choice(verb_list)[:-1]
        evil_adjective_list = open('plot_adjectives_evil.txt').readlines()
        ran_evil = random.choice(evil_adjective_list)[:-1]
        villian_job_list = open('plot_villian_job.txt').readlines()
        ran_job = random.choice(villian_job_list)[:-1]
        villian_list = open('plot_villains.txt').readlines()
        ran_vil = random.choice(villian_list)[:-1]
        random_plot = ran_name + ', a ' + ran_adj + ' ' + ran_prof + ', must ' + ran_verb + ' the ' + ran_evil + ' ' + ran_job + ', ' + ran_vil + '.'
        return random_plot

def removeN(lst):
    random.shuffle(lst)
    new_list = []
    for string in lst:
        new_list.append(string[:-1])
    return str(new_list[:5])

class InteractivePlotGenerator(SimplePlotGenerator):
    def generate(self):
        name_list = open('plot_names.txt').readlines()
        names = removeN(name_list)
        res_name = self.pv.queryUser('Enter a name from the following list: ' + names + ': ')
        adj_list = open('plot_adjectives.txt').readlines()
        adjs = removeN(adj_list)
        res_adj = self.pv.queryUser('Enter an adjective from the following list: ' + adjs + ': ')
        prof_list = open('plot_profesions.txt').readlines()
        profs = removeN(prof_list)
        res_prof = self.pv.queryUser('Enter a profession from the following list: ' + profs + ': ')
        verb_list = open('plot_verbs.txt').readlines()
        verbs = removeN(verb_list)
        res_verb = self.pv.queryUser('Enter a verb from the following list: ' + verbs + ': ')
        evil_adj_list = open('plot_adjectives_evil.txt').readlines()
        evil_adjs = removeN(evil_adj_list)
        res_evil = self.pv.queryUser('Enter an adjective from the following list: ' + evil_adjs + ': ')
        job_list = open('plot_villian_job.txt').readlines()
        jobs = removeN(job_list)
        res_job = self.pv.queryUser('Enter a job from the following list: ' + jobs + ': ')
        villian_list = open('plot_villains.txt').readlines()
        vils = removeN(villian_list)
        res_vils = self.pv.queryUser('Enter a name from the following list: ' + vils + ': ')
        random_plot = res_name + ', a ' + res_adj + ' ' + res_prof + ', must ' + res_verb + ' the ' + res_evil + ' ' + res_job + ', ' + res_vils + '.'
        return random_plot

class PlotViewer:
    def registerPlotGenerator(self, spg):
        self.spg = spg
        self.spg.registerPlotViewer(self)
    def queryUser(self, str):
        return input(str)
    def generate(self):
        print(self.spg.generate())

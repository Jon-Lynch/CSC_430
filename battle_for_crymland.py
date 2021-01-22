
import random


class Die:
    'create die class'

    def __init__(self, low=1, high=21):
        self.low = low
        self.high = high

    def roll(self):
        self.die = random.randrange(self.low, self.high)
        return self.die


class Die10(Die):
    'create 10-sided die from inheriting Die class'

    def roll(self):
        self.high = 5
        return Die.roll(self)


# def main()
file = open('file.txt').read().split()
weeks = int(file[0])
n_thieves = int(file[1])
heist_coef = int(file[2])
promotion_wealth = int(file[3])
n_detectives = int(file[4])
solve_init = float(file[5])
solve_cap = float(file[6])
init_bribe = float(file[7])
init_prob_discovered = float(file[8])


class Thief:

    thief_counter = 1

    def __init__(self, LT_ID):
        self.wealth = 0
        self.LT_ID = LT_ID

        self.thief_ID = Thief.thief_counter
        Thief.thief_counter += 1

    def award_wealth(self):
        die = Die()
        heist_value = heist_coef * (die.roll()**2)
        self.wealth += heist_value / 2
        for lieut in active_lieuts:
            if thief.get_LT_ID() == lieut.get_thief_ID():
                lieut.temp_wealth += heist_value / 2

    def get_thief_ID(self):
        return self.thief_ID

    def get_LT_ID(self):
        return self.LT_ID

    def get_wealth(self):
        return self.wealth

    def __repr__(self):
        return "Thief ID: {}".format(str(self.thief_ID))


class Lieutenant(Thief):

    def __init__(self, wealth, thief_ID, LT_ID, temp_wealth=0):
        self.temp_wealth = 0
        self.wealth = wealth
        self.LT_ID = LT_ID
        self.thief_ID = thief_ID

    def generate_thieves(self):
        for i in range(n_thieves):
            active_thieves.append(Thief(self.thief_ID))

    def give_wealth(self):
        self.wealth += self.temp_wealth / 2
        if lieut.get_thief_ID() == 0:
            self.wealth += self.temp_wealth / 2
            self.temp_wealth = 0

        for boss in active_lieuts:
            if lieut != boss and lieut.get_LT_ID() == boss.get_thief_ID():
                boss.temp_wealth += lieut.temp_wealth / 2
                self.temp_wealth = 0

    def get_temp_wealth(self):
        return self.temp_wealth

    def get_thieves(self):
        return active_thieves

    def __repr__(self):
        return "Thief ID: {}".format(str(self.thief_ID))


def promotion(active_lieuts, active_thieves):
    temp = []
    temp_lieuts = []
    temp_thieves = []
    for thief in active_thieves:
        if thief.get_wealth() >= promotion_wealth:
            temp_lieuts.append(thief)
    for thief in active_thieves:
        if thief.get_wealth() < promotion_wealth:
            temp_thieves.append(thief)
    active_thieves = temp_thieves
    for thief in temp_lieuts:
        thief = Lieutenant(thief.get_wealth(),
                           thief.get_thief_ID(), thief.get_LT_ID())
        temp.append(thief)
    return active_lieuts, temp, active_thieves

# for x in temp:
#    x.generate_thieves()
# active_lieuts = active_lieuts + temp


class Detective:

    det_counter = 1

    def __init__(self, cap_solve=solve_cap, solve_rate=.05):
        self.cap_solve = cap_solve
        self.solve_rate = solve_rate

        self.det_ID = Detective.det_counter
        Detective.det_counter += 1

        self.siezed_wealth = 0
        self.siezed_wealth_counter = 1

    def get_solve_rate(self):
        return self.solve_rate

    def increment_solve_rate(self):
        d = Die10()
        self.value = d.roll() / 100
        if self.solve_rate + self.value > self.cap_solve:
            self.solve_rate = self.cap_solve
        else:
            if self.solve_rate > 0:
                self.solve_rate += self.value

    def bribed(self):
        self.solve_rate = 0

    def solve_case(self):
        lst = [i for i in range(1, 101)]
        item = random.choice(lst)
        if self.solve_rate * 100 >= item:
            return True
        else:
            return False

    def get_det_ID(self):
        return self.det_ID

    def get_siezed_wealth(self):
        return self.siezed_wealth

    def get_siezed_wealth_counter(self):
        return self.siezed_wealth_counter

    def __repr__(self):
        return "Detective ID: {}".format(str(self.det_ID))


def jail_thieves(detectives, active_thieves, active_lieuts, jailed_thieves, captured, siezed_wealth):
    temp_det = []
    if len(active_thieves) >= len(detectives):
        temp_thieves = random.sample(active_thieves, len(detectives))
        for det in detectives:
            temp_det.append(det.solve_case())
    else:
        num = len(active_thieves)
        temp_thieves = random.sample(active_thieves, num)
        d = detectives[0:num]
        for det in d:
            temp_det.append(det.solve_case())

    for i in range(len(temp_det)):
        if temp_det[i] == True:
            jailed_thieves.append(temp_thieves[i])
            active_thieves.remove(temp_thieves[i])
            detectives[i].increment_solve_rate()
            siezed_wealth += jailed_thieves[-1].get_wealth()
            detectives[i].siezed_wealth += jailed_thieves[-1].get_wealth()

    testify = {}
    for jailed in jailed_thieves:
        if jailed.get_LT_ID() in testify:
            testify[jailed.get_LT_ID()] += 1
        else:
            testify[jailed.get_LT_ID()] = 1

    for key in testify:
        if testify[key] >= 3:
            num = key
            for lieut in active_lieuts:
                if lieut.get_thief_ID() == num:
                    jailed_thieves.append(lieut)
                    active_lieuts.remove(lieut)
                    siezed_wealth += jailed_thieves[-1].get_wealth()

    for jailed in jailed_thieves:
        if jailed.get_thief_ID() == 0:
            captured = True
        else:
            captured = False

    return detectives, active_thieves, active_lieuts, jailed_thieves, captured, siezed_wealth


def bribe(detectives, mrB_weekly_earnings):

    for det in detectives:
        if det.get_siezed_wealth() >= 1000000 * det.get_siezed_wealth_counter():
            bribe = .10 * (mrB_weekly_earnings[-1] - mrB_weekly_earnings[-2])
            det.siezed_wealth_counter += 1

            if bribe <= 10000:
                lst = [i for i in range(1, 101)]
                item = random.choice(lst)
                if 5 >= item:
                    det.bribed()
            elif bribe <= 100000:
                lst = [i for i in range(1, 101)]
                item = random.choice(lst)
                if 10 >= item:
                    det.bribed()
            elif bribe <= 1000000:
                lst = [i for i in range(1, 101)]
                item = random.choice(lst)
                if 25 >= item:
                    det.bribed()
            else:
                lst = [i for i in range(1, 101)]
                item = random.choice(lst)
                if 50 >= item:
                    det.bribed()

    return detectives


###############################################################################################


counter = 1
active_thieves = []
active_lieuts = []
jailed_thieves = []
siezed_wealth = 0
captured = False
mrB_weekly_earnings = []
mrB = Lieutenant(0, 0, 0)
active_lieuts.append(mrB)
detectives = [Detective() for i in range(3)]

for lieut in active_lieuts:
    lieut.generate_thieves()

outfile = open('crymland.txt', 'w')

while counter < 56 and captured == False:

    for thief in active_thieves:
        thief.award_wealth()

    for lieut in active_lieuts:
        lieut.give_wealth()

    mrB_weekly_earnings.append(active_lieuts[-1].get_wealth())

    active_lieuts, temp, active_thieves = promotion(
        active_lieuts, active_thieves)

    for x in temp:
        x.generate_thieves()
    active_lieuts = temp + active_lieuts

    detectives, active_thieves, active_lieuts, jailed_thieves, captured, siezed_wealth = jail_thieves(
        detectives, active_thieves, active_lieuts, jailed_thieves, captured, siezed_wealth)

    detectives = bribe(detectives, mrB_weekly_earnings)

    # print('week: ' + str(counter))  # print
    net_num = len(active_lieuts) + len(active_thieves)  # print

    # print('Criminal network number: ' + str(net_num))  # print

    # print('Jailed criminals: ' + str(len(jailed_thieves)))  # print

    # print('MrB personal wealth: ' + str(mrB.get_wealth()))  # print

    det_bribes = 0  # print
    for det in detectives:  # print
        if det.get_solve_rate() == 0:  # print
            det_bribes += 1  # print
    # print('Total bribes accepted: ' + str(det_bribes))  # print
    # print()

    outfile.write('week: ' + str(counter) + '\t' + str(net_num) + '\t' + str(len(
        jailed_thieves)) + '\t' + str(mrB.get_wealth()) + '\t' + str(det_bribes) + '\n')
    '''
    outfile.write(str(net_num) + '\t')
    outfile.write(str(len(jailed_thieves)) + '\t')
    outfile.write(str(mrB.get_wealth()) + '\t')
    outfile.write(str(det_bribes) + '\n')
    '''
    counter += 1

outfile.close()
print('week:')
print(counter - 1)

print('mrB captured status:')
print(captured)

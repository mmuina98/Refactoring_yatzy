class Yatzy:
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def chance(*args):
        return sum(args)

    # El código era demasiado largo y complejo. 
    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        return 50 if any(count == 5 for count in counts) else 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def ones(*args):
        sum = 0
        for arg in args:
            if arg == 1:
                sum += 1
        return sum
    
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def twos(*args):
        sum = 0
        for arg in args:
            if arg == 2:
                sum += 2
        return sum
    
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def threes(*args):
        sum = 0
        for arg in args:
            if arg == 3:
                sum += 3
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def fours(*args):
        sum = 0
        for arg in args:
            if arg == 4:
                sum += 4
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def fives(*args):
        sum = 0
        for arg in args:
            if arg == 5:
                sum += 5
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def sixes(*args):
        sum = 0
        for arg in args:
            if arg == 6:
                sum += 6
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def score_pair(*dice):
        counts = [0] * 6
        for die in dice:
            counts[die - 1] += 1
        for value in range(6, 0, -1):
            if counts[value - 1] == 2:
                return value * 2
        return 0
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def two_pair(*dice):
        counts = [0] * 6
        for die in dice:
            counts[die - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] >= 2:
                n += 1
                score += (6 - i)
        if n == 2:
            return score * 2
        else:
            return 0
        
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def four_of_a_kind(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def three_of_a_kind(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        for i in range(6):
            if tallies[i] >= 3:
                return (i + 1) * 3
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados
    @staticmethod
    def smallStraight(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        if all(count == 1 for count in tallies[:5]):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
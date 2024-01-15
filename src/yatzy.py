class Yatzy:
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def chance(*dice):
        return sum(dice)

    # El código era demasiado largo y complejo. 
    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        return 50 if any(count == 5 for count in counts) else 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def ones(*dice):
        sum_ones = sum(filter(lambda x: x == 1, dice))
        return sum_ones
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def twos(*dice):
        sum_twos = sum(filter(lambda x: x == 2, dice))
        return sum_twos
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def threes(*dice):
        sum_threes = sum(filter(lambda x: x == 3, dice))
        return sum_threes
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def fours(*dice):
        sum_fours = sum(filter(lambda x: x == 4, dice))
        return sum_fours
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def fives(*dice):
        sum_fives = sum(filter(lambda x: x == 5, dice))
        return sum_fives
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    # Utilice las funciones filter y lambda
    @staticmethod
    def sixes(*dice):
        sum_sixes = sum(filter(lambda x: x == 6, dice))
        return sum_sixes
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def score_pair(*dice):
        counts = [0] * 6
        for die in dice:
            counts[die - 1] += 1
        for value in range(6, 0, -1):
            if counts[value - 1] == 2:
                return value * 2
        return 0
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
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
        
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def four_of_a_kind(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def three_of_a_kind(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        for i in range(6):
            if tallies[i] >= 3:
                return (i + 1) * 3
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def smallStraight(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        if all(count == 1 for count in tallies[:5]):
            return 15
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def largeStraight(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        if all(count == 1 for count in tallies[1:6]):
            return 20
        return 0
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    @staticmethod
    def fullHouse(*dice):
        tallies = [0] * 6
        for die in dice:
            tallies[die - 1] += 1
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0
        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1
            elif tallies[i] == 3:
                _3 = True
                _3_at = i + 1
        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0
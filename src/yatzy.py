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
    @staticmethod
    def ones(*dice):
        sum = 0
        for die in dice:
            if die == 1:
                sum += 1
        return sum
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def twos(*dice):
        sum = 0
        for die in dice:
            if die == 2:
                sum += 2
        return sum
    
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def threes(*dice):
        sum = 0
        for die in dice:
            if die == 3:
                sum += 3
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def fours(*dice):
        sum = 0
        for die in dice:
            if die == 4:
                sum += 4
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def fives(*dice):
        sum = 0
        for die in dice:
            if die == 5:
                sum += 5
        return sum
    # Cambie para que se pueda usar siendo diferente de 5 dados Code smell:(Long Parameter List)
    # Cambie nombre parametro Code smell:(A routine has a poor name)
    @staticmethod
    def sixes(*dice):
        sum = 0
        for die in dice:
            if die == 6:
                sum += 6
        return sum
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
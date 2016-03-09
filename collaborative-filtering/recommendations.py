from math import sqrt
import matplotlib.pyplot as plt

# A dictionary of movie critics and their ratings of a small set of movies

critics = {
    'Lisa Rose':
        {
          'Lady in the Water':  2.5
        , 'Snakes on a Plane':  3.5
        , 'Just My Luck':       3.0
        , 'Superman Returns:':  3.5
        , 'You, Me and Dupree': 2.5
        , 'The Night Listener': 3.0
        }
  , 'Gene Seymour':
        {
          'Lady in the Water':  3.0
        , 'Snakes on a Plane':  3.5
        , 'Just My Luck':       1.5
        , 'Superman Returns:':  5.0
        , 'You, Me and Dupree': 3.5
        , 'The Night Listener': 3.0
        }
  , 'Michael Phillips':
        {
          'Lady in the Water':  2.5
        , 'Snakes on a Plane':  3.0
        , 'Superman Returns:':  3.5
        , 'The Night Listener': 4.0
        }
  , 'Claudia Puig':
        {
          'Snakes on a Plane':  3.5
        , 'Just My Luck':       3.0
        , 'Superman Returns:':  3.0
        , 'You, Me and Dupree': 2.5
        , 'The Night Listener': 4.5
        }
  , 'Mick LaSalle':
        {
          'Lady in the Water':  3.0
        , 'Snakes on a Plane':  4.0
        , 'Just My Luck':       2.0
        , 'Superman Returns:':  3.0
        , 'You, Me and Dupree': 2.0
        , 'The Night Listener': 3.0
        }
  , 'Jack Matthews':
        {
          'Lady in the Water':  3.0
        , 'Snakes on a Plane':  4.0
        , 'Superman Returns:':  5.0
        , 'You, Me and Dupree': 3.5
        , 'The Night Listener': 3.0
        }
  , 'Toby':
        {
          'Snakes on a Plane':  4.5
        , 'Superman Returns:':  4.0
        , 'You, Me and Dupree': 1.0
        }
}


# Euclidian distance
#  * Take the difference in each dimension
#  * Square them
#  * Add them together
#  * Take square root

# sqrt $ sum [ (a-b)**2 | a <- [a1, a2...], b <- [b1, b2...]]

# small distance => more similarity

# But we want higher values represent similarity
# reciprocal and add 1 to the denominator so we don't get a zero-division

# 1 / (1 + sqrt $ sum [ (a-b)**2 | a <- [a1, a2...], b <- [b1, b2...]])

# Interpretation:
#   * 1.0 ^= perfect similarity
#   * 0.0 ^= no similarity at all

def sim_distance(prefs, p1, p2):
    # get shared preferences
    shared_prefs = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
          shared_prefs[item] = 1

    # no shared preferences return 0
    if len(shared_prefs) == 0: return 0

    # add up the differences
    square_sums = sum( [pow(prefs[p1][i] - prefs[p2][i], 2) for i in shared_prefs] )

    return 1/(1 + sqrt(square_sums))

# Pearson distance correlation
# 

# Interpretation:
#   * + 1.0 total positive correlation
#   *   0.0 no correlation at all
#   * - 1.0 total negative correlation


def sim_pearson(prefs, p1, p2):
    # get shared preferences
    shared_prefs = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            shared_prefs[item] = 1

    n = len(shared_prefs)

    # no shared preferences return 0
    if n == 0: return 0

    # calc_sums :: Num a => [a] (exactly 5 items) lists, because tuples are not mutable...
    def calc_sums():
        # helper function for foldl
        def go(acc, it):
            acc[0] += prefs[p1][it]
            acc[1] += prefs[p2][it]
            acc[2] += pow(prefs[p1][it], 2)
            acc[3] += pow(prefs[p2][it], 2)
            acc[4] += prefs[p1][it] * prefs[p2][it]
            return acc

        return reduce(go, shared_prefs, [0, 0, 0, 0, 0])

    sum1, sum2, sum1_sq, sum2_sq, p_sum = tuple(calc_sums())

    # calculate pearson score
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))

    if den == 0: return 0

    return num / den

# variance :: (Num a) => [a] -> Double
def variance(values):

    n    = len(values)
    mean = sum(values) / n

    nsum = reduce (lambda acc, x: pow(x - mean, 2) + acc, values, 0)

    return nsum / n

# standart_deviation :: (Num a) => [a] -> Double
def standart_deviation(values):
    return sqrt(variance(values))


d1 = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
d2 = sim_distance(critics, 'Gene Seymour', 'Lisa Rose')
d3 = sim_distance(critics, 'Lisa Rose', 'Toby')
d4 = sim_distance(critics, 'Toby', 'Gene Seymour')

s1 = sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
s2 = sim_pearson(critics, 'Gene Seymour', 'Lisa Rose')
s3 = sim_pearson(critics, 'Lisa Rose', 'Toby')
s4 = sim_pearson(critics, 'Toby', 'Gene Seymour')

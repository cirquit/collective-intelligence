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
# 1.0 ^= perfect similarity

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


d1 = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
d2 = sim_distance(critics, 'Gene Seymour', 'Lisa Rose')
d3 = sim_distance(critics, 'Lisa Rose', 'Toby')
d4 = sim_distance(critics, 'Toby', 'Gene Seymour')

'''

def filmplots(prefs, f1, f2):
    # f1/f2 coordinates for every reviewer
    f1s = []
    f2s = []

    # get film review for every reviewer
    for p in prefs:
        if f1 in prefs[p]:
            f1s.append(prefs[p][f1])
        else:
            f1s.append(0)

        if f2 in prefs[p]:
            f2s.append(prefs[p][f2])
        else:
            f2s.append(0)

    plt.plot(f1s, f2s, 'ro')
    plt.show()


p1 = filmplots(critics, 'Just My Luck', 'Superman Returns')

'''
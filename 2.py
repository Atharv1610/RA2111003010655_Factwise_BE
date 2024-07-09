#There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
#In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
#Your score is the sum of the points of the cards you have taken.
#Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

def maxScore(cardPoints,k):
    n = len(cardPoints)
    if k>=n:
        return sum(cardPoints)
    
    win_sum = sum(cardPoints[:n-k])
    tot_sum = sum(cardPoints)
    max_score = tot_sum-win_sum

    for i in range (n-k,n):
        win_sum = win_sum - cardPoints[i-(n-k)]+cardPoints[i]
        max_score = max(max_score,tot_sum-win_sum)

    return max_score

test_case = 3
for i in range (test_case):
    c_input = input('Enter the card points seperated by commas: ')
    c_points = [int(x) for x in c_input.split(',')]

    k = int(input("Enter the number of cards to take (k): "))

    res = maxScore(c_points,k)
    print(f'The max score you can obtain is: {res}')
    print("\n")


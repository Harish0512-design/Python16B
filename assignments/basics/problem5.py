# 5.Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )

def check_vote_eligibility(age):
    # if age >= 18:
    #     return "Eligible for vote"
    # else:
    #     return "Not eligible for vote"
    return "Eligible for vote" if age >= 18 else "Not eligible for vote"


res = check_vote_eligibility(59)
print(res)

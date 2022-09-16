g = ["best", "good"]
b = ["worst", "unsatisfactory"]

rev = ["best food ever", "good but unsatisfactory", "worst customer service ever"]

def goodOrBad(reviews, goodWords, badWords):
    good = 0
    bad = 0
    sol = []

    for i in range(len(reviews)):
        words = reviews[i].split(" ")
        for j in range(len(words)):
            if words[j] in goodWords:
                good += 1
            elif words[j] in badWords:
                bad += 1
        print("index: "+str(i))
        print(good)
        print(bad)
        if good < bad:
            sol.append("bad")
        elif bad < good:
            sol.append("good")
        else:
            sol.append("neutral")
        good = 0
        bad = 0

    return sol


print(goodOrBad(rev, g, b))
D = input()

ANS = dict()
ANS["N"] = "S"
ANS["S"] = "N"
ANS["W"] = "E"
ANS["E"] = "W"
ANS["NE"] = "SW"
ANS["NW"] = "SE"
ANS["SW"] = "NE"
ANS["SE"] = "NW"

print(ANS[D])
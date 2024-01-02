def my_long_word(long, phrase):
    mots = ""
    mot_testé = ""
    for i in phrase:
        if i != " ":
            mot_testé += i
        else:
            long_mot = 0
            for i in mot_testé:
                long_mot += 1

            if long_mot > long:
                mots += mot_testé + " " 
            mot_testé = ""

    long_mot = 0
    for i in mot_testé:
        long_mot += 1

    if long_mot > long:
        mots += mot_testé

    return mots

resultat = my_long_word (3,"La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(resultat)
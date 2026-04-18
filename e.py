from Names import TabDeNom
from Races import LesRaces
import random


def FormatPourXcom():
    America = [
        "; ------------; ------------------------------------------",
        "; --------------AMERICAN------------------",
        "; ------------------------------------------"
    ]
    British=["; ------------------------------------------",
"; --------------ENGLISH------------------ -",
"; ------------------------------------------"]
    French=["; ------------------------------------------",
"; --------------FRENCH------------------ -",
"; ------------------------------------------"]
    Germany=["; ------------------------------------------",
"; --------------GERMAN------------------ -",
"; ------------------------------------------"]
    Russia=["; ------------------------------------------",
             "; --------------RUSSIAN------------------ -",
             "; ------------------------------------------"]
    China=["; ------------------------------------------",
"; --------------CHINESE------------------ -",
"; ------------------------------------------"]
    Japan=["; ------------------------------------------",
"; --------------JAPANESE------------------ -",
"; ------------------------------------------"]
    Korea=["; ------------------------------------------",
"; --------------SOUTH KOREAN------------------ -",
"; ------------------------------------------"]
    India=["; ------------------------------------------",
"; --------------INDIAN------------------ -",
"; ------------------------------------------",]
    Mexican=["; ------------------------------------------",
"; --------------MEXICAN------------------ -",
"; ------------------------------------------"]
    Africa=["; ------------------------------------------",
"; --------------AFRICAN------------------ -",
"; ------------------------------------------",]
    Australia=["; ------------------------------------------",
"; --------------AUSTRALIAN------------------ -",
"; ------------------------------------------"]
    Spain=["; ------------------------------------------",
"; --------------SPANISH------------------ -",
"; ------------------------------------------"
]
    Italy=["; ------------------------------------------",
"; --------------ITALIAN------------------ -",
"; ------------------------------------------"]
    Dutch=["; ------------------------------------------",
"; --------------DUTCH------------------ -",
"; ------------------------------------------"]
    Norway=["; ------------------------------------------",
"; --------------NORWEGIAN------------------ -",
"; ------------------------------------------"]
    Arabian=["; ------------------------------------------",
"; --------------Arabian------------------ -",
"; ------------------------------------------",
]
    Greek=["; ------------------------------------------",
"; --------------GREEK------------------ -",
"; ------------------------------------------"]
    Irish=["; ------------------------------------------",
"; --------------IRISH------------------ -",
"; ------------------------------------------"]
    Scottish=["; ------------------------------------------",
"; --------------SCOTTISH------------------ -",
"; ------------------------------------------"]
    Belgian=["; ------------------------------------------",
"; --------------BELGIAN------------------ -",
"; ------------------------------------------",]
    Turkish=["; ------------------------------------------",
"; --------------TURKISH------------------ -",
"; ------------------------------------------",]
    Israeli=["; ------------------------------------------",
"; --------------ISRAELI------------------ -"
"; ------------------------------------------",]
    Polish=["; ------------------------------------------",
"; --------------POLISH------------------ -",
"; ------------------------------------------"]


    for i in range(len(LesRaces["AMERICAN"]["m_arrAmMFirstNames"])):
        America.append(f"m_arrAmMFirstNames[{i}]=\"{LesRaces['AMERICAN']['m_arrAmMFirstNames'][i]}\"")

    for i in range(len(LesRaces["AMERICAN"]["m_arrAmFFirstNames"])):
        America.append(f"m_arrAmFFirstNames[{i}]=\"{LesRaces['AMERICAN']['m_arrAmFFirstNames'][i]}\"")

    for i in range(len(LesRaces["AMERICAN"]["m_arrAmLastNames"])):
        America.append(f"m_arrAmLastNames[{i}]=\"{LesRaces['AMERICAN']['m_arrAmLastNames'][i]}\"")

    for i in range(len(LesRaces["RUSSIAN"]["m_arrRsMFirstNames"])):
        Russia.append(f"m_arrRsMFirstNames[{i}]=\"{LesRaces['RUSSIAN']['m_arrRsMFirstNames'][i]}\"")

    for i in range(len(LesRaces["RUSSIAN"]["m_arrRsFFirstNames"])):
        Russia.append(f"m_arrRsFFirstNames[{i}]=\"{LesRaces['RUSSIAN']['m_arrRsFFirstNames'][i]}\"")

    for i in range(len(LesRaces["RUSSIAN"]["m_arrRsMLastNames"])):
        Russia.append(f"m_arrRsMLastNames[{i}]=\"{LesRaces['RUSSIAN']['m_arrRsMLastNames'][i]}\"")

    for i in range(len(LesRaces["RUSSIAN"]["m_arrRsFLastNames"])):
        Russia.append(f"m_arrRsFLastNames[{i}]=\"{LesRaces['RUSSIAN']['m_arrRsFLastNames'][i]}\"")

    for i in range(len(LesRaces["CHINESE"]["m_arrChMFirstNames"])):
        China.append(f"m_arrChMFirstNames[{i}]=\"{LesRaces['CHINESE']['m_arrChMFirstNames'][i]}\"")

    for i in range(len(LesRaces["CHINESE"]["m_arrChFFirstNames"])):
        China.append(f"m_arrChFFirstNames[{i}]=\"{LesRaces['CHINESE']['m_arrChFFirstNames'][i]}\"")

    for i in range(len(LesRaces["CHINESE"]["m_arrChLastNames"])):
        China.append(f"m_arrChLastNames[{i}]=\"{LesRaces['CHINESE']['m_arrChLastNames'][i]}\"")

    for i in range(len(LesRaces["INDIAN"]["m_arrInMFirstNames"])):
        India.append(f"m_arrInMFirstNames[{i}]=\"{LesRaces['INDIAN']['m_arrInMFirstNames'][i]}\"")

    for i in range(len(LesRaces["INDIAN"]["m_arrInFFirstNames"])):
        India.append(f"m_arrInFFirstNames[{i}]=\"{LesRaces['INDIAN']['m_arrInFFirstNames'][i]}\"")

    for i in range(len(LesRaces["INDIAN"]["m_arrInLastNames"])):
        India.append(f"m_arrInLastNames[{i}]=\"{LesRaces['INDIAN']['m_arrInLastNames'][i]}\"")


    for i in range(len(LesRaces["AFRICAN"]["m_arrAfMFirstNames"])):
        Africa.append(f"m_arrAfMFirstNames[{i}]=\"{LesRaces['AFRICAN']['m_arrAfMFirstNames'][i]}\"")

    for i in range(len(LesRaces["AFRICAN"]["m_arrAfFFirstNames"])):
        Africa.append(f"m_arrAfFFirstNames[{i}]=\"{LesRaces['AFRICAN']['m_arrAfFFirstNames'][i]}\"")

    for i in range(len(LesRaces["AFRICAN"]["m_arrAfLastNames"])):
        Africa.append(f"m_arrAfLastNames[{i}]=\"{LesRaces['AFRICAN']['m_arrAfLastNames'][i]}\"")


    for i in range(len(LesRaces["MEXICAN"]["m_arrMxMFirstNames"])):
        Mexican.append(f"m_arrMxMFirstNames[{i}]=\"{LesRaces['MEXICAN']['m_arrMxMFirstNames'][i]}\"")

    for i in range(len(LesRaces["MEXICAN"]["m_arrMxFFirstNames"])):
        Mexican.append(f"m_arrMxFFirstNames[{i}]=\"{LesRaces['MEXICAN']['m_arrMxFFirstNames'][i]}\"")

    for i in range(len(LesRaces["MEXICAN"]["m_arrMxLastNames"])):
        Mexican.append(f"m_arrMxLastNames[{i}]=\"{LesRaces['MEXICAN']['m_arrMxLastNames'][i]}\"")

    for i in range(len(LesRaces["Arabian"]["m_arrAbMFirstNames"])):
        Arabian.append(f"m_arrAbMFirstNames[{i}]=\"{LesRaces['Arabian']['m_arrAbMFirstNames'][i]}\"")

    for i in range(len(LesRaces["Arabian"]["m_arrAbFFirstNames"])):
        Arabian.append(f"m_arrAbFFirstNames[{i}]=\"{LesRaces['Arabian']['m_arrAbFFirstNames'][i]}\"")

    for i in range(len(LesRaces["Arabian"]["m_arrAbLastNames"])):
        Arabian.append(f"m_arrAbLastNames[{i}]=\"{LesRaces['Arabian']['m_arrAbLastNames'][i]}\"")

    for i in range(len(LesRaces["ENGLISH"]["m_arrEnMFirstNames"])):
        British.append(f"m_arrEnMFirstNames[{i}]=\"{LesRaces['ENGLISH']['m_arrEnMFirstNames'][i]}\"")

    for i in range(len(LesRaces["ENGLISH"]["m_arrEnFFirstNames"])):
        British.append(f"m_arrEnFFirstNames[{i}]=\"{LesRaces['ENGLISH']['m_arrEnFFirstNames'][i]}\"")

    for i in range(len(LesRaces["ENGLISH"]["m_arrEnLastNames"])):
        British.append(f"m_arrEnLastNames[{i}]=\"{LesRaces['ENGLISH']['m_arrEnLastNames'][i]}\"")

    for i in range(len(LesRaces["FRENCH"]["m_arrFrMFirstNames"])):
        French.append(f"m_arrFrMFirstNames[{i}]=\"{LesRaces['FRENCH']['m_arrFrMFirstNames'][i]}\"")

    for i in range(len(LesRaces["FRENCH"]["m_arrFrFFirstNames"])):
        French.append(f"m_arrFrFFirstNames[{i}]=\"{LesRaces['FRENCH']['m_arrFrFFirstNames'][i]}\"")

    for i in range(len(LesRaces["FRENCH"]["m_arrFrLastNames"])):
        French.append(f"m_arrFrLastNames[{i}]=\"{LesRaces['FRENCH']['m_arrFrLastNames'][i]}\"")

    for i in range(len(LesRaces["GERMAN"]["m_arrGmMFirstNames"])):
        Germany.append(f"m_arrGmMFirstNames[{i}]=\"{LesRaces['GERMAN']['m_arrGmMFirstNames'][i]}\"")


    for i in range(len(LesRaces["GERMAN"]["m_arrGmFFirstNames"])):
        Germany.append(f"m_arrGmFFirstNames[{i}]=\"{LesRaces['GERMAN']['m_arrGmFFirstNames'][i]}\"")


    for i in range(len(LesRaces["GERMAN"]["m_arrGmLastNames"])):
        Germany.append(f"m_arrGmLastNames[{i}]=\"{LesRaces['GERMAN']['m_arrGmLastNames'][i]}\"")

    for i in range(len(LesRaces["AUSTRALIAN"]["m_arrAuMFirstNames"])):
        Australia.append(f"m_arrAuMFirstNames[{i}]=\"{LesRaces['AUSTRALIAN']['m_arrAuMFirstNames'][i]}\"")

    for i in range(len(LesRaces["AUSTRALIAN"]["m_arrAuFFirstNames"])):
        Australia.append(f"m_arrAuFFirstNames[{i}]=\"{LesRaces['AUSTRALIAN']['m_arrAuFFirstNames'][i]}\"")


    for i in range(len(LesRaces["AUSTRALIAN"]["m_arrAuLastNames"])):
        Australia.append(f"m_arrAuLastNames[{i}]=\"{LesRaces['AUSTRALIAN']['m_arrAuLastNames'][i]}\"")

    for i in range(len(LesRaces["ITALIAN"]["m_arrItMFirstNames"])):
        Italy.append(f"m_arrItMFirstNames[{i}]=\"{LesRaces['ITALIAN']['m_arrItMFirstNames'][i]}\"")

    for i in range(len(LesRaces["ITALIAN"]["m_arrItFFirstNames"])):
        Italy.append(f"m_arrItFFirstNames[{i}]=\"{LesRaces['ITALIAN']['m_arrItFFirstNames'][i]}\"")

    for i in range(len(LesRaces["ITALIAN"]["m_arrItLastNames"])):
        Italy.append(f"m_arrItLastNames[{i}]=\"{LesRaces['ITALIAN']['m_arrItLastNames'][i]}\"")

    for i in range(len(LesRaces["JAPANESE"]["m_arrJpMFirstNames"])):
        Japan.append(f"m_arrJpMFirstNames[{i}]=\"{LesRaces['JAPANESE']['m_arrJpMFirstNames'][i]}\"")

    for i in range(len(LesRaces["JAPANESE"]["m_arrJpFFirstNames"])):
        Japan.append(f"m_arrJpFFirstNames[{i}]=\"{LesRaces['JAPANESE']['m_arrJpFFirstNames'][i]}\"")

    for i in range(len(LesRaces["JAPANESE"]["m_arrJpLastNames"])):
        Japan.append(f"m_arrJpLastNames[{i}]=\"{LesRaces['JAPANESE']['m_arrJpLastNames'][i]}\"")

    for i in range(len(LesRaces["ISRAELI"]["m_arrIsMFirstNames"])):
        Israeli.append(f"m_arrIsMFirstNames[{i}]=\"{LesRaces['ISRAELI']['m_arrIsMFirstNames'][i]}\"")

    for i in range(len(LesRaces["ISRAELI"]["m_arrIsFFirstNames"])):
        Israeli.append(f"m_arrIsFFirstNames[{i}]=\"{LesRaces['ISRAELI']['m_arrIsFFirstNames'][i]}\"")

    for i in range(len(LesRaces["ISRAELI"]["m_arrIsLastNames"])):
        Israeli.append(f"m_arrIsLastNames[{i}]=\"{LesRaces['ISRAELI']['m_arrIsLastNames'][i]}\"")

    for i in range(len(LesRaces["SPANISH"]["m_arrEsMFirstNames"])):
        Spain.append(f"m_arrEsMFirstNames[{i}]=\"{LesRaces['SPANISH']['m_arrEsMFirstNames'][i]}\"")

    for i in range(len(LesRaces["SPANISH"]["m_arrEsFFirstNames"])):
        Spain.append(f"m_arrEsFFirstNames[{i}]=\"{LesRaces['SPANISH']['m_arrEsFFirstNames'][i]}\"")

    for i in range(len(LesRaces["SPANISH"]["m_arrEsLastNames"])):
        Spain.append(f"m_arrEsLastNames[{i}]=\"{LesRaces['SPANISH']['m_arrEsLastNames'][i]}\"")

    for i in range(len(LesRaces["GREEK"]["m_arrGrMFirstNames"])):
        Greek.append(f"m_arrGrMFirstNames[{i}]=\"{LesRaces['GREEK']['m_arrGrMFirstNames'][i]}\"")

    for i in range(len(LesRaces["GREEK"]["m_arrGrFFirstNames"])):
        Greek.append(f"m_arrGrFFirstNames[{i}]=\"{LesRaces['GREEK']['m_arrGrFFirstNames'][i]}\"")

    for i in range(len(LesRaces["GREEK"]["m_arrGrLastNames"])):
        Greek.append(f"m_arrGrLastNames[{i}]=\"{LesRaces['GREEK']['m_arrGrLastNames'][i]}\"")

    for i in range(len(LesRaces["NORWEGIAN"]["m_arrNwMFirstNames"])):
        Norway.append(f"m_arrNwMFirstNames[{i}]=\"{LesRaces['NORWEGIAN']['m_arrNwMFirstNames'][i]}\"")

    for i in range(len(LesRaces["NORWEGIAN"]["m_arrNwFFirstNames"])):
        Norway.append(f"m_arrNwFFirstNames[{i}]=\"{LesRaces['NORWEGIAN']['m_arrNwFFirstNames'][i]}\"")

    for i in range(len(LesRaces["NORWEGIAN"]["m_arrNwLastNames"])):
        Norway.append(f"m_arrNwLastNames[{i}]=\"{LesRaces['NORWEGIAN']['m_arrNwLastNames'][i]}\"")

    for i in range(len(LesRaces["IRISH"]["m_arrIrMFirstNames"])):
        Irish.append(f"m_arrIrMFirstNames[{i}]=\"{LesRaces['IRISH']['m_arrIrMFirstNames'][i]}\"")

    for i in range(len(LesRaces["IRISH"]["m_arrIrFFirstNames"])):
        Irish.append(f"m_arrIrFFirstNames[{i}]=\"{LesRaces['IRISH']['m_arrIrFFirstNames'][i]}\"")

    for i in range(len(LesRaces["IRISH"]["m_arrIrLastNames"])):
        Irish.append(f"m_arrIrLastNames[{i}]=\"{LesRaces['IRISH']['m_arrIrLastNames'][i]}\"")

    for i in range(len(LesRaces["SOUTH KOREAN"]["m_arrSkMFirstNames"])):
        Korea.append(f"m_arrSkMFirstNames[{i}]=\"{LesRaces['SOUTH KOREAN']['m_arrSkMFirstNames'][i]}\"")

    for i in range(len(LesRaces["SOUTH KOREAN"]["m_arrSkFFirstNames"])):
        Korea.append(f"m_arrSkFFirstNames[{i}]=\"{LesRaces['SOUTH KOREAN']['m_arrSkFFirstNames'][i]}\"")

    for i in range(len(LesRaces["SOUTH KOREAN"]["m_arrSkLastNames"])):
        Korea.append(f"m_arrSkLastNames[{i}]=\"{LesRaces['SOUTH KOREAN']['m_arrSkLastNames'][i]}\"")

    for i in range(len(LesRaces["DUTCH"]["m_arrDuMFirstNames"])):
        Dutch.append(f"m_arrDuMFirstNames[{i}]=\"{LesRaces['DUTCH']['m_arrDuMFirstNames'][i]}\"")

    for i in range(len(LesRaces["DUTCH"]["m_arrDuFFirstNames"])):
        Dutch.append(f"m_arrDuFFirstNames[{i}]=\"{LesRaces['DUTCH']['m_arrDuFFirstNames'][i]}\"")

    for i in range(len(LesRaces["DUTCH"]["m_arrDuLastNames"])):
        Dutch.append(f"m_arrDuLastNames[{i}]=\"{LesRaces['DUTCH']['m_arrDuLastNames'][i]}\"")

    for i in range(len(LesRaces["SCOTTISH"]["m_arrScMFirstNames"])):
        Scottish.append(f"m_arrScMFirstNames[{i}]=\"{LesRaces['SCOTTISH']['m_arrScMFirstNames'][i]}\"")

    for i in range(len(LesRaces["SCOTTISH"]["m_arrScFFirstNames"])):
        Scottish.append(f"m_arrScFFirstNames[{i}]=\"{LesRaces['SCOTTISH']['m_arrScFFirstNames'][i]}\"")

    for i in range(len(LesRaces["SCOTTISH"]["m_arrScLastNames"])):
        Scottish.append(f"m_arrScLastNames[{i}]=\"{LesRaces['SCOTTISH']['m_arrScLastNames'][i]}\"")

    for i in range(len(LesRaces["BELGIAN"]["m_arrBgMFirstNames"])):
        Belgian.append(f"m_arrBgMFirstNames[{i}]=\"{LesRaces['BELGIAN']['m_arrBgMFirstNames'][i]}\"")

    for i in range(len(LesRaces["BELGIAN"]["m_arrBgFFirstNames"])):
        Belgian.append(f"m_arrBgFFirstNames[{i}]=\"{LesRaces['BELGIAN']['m_arrBgFFirstNames'][i]}\"")

    for i in range(len(LesRaces["BELGIAN"]["m_arrBgLastNames"])):
        Belgian.append(f"m_arrBgLastNames[{i}]=\"{LesRaces['BELGIAN']['m_arrBgLastNames'][i]}\"")

    for i in range(len(LesRaces["POLISH"]["m_arrPlMFirstNames"])):
        Polish.append(f"m_arrPlMFirstNames[{i}]=\"{LesRaces['POLISH']['m_arrPlMFirstNames'][i]}\"")

    for i in range(len(LesRaces["POLISH"]["m_arrPlMLastNames"])):
        Polish.append(f"m_arrPlMLastNames[{i}]=\"{LesRaces['POLISH']['m_arrPlMLastNames'][i]}\"")

    for i in range(len(LesRaces["POLISH"]["m_arrPlFFirstNames"])):
        Polish.append(f"m_arrPlFFirstNames[{i}]=\"{LesRaces['POLISH']['m_arrPlFFirstNames'][i]}\"")

    for i in range(len(LesRaces["POLISH"]["m_arrPlFLastNames"])):
        Polish.append(f"m_arrPlFLastNames[{i}]=\"{LesRaces['POLISH']['m_arrPlFLastNames'][i]}\"")

    for i in range(len(LesRaces["TURKISH"]["m_arrTkMFirstNames"])):
        Turkish.append(f"m_arrTkMFirstNames[{i}]=\"{LesRaces['TURKISH']['m_arrTkMFirstNames'][i]}\"")

    for i in range(len(LesRaces["TURKISH"]["m_arrTkMLastNames"])):
        Turkish.append(f"m_arrTkMLastNames[{i}]=\"{LesRaces['TURKISH']['m_arrTkMLastNames'][i]}\"")

    for i in range(len(LesRaces["TURKISH"]["m_arrTkFFirstNames"])):
        Turkish.append(f"m_arrTkFFirstNames[{i}]=\"{LesRaces['TURKISH']['m_arrTkFFirstNames'][i]}\"")

    for i in range(len(LesRaces["TURKISH"]["m_arrTkFLastNames"])):
        Turkish.append(f"m_arrTkFLastNames[{i}]=\"{LesRaces['TURKISH']['m_arrTkFLastNames'][i]}\"")

    print('\n'.join(
        America + British + French + Germany + Russia + China + Japan + Korea + India + Mexican + Africa + Australia + Spain + Italy + Dutch + Norway + Arabian + Greek + Irish + Scottish + Belgian + Turkish + Israeli + Polish))




def character_name_generator(characters):

    for i in characters:

        nomTemp = characters[i]["nom"]
        prenomTemp = characters[i]["prenom"]

        # ---------------- AMERICAN ----------------
        if characters[i]["race"] == 0:
            LesRaces["AMERICAN"]["m_arrAmLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["AMERICAN"]["m_arrAmMFirstNames"].append(prenomTemp)
            else:
                LesRaces["AMERICAN"]["m_arrAmFFirstNames"].append(prenomTemp)

        # ---------------- BRITISH ----------------
        if characters[i]["race"] == 1:
            LesRaces["ENGLISH"]["m_arrEnLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["ENGLISH"]["m_arrEnMFirstNames"].append(prenomTemp)
            else:
                LesRaces["ENGLISH"]["m_arrEnFFirstNames"].append(prenomTemp)

        # ---------------- FRENCH ----------------
        if characters[i]["race"] == 2:
            LesRaces["FRENCH"]["m_arrFrLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["FRENCH"]["m_arrFrMFirstNames"].append(prenomTemp)
            else:
                LesRaces["FRENCH"]["m_arrFrFFirstNames"].append(prenomTemp)

        # ---------------- GERMAN ----------------
        if characters[i]["race"] == 3:
            LesRaces["GERMAN"]["m_arrGmLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["GERMAN"]["m_arrGmMFirstNames"].append(prenomTemp)
            else:
                LesRaces["GERMAN"]["m_arrGmFFirstNames"].append(prenomTemp)

        # ---------------- RUSSIAN ----------------
        if characters[i]["race"] == 4:
            if random.choice([True, False]):
                LesRaces["RUSSIAN"]["m_arrRsMLastNames"].append(nomTemp)
                LesRaces["RUSSIAN"]["m_arrRsMFirstNames"].append(prenomTemp)
            else:
                LesRaces["RUSSIAN"]["m_arrRsFLastNames"].append(nomTemp)
                LesRaces["RUSSIAN"]["m_arrRsFFirstNames"].append(prenomTemp)

        # ---------------- CHINESE ----------------
        if characters[i]["race"] == 5:
            LesRaces["CHINESE"]["m_arrChLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["CHINESE"]["m_arrChMFirstNames"].append(prenomTemp)
            else:
                LesRaces["CHINESE"]["m_arrChFFirstNames"].append(prenomTemp)

        # ---------------- JAPANESE ----------------
        if characters[i]["race"] == 6:
            LesRaces["JAPANESE"]["m_arrJpLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["JAPANESE"]["m_arrJpMFirstNames"].append(prenomTemp)
            else:
                LesRaces["JAPANESE"]["m_arrJpFFirstNames"].append(prenomTemp)

        # ---------------- SOUTH KOREAN ----------------
        if characters[i]["race"] == 7:
            LesRaces["SOUTH KOREAN"]["m_arrSkLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["SOUTH KOREAN"]["m_arrSkMFirstNames"].append(prenomTemp)
            else:
                LesRaces["SOUTH KOREAN"]["m_arrSkFFirstNames"].append(prenomTemp)

        # ---------------- INDIAN ----------------
        if characters[i]["race"] == 8:
            LesRaces["INDIAN"]["m_arrInLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["INDIAN"]["m_arrInMFirstNames"].append(prenomTemp)
            else:
                LesRaces["INDIAN"]["m_arrInFFirstNames"].append(prenomTemp)

        # ---------------- MEXICAN ----------------
        if characters[i]["race"] == 9:
            LesRaces["MEXICAN"]["m_arrMxLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["MEXICAN"]["m_arrMxMFirstNames"].append(prenomTemp)
            else:
                LesRaces["MEXICAN"]["m_arrMxFFirstNames"].append(prenomTemp)

        # ---------------- AFRICAN ----------------
        if characters[i]["race"] == 10:
            LesRaces["AFRICAN"]["m_arrAfLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["AFRICAN"]["m_arrAfMFirstNames"].append(prenomTemp)
            else:
                LesRaces["AFRICAN"]["m_arrAfFFirstNames"].append(prenomTemp)

        # ---------------- AUSTRALIAN ----------------
        if characters[i]["race"] == 11:
            LesRaces["AUSTRALIAN"]["m_arrAuLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["AUSTRALIAN"]["m_arrAuMFirstNames"].append(prenomTemp)
            else:
                LesRaces["AUSTRALIAN"]["m_arrAuFFirstNames"].append(prenomTemp)

        # ---------------- SPANISH ----------------
        if characters[i]["race"] == 12:
            LesRaces["SPANISH"]["m_arrEsLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["SPANISH"]["m_arrEsMFirstNames"].append(prenomTemp)
            else:
                LesRaces["SPANISH"]["m_arrEsFFirstNames"].append(prenomTemp)

        # ---------------- ITALIAN ----------------
        if characters[i]["race"] == 13:
            LesRaces["ITALIAN"]["m_arrItLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["ITALIAN"]["m_arrItMFirstNames"].append(prenomTemp)
            else:
                LesRaces["ITALIAN"]["m_arrItFFirstNames"].append(prenomTemp)

        # ---------------- DUTCH ----------------
        if characters[i]["race"] == 14:
            LesRaces["DUTCH"]["m_arrDuLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["DUTCH"]["m_arrDuMFirstNames"].append(prenomTemp)
            else:
                LesRaces["DUTCH"]["m_arrDuFFirstNames"].append(prenomTemp)

        # ---------------- NORWEGIAN ----------------
        if characters[i]["race"] == 15:
            LesRaces["NORWEGIAN"]["m_arrNwLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["NORWEGIAN"]["m_arrNwMFirstNames"].append(prenomTemp)
            else:
                LesRaces["NORWEGIAN"]["m_arrNwFFirstNames"].append(prenomTemp)

        # ---------------- Arabian ----------------
        if characters[i]["race"] == 16:
            LesRaces["Arabian"]["m_arrAbLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["Arabian"]["m_arrAbMFirstNames"].append(prenomTemp)
            else:
                LesRaces["Arabian"]["m_arrAbFFirstNames"].append(prenomTemp)

        # ---------------- ISRAELI ----------------
        if characters[i]["race"] == 17:
            LesRaces["ISRAELI"]["m_arrIsLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["ISRAELI"]["m_arrIsMFirstNames"].append(prenomTemp)
            else:
                LesRaces["ISRAELI"]["m_arrIsFFirstNames"].append(prenomTemp)

        # ---------------- SCOTTISH ----------------
        if characters[i]["race"] == 18:
            LesRaces["SCOTTISH"]["m_arrScLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["SCOTTISH"]["m_arrScMFirstNames"].append(prenomTemp)
            else:
                LesRaces["SCOTTISH"]["m_arrScFFirstNames"].append(prenomTemp)

        # ---------------- IRISH ----------------
        if characters[i]["race"] == 19:
            LesRaces["IRISH"]["m_arrIrLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["IRISH"]["m_arrIrMFirstNames"].append(prenomTemp)
            else:
                LesRaces["IRISH"]["m_arrIrFFirstNames"].append(prenomTemp)

        # ---------------- BELGIAN ----------------
        if characters[i]["race"] == 20:
            LesRaces["BELGIAN"]["m_arrBgLastNames"].append(nomTemp)
            if random.choice([True, False]):
                LesRaces["BELGIAN"]["m_arrBgMFirstNames"].append(prenomTemp)
            else:
                LesRaces["BELGIAN"]["m_arrBgFFirstNames"].append(prenomTemp)

        # ---------------- TURKISH ----------------
        if characters[i]["race"] == 21:
            if random.choice([True, False]):
                LesRaces["TURKISH"]["m_arrTkMLastNames"].append(nomTemp)
                LesRaces["TURKISH"]["m_arrTkMFirstNames"].append(prenomTemp)
            else:
                LesRaces["TURKISH"]["m_arrTkFLastNames"].append(nomTemp)
                LesRaces["TURKISH"]["m_arrTkFFirstNames"].append(prenomTemp)

        # ---------------- POLISH ----------------
        if characters[i]["race"] == 22:
            if random.choice([True, False]):
                LesRaces["POLISH"]["m_arrPlMLastNames"].append(nomTemp)
                LesRaces["POLISH"]["m_arrPlMFirstNames"].append(prenomTemp)
            else:
                LesRaces["POLISH"]["m_arrPlFLastNames"].append(nomTemp)
                LesRaces["POLISH"]["m_arrPlFFirstNames"].append(prenomTemp)

        # ---------------- GREEK ----------------
        if characters[i]["race"] == 23:
                LesRaces["GREEK"]["m_arrGrLastNames"].append(nomTemp)
                if random.choice([True, False]):
                    LesRaces["GREEK"]["m_arrGrMFirstNames"].append(prenomTemp)
                else:
                    LesRaces["GREEK"]["m_arrGrFFirstNames"].append(prenomTemp)

    return FormatPourXcom()




def random_number_generator(nom,prenom):
    prenom_utilises = set()
    nom_utilises = set()

    taille_nom= len(nom)
    taille_prenom= len(prenom)
    characters={}
    i=1
    prenom_attendue = set(range(taille_prenom))
    nom_attendue = set(range(taille_nom))

    while nom_utilises != nom_attendue or prenom_utilises != prenom_attendue:
        index_nom = random.randint(0,taille_nom-1)
        index_prenom = random.randint(0,taille_prenom-1)

        characters[f"personnage{i}"] = { "nom" : nom[index_nom], "prenom": prenom[index_prenom] ,
        "race" : random.randint(0,23)}


        nom_utilises.add(index_nom)
        prenom_utilises.add(index_prenom)
        i += 1

    return character_name_generator(characters)




def generateur_de_valeur_pourtabs(tableau):
    # commence ici c'est ce qui vas appeler la première fonction puis les autres
    tableau_nom=[]
    tableau_prenom=[]
    poidNom=1
    poidPrenom=1
    for i in tableau :
        poidNom += len(tableau_prenom)
        poidPrenom += len(tableau_nom)
        if random.choices([True,False], weights=[poidNom,poidPrenom])[0] :
            tableau_nom.append(i)
        else :
            tableau_prenom.append(i)

    return random_number_generator(tableau_nom,tableau_prenom)

print(generateur_de_valeur_pourtabs(TabDeNom))
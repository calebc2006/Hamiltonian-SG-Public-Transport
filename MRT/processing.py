import json

data = [
    { "codes": ["BP10"], "id": 1, "adjacencies": [2, 11] },
    { "codes": ["BP11"], "id": 2, "adjacencies": [1, 3] },
    { "codes": ["BP12"], "id": 3, "adjacencies": [2, 4] },
    { "codes": ["BP13"], "id": 4, "adjacencies": [3, 35] },
    { "codes": ["BP2"], "id": 5, "adjacencies": [6, 127] },
    { "codes": ["BP3"], "id": 6, "adjacencies": [5, 7] },
    { "codes": ["BP4"], "id": 7, "adjacencies": [6, 8] },
    { "codes": ["BP5"], "id": 8, "adjacencies": [7, 35] },
    { "codes": ["BP7"], "id": 9, "adjacencies": [10, 35] },
    { "codes": ["BP8"], "id": 10, "adjacencies": [9, 11] },
    { "codes": ["BP9"], "id": 11, "adjacencies": [1, 10] },
    { "codes": ["CC10", "DT26"], "id": 12, "adjacencies": [13, 89, 47, 48] },
    { "codes": ["CC11"], "id": 13, "adjacencies": [12, 14] },
    { "codes": ["CC12"], "id": 14, "adjacencies": [13, 94] },
    { "codes": ["CC14"], "id": 15, "adjacencies": [94, 113] },
    { "codes": ["CC16"], "id": 16, "adjacencies": [17, 113] },
    { "codes": ["CC17", "TE9"], "id": 17, "adjacencies": [16, 165] },
    { "codes": ["CC19", "DT9"], "id": 18, "adjacencies": [20, 36, 60] },
    { "codes": ["CC2"], "id": 19, "adjacencies": [28, 121] },
    { "codes": ["CC20"], "id": 20, "adjacencies": [18, 21] },
    { "codes": ["CC21"], "id": 21, "adjacencies": [20, 72] },
    { "codes": ["CC23"], "id": 22, "adjacencies": [23, 72] },
    { "codes": ["CC24"], "id": 23, "adjacencies": [22, 24] },
    { "codes": ["CC25"], "id": 24, "adjacencies": [23, 25] },
    { "codes": ["CC26"], "id": 25, "adjacencies": [24, 26] },
    { "codes": ["CC27"], "id": 26, "adjacencies": [25, 27] },
    { "codes": ["CC28"], "id": 27, "adjacencies": [26, 91] },
    { "codes": ["CC3"], "id": 28, "adjacencies": [19, 29] },
    { "codes": ["CC4", "DT15"], "id": 29, "adjacencies": [28, 30, 64, 38] },
    { "codes": ["CC5"], "id": 30, "adjacencies": [29, 31] },
    { "codes": ["CC6"], "id": 31, "adjacencies": [30, 32] },
    { "codes": ["CC7"], "id": 32, "adjacencies": [31, 33] },
    { "codes": ["CC8"], "id": 33, "adjacencies": [32, 89] },
    { "codes": ["CG2"], "id": 34, "adjacencies": [56] },
    { "codes": ["DT1", "BP6"], "id": 35, "adjacencies": [41, 8, 9, 4] },
    { "codes": ["DT10"], "id": 36, "adjacencies": [18, 118] },
    { "codes": ["DT13"], "id": 37, "adjacencies": [64, 102] },
    { "codes": ["DT16", "CE1"], "id": 38, "adjacencies": [29, 39, 124] },
    { "codes": ["DT17"], "id": 39, "adjacencies": [38, 40] },
    { "codes": ["DT18"], "id": 40, "adjacencies": [39, 100] },
    { "codes": ["DT2"], "id": 41, "adjacencies": [35, 51] },
    { "codes": ["DT20"], "id": 42, "adjacencies": [43, 100] },
    { "codes": ["DT21"], "id": 43, "adjacencies": [42, 44] },
    { "codes": ["DT22"], "id": 44, "adjacencies": [43, 45] },
    { "codes": ["DT23"], "id": 45, "adjacencies": [44, 46] },
    { "codes": ["DT24"], "id": 46, "adjacencies": [45, 47] },
    { "codes": ["DT25"], "id": 47, "adjacencies": [12, 46] },
    { "codes": ["DT27"], "id": 48, "adjacencies": [12, 49] },
    { "codes": ["DT28"], "id": 49, "adjacencies": [48, 50] },
    { "codes": ["DT29"], "id": 50, "adjacencies": [49, 52] },
    { "codes": ["DT3"], "id": 51, "adjacencies": [41] },
    { "codes": ["DT30"], "id": 52, "adjacencies": [50, 53] },
    { "codes": ["DT31"], "id": 53, "adjacencies": [52, 70] },
    { "codes": ["DT33"], "id": 54, "adjacencies": [55, 70] },
    { "codes": ["DT34"], "id": 55, "adjacencies": [54, 56] },
    { "codes": ["DT35", "CG1"], "id": 56, "adjacencies": [55, 34, 85] },
    { "codes": ["DT5"], "id": 57, "adjacencies": [58] },
    { "codes": ["DT6"], "id": 58, "adjacencies": [57, 59] },
    { "codes": ["DT7"], "id": 59, "adjacencies": [58, 60] },
    { "codes": ["DT8"], "id": 60, "adjacencies": [18, 59] },
    { "codes": ["EW1"], "id": 61, "adjacencies": [70] },
    { "codes": ["EW10"], "id": 62, "adjacencies": [63, 90] },
    { "codes": ["EW11"], "id": 63, "adjacencies": [62, 64] },
    { "codes": ["EW12", "DT14"], "id": 64, "adjacencies": [63, 122, 29, 37] },
    { "codes": ["EW15"], "id": 65, "adjacencies": [66, 123] },
    { "codes": ["EW16", "NE3"], "id": 66, "adjacencies": [65, 67, 100] },
    { "codes": ["EW17"], "id": 67, "adjacencies": [66, 68] },
    { "codes": ["EW18"], "id": 68, "adjacencies": [67, 69] },
    { "codes": ["EW19"], "id": 69, "adjacencies": [68, 71] },
    { "codes": ["EW2", "DT32"], "id": 70, "adjacencies": [61, 80, 53, 54] },
    { "codes": ["EW20"], "id": 71, "adjacencies": [69, 72] },
    { "codes": ["EW21", "CC22"], "id": 72, "adjacencies": [71, 73, 21, 22] },
    { "codes": ["EW22"], "id": 73, "adjacencies": [72, 74] },
    { "codes": ["EW23"], "id": 74, "adjacencies": [73, 105] },
    { "codes": ["EW25"], "id": 75, "adjacencies": [76, 105] },
    { "codes": ["EW26"], "id": 76, "adjacencies": [75, 77] },
    { "codes": ["EW27"], "id": 77, "adjacencies": [76, 78] },
    { "codes": ["EW28"], "id": 78, "adjacencies": [77, 79] },
    { "codes": ["EW29"], "id": 79, "adjacencies": [78, 81] },
    { "codes": ["EW3"], "id": 80, "adjacencies": [70, 85] },
    { "codes": ["EW30"], "id": 81, "adjacencies": [79, 82] },
    { "codes": ["EW31"], "id": 82, "adjacencies": [81, 83] },
    { "codes": ["EW32"], "id": 83, "adjacencies": [82, 84] },
    { "codes": ["EW33"], "id": 84, "adjacencies": [83] },
    { "codes": ["EW4"], "id": 85, "adjacencies": [80, 86, 56] },
    { "codes": ["EW5"], "id": 86, "adjacencies": [85, 87] },
    { "codes": ["EW6"], "id": 87, "adjacencies": [86, 88] },
    { "codes": ["EW7"], "id": 88, "adjacencies": [87, 89] },
    { "codes": ["EW8", "CC9"], "id": 89, "adjacencies": [88, 90, 12, 33] },
    { "codes": ["EW9"], "id": 90, "adjacencies": [62, 89] },
    { "codes": ["NE1", "CC29"], "id": 91, "adjacencies": [27] },
    { "codes": ["NE10"], "id": 92, "adjacencies": [93, 104] },
    { "codes": ["NE11"], "id": 93, "adjacencies": [92, 94] },
    { "codes": ["NE12", "CC13"], "id": 94, "adjacencies": [93, 95, 14, 15] },
    { "codes": ["NE13"], "id": 95, "adjacencies": [94, 96] },
    { "codes": ["NE14"], "id": 96, "adjacencies": [95, 97] },
    { "codes": ["NE15"], "id": 97, "adjacencies": [96, 98] },
    {
        "codes": ["NE16", "STC"],
        "id": 98,
        "adjacencies": [97, 99, 146, 150, 151, 158]
    },
    {
        "codes": ["NE17", "PTC"],
        "id": 99,
        "adjacencies": [98, 139, 145, 132, 138]
    },
    { "codes": ["NE4", "DT19"], "id": 100, "adjacencies": [66, 101, 40, 42] },
    { "codes": ["NE5"], "id": 101, "adjacencies": [100, 121] },
    { "codes": ["NE7", "DT12"], "id": 102, "adjacencies": [103, 121, 37, 118] },
    { "codes": ["NE8"], "id": 103, "adjacencies": [102, 104] },
    { "codes": ["NE9"], "id": 104, "adjacencies": [92, 103] },
    { "codes": ["NS1", "EW24"], "id": 105, "adjacencies": [116, 74, 75] },
    { "codes": ["NS10"], "id": 106, "adjacencies": [107, 131] },
    { "codes": ["NS11"], "id": 107, "adjacencies": [106, 108] },
    { "codes": ["NS12"], "id": 108, "adjacencies": [107, 109] },
    { "codes": ["NS13"], "id": 109, "adjacencies": [108, 110] },
    { "codes": ["NS14"], "id": 110, "adjacencies": [109, 111] },
    { "codes": ["NS15"], "id": 111, "adjacencies": [110, 112] },
    { "codes": ["NS16"], "id": 112, "adjacencies": [111, 113] },
    { "codes": ["NS17", "CC15"], "id": 113, "adjacencies": [112, 114, 15, 16] },
    { "codes": ["NS18"], "id": 114, "adjacencies": [113, 115] },
    { "codes": ["NS19"], "id": 115, "adjacencies": [114, 117] },
    { "codes": ["NS2"], "id": 116, "adjacencies": [105, 126] },
    { "codes": ["NS20"], "id": 117, "adjacencies": [115, 118] },
    {
        "codes": ["NS21", "DT11"],
        "id": 118,
        "adjacencies": [117, 119, 36, 102]
    },
    { "codes": ["NS22"], "id": 119, "adjacencies": [118, 120] },
    { "codes": ["NS23"], "id": 120, "adjacencies": [119, 121] },
    {
        "codes": ["NS24", "NE6", "CC1"],
        "id": 121,
        "adjacencies": [120, 122, 101, 102, 19]
    },
    { "codes": ["NS25", "EW13"], "id": 122, "adjacencies": [121, 123, 64] },
    { "codes": ["NS26", "EW14"], "id": 123, "adjacencies": [122, 124, 65] },
    { "codes": ["NS27", "CE2"], "id": 124, "adjacencies": [123, 125, 38] },
    { "codes": ["NS28"], "id": 125, "adjacencies": [124] },
    { "codes": ["NS3"], "id": 126, "adjacencies": [116, 127] },
    { "codes": ["NS4", "BP1"], "id": 127, "adjacencies": [126, 128, 5] },
    { "codes": ["NS5"], "id": 128, "adjacencies": [127] },
    { "codes": ["NS7"], "id": 129, "adjacencies": [130] },
    { "codes": ["NS8"], "id": 130, "adjacencies": [129, 131] },
    { "codes": ["NS9", "TE2"], "id": 131, "adjacencies": [106, 130, 159, 160] },
    { "codes": ["PE1"], "id": 132, "adjacencies": [133, 99] },
    { "codes": ["PE2"], "id": 133, "adjacencies": [132, 134] },
    { "codes": ["PE3"], "id": 134, "adjacencies": [133, 135] },
    { "codes": ["PE4"], "id": 135, "adjacencies": [134, 136] },
    { "codes": ["PE5"], "id": 136, "adjacencies": [135, 137] },
    { "codes": ["PE6"], "id": 137, "adjacencies": [136, 138] },
    { "codes": ["PE7"], "id": 138, "adjacencies": [137, 99] },
    { "codes": ["PW1"], "id": 139, "adjacencies": [140, 99] },
    { "codes": ["PW2"], "id": 140, "adjacencies": [139, 141] },
    { "codes": ["PW3"], "id": 141, "adjacencies": [140, 142] },
    { "codes": ["PW4"], "id": 142, "adjacencies": [141, 143] },
    { "codes": ["PW5"], "id": 143, "adjacencies": [142, 144] },
    { "codes": ["PW6"], "id": 144, "adjacencies": [143, 145] },
    { "codes": ["PW7"], "id": 145, "adjacencies": [144, 99] },
    { "codes": ["SE1"], "id": 146, "adjacencies": [147, 98] },
    { "codes": ["SE2"], "id": 147, "adjacencies": [146, 148] },
    { "codes": ["SE3"], "id": 148, "adjacencies": [147, 149] },
    { "codes": ["SE4"], "id": 149, "adjacencies": [148, 150] },
    { "codes": ["SE5"], "id": 150, "adjacencies": [149, 98] },
    { "codes": ["SW1"], "id": 151, "adjacencies": [152, 98] },
    { "codes": ["SW2"], "id": 152, "adjacencies": [151, 153] },
    { "codes": ["SW3"], "id": 153, "adjacencies": [152, 154] },
    { "codes": ["SW4"], "id": 154, "adjacencies": [153, 155] },
    { "codes": ["SW5"], "id": 155, "adjacencies": [154, 156] },
    { "codes": ["SW6"], "id": 156, "adjacencies": [155, 157] },
    { "codes": ["SW7"], "id": 157, "adjacencies": [156, 158] },
    { "codes": ["SW8"], "id": 158, "adjacencies": [157, 98] },
    { "codes": ["TE1"], "id": 159, "adjacencies": [131] },
    { "codes": ["TE3"], "id": 160, "adjacencies": [131, 161] },
    { "codes": ["TE4"], "id": 161, "adjacencies": [160, 162] },
    { "codes": ["TE5"], "id": 162, "adjacencies": [161, 163] },
    { "codes": ["TE6"], "id": 163, "adjacencies": [162, 164] },
    { "codes": ["TE7"], "id": 164, "adjacencies": [163, 165] },
    { "codes": ["TE8"], "id": 165, "adjacencies": [17, 164] }
]


for station in data:
    adjList = []

    for code in station["codes"]:
        if code != "PTC" and code != "STC":
            line = str(code[:2])
            num = int(code[2:])
            newCode1 = line + str(num + 1)
            newCode2 = line + str(num - 1)

            for newStation in data:
                if newStation["id"] in adjList:
                    continue
                
                if newCode1 in newStation["codes"]:
                    adjList.append(newStation["id"])
                if newCode2 in newStation["codes"]:
                    adjList.append(newStation["id"])

    if station["id"] == 85:  # EW-CG
        adjList.append(56)
    if station["id"] == 56:
        adjList.append(85)

    if station["id"] == 4:  # BP
        adjList.append(35)
    if station["id"] == 35:
        adjList.append(4)

    if station["id"] == 139:  # PTC
        adjList.append(99)
    if station["id"] == 99:
        adjList.append(139)

    if station["id"] == 145:  # PTC
        adjList.append(99)
    if station["id"] == 99:
        adjList.append(145)

    if station["id"] == 132:  # PTC
        adjList.append(99)
    if station["id"] == 99:
        adjList.append(132)

    if station["id"] == 138:  # PTC
        adjList.append(99)
    if station["id"] == 99:
        adjList.append(138)

    if station["id"] == 146:  # STC
        adjList.append(98)
    if station["id"] == 98:
        adjList.append(146)

    if station["id"] == 150:  # STC
        adjList.append(98)
    if station["id"] == 98:
        adjList.append(150)

    if station["id"] == 151:  # STC
        adjList.append(98)
    if station["id"] == 98:
        adjList.append(151)

    if station["id"] == 158:  # STC
        adjList.append(98)
    if station["id"] == 98:
        adjList.append(158)

    if station["id"] == 38:  # CC-CE
        adjList.append(29)
    if station["id"] == 29:
        adjList.append(38)

    station["adjacencies"] = adjList

    print(station["id"], adjList)


file_w = open('stations.json', 'w')
json.dump(data, file_w)
file_w.close()

mode_table = {
    1: '0001', #numeric
    2: '0010', #alphanumeric
    3: '0100', #byte
    4: '1000', #kanji (not supported)
    5: '0111', #eci (not supported)
}

ec_table = {
    'L' : '01',
    'M' : '00',
    'Q' : '11',
    'H' : '10'
}

alphanumeric_table = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 36,
    '$': 37,
    '%': 38,
    '*': 39,
    '+': 40,
    '-': 41,
    '.': 42,
    '/': 43,
    ':': 44
}

alignment_pattern_locations = {
    # Version 1 has no ap
    2: {"starting_number": 18, "increment": 1000},
    3: {"starting_number": 22, "increment": 1000},
    4: {"starting_number": 26, "increment": 1000},
    5: {"starting_number": 30, "increment": 1000},
    6: {"starting_number": 34, "increment": 1000},
    7: {"starting_number": 22, "increment": 16},
    8: {"starting_number": 24, "increment": 18},
    9: {"starting_number": 26, "increment": 20},
    10: {"starting_number": 28, "increment": 22},
    11: {"starting_number": 30, "increment": 24},
    12: {"starting_number": 32, "increment": 26},
    13: {"starting_number": 34, "increment": 28},
    14: {"starting_number": 26, "increment": 20},
    15: {"starting_number": 26, "increment": 22},
    16: {"starting_number": 26, "increment": 24},
    17: {"starting_number": 30, "increment": 24},
    18: {"starting_number": 30, "increment": 26},
    19: {"starting_number": 30, "increment": 28},
    20: {"starting_number": 34, "increment": 28},
    21: {"starting_number": 28, "increment": 22},
    22: {"starting_number": 26, "increment": 24},
    23: {"starting_number": 30, "increment": 24},
    24: {"starting_number": 28, "increment": 26},
    25: {"starting_number": 32, "increment": 26},
    26: {"starting_number": 30, "increment": 28},
    27: {"starting_number": 34, "increment": 28}
}

remainder_bits = {
    1:	0,
    2:	7,
    3:	7,
    4:	7,
    5:	7,
    6:	7,
    7:	0,
    8:	0,
    9:	0,
    10:	0,
    11:	0,
    12:	0,
    13:	0,
    14:	3,
    15:	3,
    16:	3,
    17:	3,
    18:	3,
    19:	3,
    20:	3,
    21:	4,
    22:	4,
    23:	4,
    24:	4,
    25:	4,
    26:	4,
    27:	4,
    28:	3,
    29:	3,
    30:	3,
    31:	3,
    32:	3,
    33:	3,
    34:	3,
    35:	0,
    36:	0,
    37:	0,
    38:	0,
    39:	0,
    40:	0
}

format_information_bits = {
    "L": {
        0: "111011111000100",
        1: "111001011110011",
        2: "111110110101010",
        3: "111100010011101",
        4: "110011000101111",
        5: "110001100011000",
        6: "110110001000001",
        7: "110100101110110",
    },
    "M": {
        0: "101010000010010",
        1: "101000100100101",
        2: "101111001111100",
        3: "101101101001011",
        4: "100010111111001",
        5: "100000011001110",
        6: "100111110010111",
        7: "100101010100000",
    },
    "Q": {
        0: "011010101011111",
        1: "011000001101000",
        2: "011111100110001",
        3: "011101000000110",
        4: "010010010110100",
        5: "010000110000011",
        6: "010111011011010",
        7: "010101111101101",
    },
    "H": {
        0: "001011010001001",
        1: "001001110111110",
        2: "001110011100111",
        3: "001100111010000",
        4: "000011101100010",
        5: "000001001010101",
        6: "000110100001100",
        7: "000100000111011",
    },
}

version_information_bits = {
    7: "000111110010010100",
    8: "001000010110111100",
    9: "001001101010011001",
    10: "001010010011010011",
    11: "001011101111110110",
    12: "001100011101100010",
    13: "001101100001000111",
    14: "001110011000001101",
    15: "001111100100101000",
    16: "010000101101111000",
    17: "010001010001011101",
    18: "010010101000010111",
    19: "010011010100110010",
    20: "010100100110100110",
    21: "010101011010000011",
    22: "010110100011001001",
    23: "010111011111101100",
    24: "011000111011000100",
    25: "011001000111100001",
    26: "011010111110101011",
    27: "011011000010001110",
    28: "011100110000011010",
    29: "011101001100111111",
    30: "011110110101110101",
    31: "011111001001010000",
    32: "100000100111010101",
    33: "100001011011110000",
    34: "100010100010111010",
    35: "100011011110011111",
    36: "100100101100001011",
    37: "100101010000101110",
    38: "100110101001100100",
    39: "100111010101000001",
    40: "101000110001101001",
}

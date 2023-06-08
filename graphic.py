from vpython import *

translate = {"2-6": 1, "2-7": 2, "2-8": 3, "2-9": 4, "2-10": 5, "2nd\n Grade": 6, "J's \nSmart Class": 7, "2-11": 8,
             "2-12": 9,
             "2-13": 10,
             "2-14": 11, "2-5": 12, "2-4": 13, "2-3": 14, "2-2": 15, "2-1": 16, "1st Grade": 17, "Dream\nClass": 18,
             "1-1": 19,
             "1-2": 20, "1-3": 21, "FutureClass": 22,
             "1-14": 23, "1-13": 24, "1-12": 25, "1-11": 26, "1-10": 27, "1-9": 28, "1-8": 29, "1-7": 30, "1-6": 31,
             "1-5": 32, "1-4": 33,
             "Restroom\n(Woman)": 34, "Print\n room": 35, "Exam \nroom": 36, "Grade \nroom": 37, "MainRest \nroom": 38,
             "1st \nTeacher Office": 39, "Main \nEntrance": 40, "Administrative \nOffice": 41,
             "Principal's \nOffice": 42, "Main \nDiscussing room": 43, "book \ngarage": 44, "Broadcasting \nroom": 45,
             "Document \nroom": 46, "3.1": 47, "AI Class": 48, "Informatics \nroom": 49, "Science \nTeacher Office": 50,
             "Resource\n room": 51,
             "Math \nClass a": 52, "Music \nClass": 53, "Chemistry \nClass": 54, "Chemical \nExperiment": 55,
             "Chemi/Bio\n Pre room": 56,
             "reagent \nroom": 57, "Intelligent \nScience Lab": 58, "Bio \nExperiment": 59, "English \nonly Class": 60,
             "Class \nshare cafe": 61, "Physics \nExperiment": 62, "Physics \nClass": 63,
             "Physic/Earth \nPre room": 64, "Science \nteacher Lab": 65, "Earth \nClass": 66, "Earth \nExperiment": 67,
             "3th Grade": 68, "Art \nClass 2": 69, "Art \nResearch room": 70, "Art \nClass 1": 71, "Back Entrance": 72,
             "2nd \nTeacher Office": 73, "Back \nDiscussing \nroom": 74, "Back \nrest room": 75,
             "Math Class b": 76, "3-8": 77, "3-9": 78, "3-10": 79, "3-11": 80,
             "3-12": 81, "3-13": 82, "3-14": 83, "3-7": 84, "3-6": 85, "3-5": 86, "3-4": 87, "3-3": 88, "3-2": 89,
             "3-1": 90, "Introspection\nRoom": 91, "Club": 92, "a": 93,
             "b": 94, "Aid\nRoom": 95, "Specialized\nClass": 96, "Rest Room\n(Man)": 97, "c": 98,
             "Special\nTeacher Office": 99, "WeeClass": 100,
             "Future\nCunsulting\nRoom": 101, "Store": 102,
             "Student\nDiscussing\nRoom": 103, "Cafeteria_1": 104, "Cafeteria_2": 105, "Cafeteria_3": 106,
             "Seo\nOnBit\n1": 107,
             "Seo\nOnBit\n2": 108, "Seo\nOnBit\n3": 109, "Parents\nAcademy": 110,
             "Restroom_study": 111,
             "Parents\nMeeting": 112,
             "Theater": 113, "Library": 114, "Study Room": 115}


class Node:
    def __init__(self, pos: tuple[float, float, float]):
        self.pos = pos


nodes = {
    # 본관
    1: Node((-500, 245, 0)),
    2: Node((-400, 245, 0)),
    3: Node((-300, 245, 0)),
    4: Node((-200, 245, 0)),
    5: Node((-100, 245, 0)),
    6: Node((0, 245, 0)),
    7: Node((100, 245, 0)),
    8: Node((200, 245, 0)),
    9: Node((300, 245, 0)),
    10: Node((400, 245, 0)),
    11: Node((500, 245, 0)),

    12: Node((-500, 175, 0)),
    13: Node((-400, 175, 0)),
    14: Node((-300, 175, 0)),
    15: Node((-200, 175, 0)),
    16: Node((-100, 175, 0)),
    17: Node((0, 175, 0)),
    18: Node((100, 175, 0)),
    19: Node((200, 175, 0)),
    20: Node((300, 175, 0)),
    21: Node((400, 175, 0)),
    22: Node((500, 175, 0)),

    23: Node((-500, 105, 0)),
    24: Node((-400, 105, 0)),
    25: Node((-300, 105, 0)),
    26: Node((-200, 105, 0)),
    27: Node((-100, 105, 0)),
    28: Node((0, 105, 0)),
    29: Node((100, 105, 0)),
    30: Node((200, 105, 0)),
    31: Node((300, 105, 0)),
    32: Node((400, 105, 0)),
    33: Node((500, 105, 0)),

    34: Node((-525, 35, 0)),
    35: Node((-475, 35, 0)),
    36: Node((-425, 35, 0)),
    37: Node((-375, 35, 0)),
    38: Node((-325, 35, 0)),
    39: Node((-162.5, 35, 0)),
    40: Node((0, 35, 0)),
    41: Node((100, 35, 0)),
    42: Node((200, 35, 0)),
    43: Node((270, 35, 0)),
    44: Node((350, 35, 0)),
    45: Node((430, 35, 0)),
    46: Node((520, 35, 0)),
    # 건물별로
    # 과학동
    47: Node((0, 35, -400,)),
    48: Node((-972, 105, -452)),
    49: Node((-897, 105, -452)),
    50: Node((-784.5, 105, -452)),
    51: Node((-662, 105, -452)),
    52: Node((-612, 105, -452)),
    53: Node((-549.5, 105, -452)),

    54: Node((-972, 175, -452)),
    55: Node((-892, 175, -452)),
    56: Node((-822, 175, -452)),
    57: Node((-752, 175, -452)),
    58: Node((-672, 175, -452)),
    59: Node((-597, 175, -452)),
    60: Node((-534.5, 175, -452)),
    61: Node((-472, 175, -452)),

    62: Node((-972, 245, -452)),
    63: Node((-897, 245, -452)),
    64: Node((-822, 245, -452)),
    65: Node((-747, 245, -452)),
    66: Node((-672, 245, -452)),
    67: Node((-597, 245, -452)),
    68: Node((-490, 245, -452)),

    # 후관
    69: Node((-420, 105, -712)),
    70: Node((-330, 105, -712)),
    71: Node((-240, 105, -712)),
    72: Node((-150, 105, -712)),
    73: Node((30, 105, -712)),
    74: Node((165, 105, -712)),
    75: Node((255, 105, -712)),

    76: Node((-420, 175, -712)),
    77: Node((-330, 175, -712)),
    78: Node((-240, 175, -712)),
    79: Node((-150, 175, -712)),
    80: Node((-60, 175, -712)),
    81: Node((30, 175, -712)),
    82: Node((120, 175, -712)),
    83: Node((225, 175, -712)),

    84: Node((-420, 245, -712)),
    85: Node((-330, 245, -712)),
    86: Node((-240, 245, -712)),
    87: Node((-150, 245, -712)),
    88: Node((-60, 245, -712)),
    89: Node((30, 245, -712)),
    90: Node((120, 245, -712)),
    91: Node((180, 245, -712)),
    92: Node((250, 245, -712)),

    93: Node((1800, 245, -712)),
    94: Node((1840, 245, -712)),
    98: Node((1840, 245, -712)),

    95: Node((360, 105, -500)),
    96: Node((360, 105, -400)),
    97: Node((350, 105, -300)),
    99: Node((420, 105, -300)),
    100: Node((360, 175, -525)),
    101: Node((360, 175, -457)),
    102: Node((360, 175, -389)),
    103: Node((360, 175, -321)),

    104: Node((260, 105, -1086)),
    105: Node((260, 175, -1086)),
    106: Node((260, 245, -1086)),
    107: Node((230, 315, -1086)),
    108: Node((260, 315, -1086)),
    109: Node((290, 315, -1086)),

    110: Node((-394, 105, -1135)),
    111: Node((-394, 105, -935)),
    112: Node((-594, 105, -1135)),
    113: Node((-594, 105, -935)),
    114: Node((-494, 175, -1035)),
    115: Node((-494, 245, -1035)),

    116: Node((460, 105, -174)),
    117: Node((460, 175, -174)),
    118: Node((460, 105, 0)),
    119: Node((460, 175, 0)),

    120: Node((460, 175, -321)),
    121: Node((460, 175, -389)),
    122: Node((460, 175, -457)),
    123: Node((460, 175, -525)),

    124: Node((460, 105, -500)),
    125: Node((460, 105, -400)),
    126: Node((460, 105, -300)),

    127: Node((459, 175, -623)),

    128: Node((459, 245, -763)),
    129: Node((459, 175, -763)),
    130: Node((459, 105, -763)),

    131: Node((364, 245, -763)),
    132: Node((364, 175, -763)),
    133: Node((364, 105, -763)),

    134: Node((250, 245, -763)),
    135: Node((225, 175, -763)),

    136: Node((303, 245, -763)),
    137: Node((303, 175, -763)),

    138: Node((303, 245, -870)),
    139: Node((303, 175, -870)),

    140: Node((-496, 175, -712)),

    141: Node((-496, 175, -847)),

    142: Node((-545, 245, -712)),
    143: Node((-545, 175, -712)),

    144: Node((-545, 245, -573)),
    145: Node((-545, 175, -573)),

    146: Node((-545, 245, -452)),
    147: Node((-545, 175, -452)),

    148: Node((-468, 245, -452)),
    149: Node((-468, 175, -452)),

    150: Node((-468, 245, -285)),
    151: Node((-468, 175, -285)),

    152: Node((-468, 245, 0)),
    153: Node((-468, 175, 0)),

}

scene.camera.pos = vec(470, 554, 543)
scene.camera.axis = vec(-353, -402, -694)
scene.width = 1900
scene.height = 980

floor = box(pos=vec(0,-0,-500), size=vec(2000,1,2000), color=vec(232/255,208/255, 169/255))
mainBuilding = box(pos=vec(0, 140, 0), size=vector(1100, 280, 125), opacity=0.5)

main_science = box(pos=vec(-468, 210, -285), size=vec(45, 140, 447), opacity=0.5)

scienceBuilding = box(pos=vec(-757, 350 / 2, -452), size=vec(580, 210, 114), opacity=0.5)
science_back = box(pos=vec(-545, 210, -573), size=vec(109, 140, 128), opacity=0.5)
backBuilding = box(size=vec(900, 210, 150), pos=vec(-150, 70 + 210 / 2, -712), opacity=0.5)
studyBuilding = box(size=vec(311, 210, 254), pos=vec(-494, 175, -1035), opacity=0.5)
study_back = box(size=vec(43, 70, 120), pos=vec(-496, 350 / 2, -847), opacity=0.5)
centerBuilding = box(size=vec(211, 140, 272), pos=vec(444, 140, -423), opacity=0.5)
main_center = box(size=vec(38, 140, 225), pos=vec(460, 140, -174), opacity=0.5)
center_toilet = box(size=vec(60, 70, 131), pos=vec(459, 175, -623), opacity=0.5)
toiletBuilding = box(size=vec(120, 210, 95), pos=vec(489, 175, -740), opacity=0.5)
toilet_back = box(size=vec(129, 140, 47), pos=vec(364, 210, -763), opacity=0.5)
cafeBuilding = box(size=vec(132, 280, 276), pos=vec(260, 210, -1086), opacity=0.5)
cafe_toilet = box(size=vec(48, 140, 162), pos=vec(303, 210, -870), opacity=0.5)
threeoneTower = sphere(size=vec(50,140,50), pos=vec(0,70,-400), opacity=0.5)
for i in range(1, 116):
    keys = [k for k, v in translate.items() if v == i]
    a = keys[0]
    Tx = text(text=a, pos=vec(nodes[i].pos[0], nodes[i].pos[1], nodes[i].pos[2] + 10), align='center',
              color=vec(0, 0, 153 / 255), height=10)


def way(paths_finished):
    for obj in scene.objects:
        if 'curve' in str(obj):
            obj.visible = False

    path_len = len(paths_finished)


    for n in range(0, path_len - 1):
        line = curve(pos=[nodes[paths_finished[n]].pos, nodes[paths_finished[n + 1]].pos],
                     color=vec(255 / 255, 153 / 255, 51 / 255), radius=10)

        x = int(nodes[paths_finished[n]].pos[0]) - int(nodes[paths_finished[n + 1]].pos[0])
        y = int(nodes[paths_finished[n]].pos[1]) - int(nodes[paths_finished[n + 1]].pos[1])
        z = int(nodes[paths_finished[n]].pos[2]) - int(nodes[paths_finished[n + 1]].pos[2])
        key=max(abs(x), abs(y), abs(z))
        for k in range(key):
            X = nodes[paths_finished[n]].pos[0] - k * x / key
            Y = nodes[paths_finished[n]].pos[1] - k * y / key
            Z = nodes[paths_finished[n]].pos[2] - k * z / key
            scene.camera.pos = vec(X, Y, Z + 300)
            scene.camera.axis = vec(0, 0, -900)
            rate(100)

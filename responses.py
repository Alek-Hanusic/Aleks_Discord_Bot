import random
responses = [
    "laganini poz za mog druga SAMO KAMATA LAGANINI REAL MADRID",
    "Tito laganini Real Madrid poz",
    "XEXE laganini Real Madrid",
    "Malo laganini sokace PoZ real Madrid",
    "2,Grama xexe PoZ laganini Real Madrid",
    "laganini samo Balkan gori mnjauuuu Real Madrid",
    "alekmuselam uskoro abda lagnini poz real Madrid",
    "laganini samo poz Real Madrid",
    "laganini sad mnjaucu PoZ real Madrid",
    "nista I Dr put JESTE li sokace uzeli laganini Real Madrid poz",
    "samo Lubenka laganini Real Madrid poz",
    "Monte me namontirao laganini Real Madrid poz",
    "poz za Tz laganini Real Madrid",
    "Jenjetina i sokace laganini poz Real Madrid",
    "alejkmuselam laganini Real Madrid poz",
    "hodzino se melje laganini samo poz Real Madrid",
    "hodzino se melje laganini samo poz Real Madrid",
    "alekmuselam uskoro abda ide ludilooooo BALKAN gori poz real Madrid",
    "Hvala laganini samo poz Real Madrid",
    "Alejkmuselam dok se Hozdino samelje poz Real Madrid",
    "Kolac je turbo diesel ala me Turbiraaaaa poz Real Madrid laganini",
    "Kolac je turbo diesel ala me Turbiraaaaa poz Real Madrid laganini",
    "Imas opciju block laganini poz Real Madrid",
    "uvjek laganini samo poz Real Madrid",
    "Amin boze poz Real Madrid laganini",
    "Meduljo PoZ laganini Real Madrid",
    "bice Laganini salju ljudi gute bez live jojjjjjjjjjjjjjjjj jojjjjjjjjjjjjjjjj poz Real Madrid laganini",
    "ma mnjaucu laganini xexe😅 PoZ laganini Real Madrid",
    'LAGA NI NI',
    'JOOOOJ AL ME MONTIRA',
    'JOOOJ AL ME HLADIRA',
    'JOJ STO ME HLORISE',
    'OVOOO ONOOOO','ZEHROOO',
    'JOOOOJ AL ME HELLIRA'
]



def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'elvedin':
        return random.choice(responses)
    # if p_message == 'roll':
    #     return str(random.randint(1,6))
    # if p_message == 'play':
    #     return 'Playing music'
    # if p_message == 'stop':
    #     return 'Stopping music'
    # if p_message == '!help':
    #     return 'Commands: !roll, !play, !stop'
    return 'Ne znam šta pričaš bracika'



from random import choice

class sk_heirarchy:
    def __init__(self, data):
        self.data = data
    
    def pick(self):
        seeming = choice(self.data.keys())
        kith = choice(self.data[seeming])
        return seeming+' '+kith

class sk_flat:
    def __init__(self, data):
        self.data = data
    
    def pick(self):
        output = []
        for d in self.data:
            output.append(choice(d))
        return ' '.join(output)

# Available seemings and kiths. Change as you like to suit your needs.
pairs = {"Changeling: the Lost": sk_heirarchy({"Beast":[
            "Broadback",
            "Hunterheart",
            "Runnerswift",
            "Skitterskulk",
            "Swimmerskin",
            "Venombite",
            "Windwing"
        ],"Darkling":[
            "Antiquarian",
            "Gravewight",
            "Leechfinger",
            "Mirrorskin",
            "Tunnelgrub"
        ],"Elemental":[
            "Airtouched",
            "Earthbones",
            "Fireheart",
            "Manikin",
            "Waterborn",
            "Woodblood"
        ],"Fairest":[
            "Bright one",
            "Dancer",
            "Draconic",
            "Flowering",
            "Muse"
        ],"Ogre":[
            "Cyclopean",
            "Farwalker",
            "Gargantuan",
            "Gristlegrinder",
            "Stonebones",
            "Water-dweller"
        ],"Wizened":[
            "Artist",
            "Brewer",
            "Chatelaine",
            "Chirurgeon",
            "Smith",
            "Soldier"
        ]}),
    "Mage: the Awakening": sk_flat([['Acanthus', 'Mastigos', 'Moros', 'Obrimos', 'Thyrsis'], ['Adamantine Arrow', 'Free Council', 'Guardians of the Veil', 'Mysterium', 'Silver Ladder']]),
    "Werewolf: the Forsaken (Urdaga/Forsaken)": sk_flat([['Rahu', 'Cahalith', 'Elodoth', 'Ithaeur', 'Irraka'], ['Blood Talon', 'Bone Shadow', 'Hunter in Darkness', 'Iron Master', 'Storm Lord', 'Ghost Wolf']]),
    "Werewolf: the Forsaken (Anshega/Pure & Other)": sk_flat([['Rahu', 'Cahalith', 'Elodoth', 'Ithaeur', 'Irraka'], ['Fire-Touched', 'Ivory Claw', 'Predator King', 'Bale Hound']]),
}

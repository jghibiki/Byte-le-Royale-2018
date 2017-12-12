from game.common.enums import ItemType, UnitClass

valid_purchasers = {
    ItemType.sword:               [ UnitClass.knight ],
    ItemType.mace:                [ UnitClass.brawler ],
    ItemType.spear:               [ UnitClass.pikeman ],
    ItemType.dagger:              [ UnitClass.rogue ],
    ItemType.staff:               [ UnitClass.magus ],
    ItemType.wand:                [ UnitClass.wizard ],
    ItemType.spell_book:          [ UnitClass.sorcerer ],
    ItemType.alchemical_supplies: [ UnitClass.alchemist ],
    ItemType.fire_bomb:           [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.frost_bomb:          [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.shock_bomb:          [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.acid_bomb:           [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.flash_bomb:          [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.spike_bomb:          [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.concussion_bomb:     [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.fire_ball:            [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.thunderbolt:         [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.ice_spike:           [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ]
}

item_data = {
    ItemType.sword: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.mace: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.spear: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.dagger: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.staff: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.wand: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.spell_book: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.alchemical_supplies: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.fire_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.frost_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.shock_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.acid_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.flash_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.spike_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.concussion_bomb: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.fire_ball: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.thunderbolt: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    },
    ItemType.ice_spike: {
        1: { "cost": 50 },
        2: { "cost": 300 },
        3: { "cost": 300 },
        4: { "cost": 300 },
        5: { "cost": 300 },
        6: { "cost": 300 },
        7: { "cost": 300 },
        8: { "cost": 300 },
        9: { "cost": 300 },
        10: { "cost": 300 }
    }
}


town_0 = [
        { "type": ItemType.sword,               "level": 1,  "cost": 0  },
        { "type": ItemType.mace,                "level": 1,  "cost": 0  },
        { "type": ItemType.spear,               "level": 1,  "cost": 0  },
        { "type": ItemType.dagger,              "level": 1,  "cost": 0  },
        { "type": ItemType.staff,               "level": 1,  "cost": 0  },
        { "type": ItemType.wand,                "level": 1,  "cost": 0  },
        { "type": ItemType.spell_book,          "level": 1,  "cost": 0  },
        { "type": ItemType.alchemical_supplies, "level": 1,  "cost": 0  },
        { "type": ItemType.fire_bomb,           "level": 1,  "cost": 50 },
        { "type": ItemType.frost_bomb,          "level": 1,  "cost": 50 },
        { "type": ItemType.shock_bomb,          "level": 1,  "cost": 50 },
        { "type": ItemType.acid_bomb,           "level": 1,  "cost": 50 },
        { "type": ItemType.flash_bomb,          "level": 1,  "cost": 50 },
        { "type": ItemType.spike_bomb,          "level": 1,  "cost": 50 },
        { "type": ItemType.concussion_bomb,     "level": 1,  "cost": 50 },
        { "type": ItemType.fire_ball,           "level": 1,  "cost": 50 },
        { "type": ItemType.thunderbolt,         "level": 1,  "cost": 50 },
        { "type": ItemType.ice_spike,           "level": 1,  "cost": 50 }
]


town_1 = [
        { "type": ItemType.sword,               "level": 2,  "cost": 300 },
        { "type": ItemType.mace,                "level": 2,  "cost": 300 },
        { "type": ItemType.spear,               "level": 2,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 2,  "cost": 300 },
        { "type": ItemType.staff,               "level": 2,  "cost": 300 },
        { "type": ItemType.wand,                "level": 2,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 2,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 2,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 2,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 2,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 2,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 2,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 2,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 2,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 2,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 2,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 2,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 2,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_2 = [
        { "type": ItemType.sword,               "level": 3,  "cost": 300 },
        { "type": ItemType.mace,                "level": 3,  "cost": 300 },
        { "type": ItemType.spear,               "level": 3,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 3,  "cost": 300 },
        { "type": ItemType.staff,               "level": 3,  "cost": 300 },
        { "type": ItemType.wand,                "level": 3,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 3,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 3,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 3,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 3,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 3,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 3,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 3,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 3,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 3,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 3,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 3,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 3,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_3 = [
        { "type": ItemType.sword,               "level": 4,  "cost": 300 },
        { "type": ItemType.mace,                "level": 4,  "cost": 300 },
        { "type": ItemType.spear,               "level": 4,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 4,  "cost": 300 },
        { "type": ItemType.staff,               "level": 4,  "cost": 300 },
        { "type": ItemType.wand,                "level": 4,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 4,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 4,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 4,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 4,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 4,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 4,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 4,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 4,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 4,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 4,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 4,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 4,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_4 = [
        { "type": ItemType.sword,               "level": 5,  "cost": 300 },
        { "type": ItemType.mace,                "level": 5,  "cost": 300 },
        { "type": ItemType.spear,               "level": 5,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 5,  "cost": 300 },
        { "type": ItemType.staff,               "level": 5,  "cost": 300 },
        { "type": ItemType.wand,                "level": 5,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 5,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 5,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 5,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 5,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 5,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 5,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 5,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 5,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 5,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 5,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 5,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 5,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_5 = [
        { "type": ItemType.sword,               "level": 6,  "cost": 300 },
        { "type": ItemType.mace,                "level": 6,  "cost": 300 },
        { "type": ItemType.spear,               "level": 6,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 6,  "cost": 300 },
        { "type": ItemType.staff,               "level": 6,  "cost": 300 },
        { "type": ItemType.wand,                "level": 6,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 6,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 6,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 6,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 6,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 6,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 6,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 6,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 6,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 6,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 6,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 6,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 6,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_6 = [
        { "type": ItemType.sword,               "level": 7,  "cost": 300 },
        { "type": ItemType.mace,                "level": 7,  "cost": 300 },
        { "type": ItemType.spear,               "level": 7,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 7,  "cost": 300 },
        { "type": ItemType.staff,               "level": 7,  "cost": 300 },
        { "type": ItemType.wand,                "level": 7,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 7,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 7,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 7,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 7,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 7,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 7,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 7,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 7,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 7,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 7,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 7,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 7,  "cost": 200 }
]

# TODO UPDATE OPTIONS
town_7 = [
        { "type": ItemType.sword,               "level": 8,  "cost": 300 },
        { "type": ItemType.mace,                "level": 8,  "cost": 300 },
        { "type": ItemType.spear,               "level": 8,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 8,  "cost": 300 },
        { "type": ItemType.staff,               "level": 8,  "cost": 300 },
        { "type": ItemType.wand,                "level": 8,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 8,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 8,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 8,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 8,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 8,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 8,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 8,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 8,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 8,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 8,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 8,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 8,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_8 = [
        { "type": ItemType.sword,               "level": 9,  "cost": 300 },
        { "type": ItemType.mace,                "level": 9,  "cost": 300 },
        { "type": ItemType.spear,               "level": 9,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 9,  "cost": 300 },
        { "type": ItemType.staff,               "level": 9,  "cost": 300 },
        { "type": ItemType.wand,                "level": 9,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 9,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 9,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 9,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 9,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 9,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 9,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 9,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 9,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 9,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 9,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 9,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 9,  "cost": 200 }
]


# TODO UPDATE OPTIONS
town_9 = [
        { "type": ItemType.sword,               "level": 10,  "cost": 300 },
        { "type": ItemType.mace,                "level": 10,  "cost": 300 },
        { "type": ItemType.spear,               "level": 10,  "cost": 300 },
        { "type": ItemType.dagger,              "level": 10,  "cost": 300 },
        { "type": ItemType.staff,               "level": 10,  "cost": 300 },
        { "type": ItemType.wand,                "level": 10,  "cost": 300 },
        { "type": ItemType.spell_book,          "level": 10,  "cost": 300 },
        { "type": ItemType.alchemical_supplies, "level": 10,  "cost": 300 },
        { "type": ItemType.fire_bomb,           "level": 10,  "cost": 200 },
        { "type": ItemType.frost_bomb,          "level": 10,  "cost": 200 },
        { "type": ItemType.shock_bomb,          "level": 10,  "cost": 200 },
        { "type": ItemType.acid_bomb,           "level": 10,  "cost": 200 },
        { "type": ItemType.flash_bomb,          "level": 10,  "cost": 200 },
        { "type": ItemType.spike_bomb,          "level": 10,  "cost": 200 },
        { "type": ItemType.concussion_bomb,     "level": 10,  "cost": 200 },
        { "type": ItemType.fire_ball,           "level": 10,  "cost": 200 },
        { "type": ItemType.thunderbolt,         "level": 10,  "cost": 200 },
        { "type": ItemType.ice_spike,           "level": 10,  "cost": 200 }
]



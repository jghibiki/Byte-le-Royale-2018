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
    ItemType.guided_bomb:         [ UnitClass.rogue, UnitClass.alchemist ],
    ItemType.fire_ball:           [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.thunderbolt:         [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.ice_spike:           [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.sonic_blast:         [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.magic_sword:         [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.spear_of_light:      [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.rock_smash:          [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ],
    ItemType.armor:               [ UnitClass.knight, UnitClass.brawler, UnitClass.pikeman,
                                    UnitClass.rogue, UnitClass.magus, UnitClass.sorcerer,
                                    UnitClass.wizard, UnitClass.alchemist]
}

item_data = {
    ItemType.sword: {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.mace: {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.spear: {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.dagger: {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.staff:  {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.wand: {
        1: { "cost": 0 },
        2: { "cost": 300 },
        3: { "cost": 600 },
        4: { "cost": 900 },
        5: { "cost": 1200 },
        6: { "cost": 1500 },
        7: { "cost": 1800 },
        8: { "cost": 2100 },
        9: { "cost": 2400 },
        10: { "cost": 2700 }
    },
    ItemType.spell_book:  {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.alchemical_supplies: {
        1: { "cost": 0 },
        2: { "cost": 225 },
        3: { "cost": 591 },
        4: { "cost": 1141 },
        5: { "cost": 1869 },
        6: { "cost": 2776 },
        7: { "cost": 3861 },
        8: { "cost": 5126 },
        9: { "cost": 6569 },
        10: { "cost": 8191 }
    },
    ItemType.fire_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.frost_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.shock_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.acid_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.flash_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.spike_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.concussion_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.guided_bomb: {
        1: { "cost": 33 },
        2: { "cost": 244 },
        3: { "cost": 651 },
        4: { "cost": 1255 },
        5: { "cost": 2055 },
        6: { "cost": 3053 },
        7: { "cost": 4247 },
        8: { "cost": 5638 },
        9: { "cost": 7225 },
        10: { "cost": 9010 }
    },
    ItemType.fire_ball: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.thunderbolt: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.ice_spike: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.sonic_blast: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.magic_sword: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.spear_of_light: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.rock_smash: {
        1: { "cost": 34 },
        2: { "cost": 255 },
        3: { "cost": 680 },
        4: { "cost": 1312 },
        5: { "cost": 2149 },
        6: { "cost": 3192 },
        7: { "cost": 4440 },
        8: { "cost": 5894 },
        9: { "cost": 7554 },
        10: { "cost": 9419 }
    },
    ItemType.armor: {
        1: { "cost": 35 },
        2: { "cost": 277 },
        3: { "cost": 740 },
        4: { "cost": 1426 },
        5: { "cost": 2336 },
        6: { "cost": 3470 },
        7: { "cost": 4827 },
        8: { "cost": 6407 },
        9: { "cost": 8212 },
        10: { "cost": 10239 }
    }
}

towns = [
    [ # town 0
        { "type": ItemType.sword,               "level": 1},
        { "type": ItemType.mace,                "level": 1},
        { "type": ItemType.spear,               "level": 1},
        { "type": ItemType.dagger,              "level": 1},
        { "type": ItemType.staff,               "level": 1},
        { "type": ItemType.wand,                "level": 1},
        { "type": ItemType.spell_book,          "level": 1},
        { "type": ItemType.alchemical_supplies, "level": 1},
        { "type": ItemType.fire_bomb,           "level": 1},
        { "type": ItemType.frost_bomb,          "level": 1},
        { "type": ItemType.shock_bomb,          "level": 1},
        { "type": ItemType.acid_bomb,           "level": 1},
        { "type": ItemType.flash_bomb,          "level": 1},
        { "type": ItemType.spike_bomb,          "level": 1},
        { "type": ItemType.concussion_bomb,     "level": 1},
        { "type":  ItemType.guided_bomb,        "level": 1},
        { "type": ItemType.fire_ball,           "level": 1},
        { "type": ItemType.thunderbolt,         "level": 1},
        { "type": ItemType.ice_spike,           "level": 1},
        { "type": ItemType.sonic_blast,         "level": 1},
        { "type": ItemType.magic_sword,         "level": 1},
        { "type": ItemType.spear_of_light,      "level": 1},
        { "type": ItemType.rock_smash,          "level": 1},
        { "type": ItemType.armor,               "level": 1}

    ],
    [ # Town 1
        { "type": ItemType.sword,               "level": 2},
        { "type": ItemType.mace,                "level": 2},
        { "type": ItemType.spear,               "level": 2},
        { "type": ItemType.dagger,              "level": 2},
        { "type": ItemType.staff,               "level": 2},
        { "type": ItemType.wand,                "level": 2},
        { "type": ItemType.spell_book,          "level": 2},
        { "type": ItemType.alchemical_supplies, "level": 2},
        { "type": ItemType.fire_bomb,           "level": 2},
        { "type": ItemType.frost_bomb,          "level": 2},
        { "type": ItemType.shock_bomb,          "level": 2},
        { "type": ItemType.acid_bomb,           "level": 2},
        { "type": ItemType.flash_bomb,          "level": 2},
        { "type": ItemType.spike_bomb,          "level": 2},
        { "type": ItemType.concussion_bomb,     "level": 2},
        { "type": ItemType.guided_bomb,         "level": 2},
        { "type": ItemType.fire_ball,           "level": 2},
        { "type": ItemType.thunderbolt,         "level": 2},
        { "type": ItemType.ice_spike,           "level": 2},
        { "type": ItemType.sonic_blast,         "level": 2},
        { "type": ItemType.magic_sword,         "level": 2},
        { "type": ItemType.spear_of_light,      "level": 2},
        { "type": ItemType.rock_smash,          "level": 2},
        { "type": ItemType.armor,               "level": 2}
    ],
    [ # Town 2
        { "type": ItemType.sword,               "level": 3},
        { "type": ItemType.mace,                "level": 3},
        { "type": ItemType.spear,               "level": 3},
        { "type": ItemType.dagger,              "level": 3},
        { "type": ItemType.staff,               "level": 3},
        { "type": ItemType.wand,                "level": 3},
        { "type": ItemType.spell_book,          "level": 3},
        { "type": ItemType.alchemical_supplies, "level": 3},
        { "type": ItemType.fire_bomb,           "level": 3},
        { "type": ItemType.frost_bomb,          "level": 3},
        { "type": ItemType.shock_bomb,          "level": 3},
        { "type": ItemType.acid_bomb,           "level": 3},
        { "type": ItemType.flash_bomb,          "level": 3},
        { "type": ItemType.spike_bomb,          "level": 3},
        { "type": ItemType.concussion_bomb,     "level": 3},
        { "type":  ItemType.guided_bomb,        "level": 3},
        { "type": ItemType.fire_ball,           "level": 3},
        { "type": ItemType.thunderbolt,         "level": 3},
        { "type": ItemType.ice_spike,           "level": 3},
        { "type": ItemType.sonic_blast,         "level": 3},
        { "type": ItemType.magic_sword,         "level": 3},
        { "type": ItemType.spear_of_light,      "level": 3},
        { "type": ItemType.rock_smash,          "level": 3},
        { "type": ItemType.armor,               "level": 3}
    ],
    [ # Town 3
        { "type": ItemType.sword,               "level": 4},
        { "type": ItemType.mace,                "level": 4},
        { "type": ItemType.spear,               "level": 4},
        { "type": ItemType.dagger,              "level": 4},
        { "type": ItemType.staff,               "level": 4},
        { "type": ItemType.wand,                "level": 4},
        { "type": ItemType.spell_book,          "level": 4},
        { "type": ItemType.alchemical_supplies, "level": 4},
        { "type": ItemType.fire_bomb,           "level": 4},
        { "type": ItemType.frost_bomb,          "level": 4},
        { "type": ItemType.shock_bomb,          "level": 4},
        { "type": ItemType.acid_bomb,           "level": 4},
        { "type": ItemType.flash_bomb,          "level": 4},
        { "type": ItemType.spike_bomb,          "level": 4},
        { "type": ItemType.concussion_bomb,     "level": 4},
        { "type": ItemType.guided_bomb,        "level": 4},
        { "type": ItemType.fire_ball,           "level": 4},
        { "type": ItemType.thunderbolt,         "level": 4},
        { "type": ItemType.ice_spike,           "level": 4},
        { "type": ItemType.sonic_blast,         "level": 4},
        { "type": ItemType.magic_sword,         "level": 4},
        { "type": ItemType.spear_of_light,      "level": 4},
        { "type": ItemType.rock_smash,          "level": 4},
        { "type": ItemType.armor,               "level": 4}
    ],
    [ # Town 4
        { "type": ItemType.sword,               "level": 5},
        { "type": ItemType.mace,                "level": 5},
        { "type": ItemType.spear,               "level": 5},
        { "type": ItemType.dagger,              "level": 5},
        { "type": ItemType.staff,               "level": 5},
        { "type": ItemType.wand,                "level": 5},
        { "type": ItemType.spell_book,          "level": 5},
        { "type": ItemType.alchemical_supplies, "level": 5},
        { "type": ItemType.fire_bomb,           "level": 5},
        { "type": ItemType.frost_bomb,          "level": 5},
        { "type": ItemType.shock_bomb,          "level": 5},
        { "type": ItemType.acid_bomb,           "level": 5},
        { "type": ItemType.flash_bomb,          "level": 5},
        { "type": ItemType.spike_bomb,          "level": 5},
        { "type": ItemType.concussion_bomb,     "level": 5},
        { "type": ItemType.guided_bomb,         "level": 5},
        { "type": ItemType.fire_ball,           "level": 5},
        { "type": ItemType.thunderbolt,         "level": 5},
        { "type": ItemType.ice_spike,           "level": 5},
        { "type": ItemType.sonic_blast,         "level": 5},
        { "type": ItemType.magic_sword,         "level": 5},
        { "type": ItemType.spear_of_light,      "level": 5},
        { "type": ItemType.rock_smash,          "level": 5},
        { "type": ItemType.armor,               "level": 5}
    ],
    [ # Town 5
        { "type": ItemType.sword,               "level": 6},
        { "type": ItemType.mace,                "level": 6},
        { "type": ItemType.spear,               "level": 6},
        { "type": ItemType.dagger,              "level": 6},
        { "type": ItemType.staff,               "level": 6},
        { "type": ItemType.wand,                "level": 6},
        { "type": ItemType.spell_book,          "level": 6},
        { "type": ItemType.alchemical_supplies, "level": 6},
        { "type": ItemType.fire_bomb,           "level": 6},
        { "type": ItemType.frost_bomb,          "level": 6},
        { "type": ItemType.shock_bomb,          "level": 6},
        { "type": ItemType.acid_bomb,           "level": 6},
        { "type": ItemType.flash_bomb,          "level": 6},
        { "type": ItemType.spike_bomb,          "level": 6},
        { "type": ItemType.concussion_bomb,     "level": 6},
        { "type": ItemType.guided_bomb,         "level": 6},
        { "type": ItemType.fire_ball,           "level": 6},
        { "type": ItemType.thunderbolt,         "level": 6},
        { "type": ItemType.ice_spike,           "level": 6},
        { "type": ItemType.sonic_blast,         "level": 6},
        { "type": ItemType.magic_sword,         "level": 6},
        { "type": ItemType.spear_of_light,      "level": 6},
        { "type": ItemType.rock_smash,          "level": 6},
        { "type": ItemType.armor,               "level": 6}
    ],
    [ # Town 6
        { "type": ItemType.sword,               "level": 7},
        { "type": ItemType.mace,                "level": 7},
        { "type": ItemType.spear,               "level": 7},
        { "type": ItemType.dagger,              "level": 7},
        { "type": ItemType.staff,               "level": 7},
        { "type": ItemType.wand,                "level": 7},
        { "type": ItemType.spell_book,          "level": 7},
        { "type": ItemType.alchemical_supplies, "level": 7},
        { "type": ItemType.fire_bomb,           "level": 7},
        { "type": ItemType.frost_bomb,          "level": 7},
        { "type": ItemType.shock_bomb,          "level": 7},
        { "type": ItemType.acid_bomb,           "level": 7},
        { "type": ItemType.flash_bomb,          "level": 7},
        { "type": ItemType.spike_bomb,          "level": 7},
        { "type": ItemType.concussion_bomb,     "level": 7},
        { "type":  ItemType.guided_bomb,        "level": 7},
        { "type": ItemType.fire_ball,           "level": 7},
        { "type": ItemType.thunderbolt,         "level": 7},
        { "type": ItemType.ice_spike,           "level": 7},
        { "type": ItemType.sonic_blast,         "level": 7},
        { "type": ItemType.magic_sword,         "level": 7},
        { "type": ItemType.spear_of_light,      "level": 7},
        { "type": ItemType.rock_smash,          "level": 7},
        { "type": ItemType.armor,               "level": 7}
    ],
    [ # Town 7
        { "type": ItemType.sword,               "level": 8},
        { "type": ItemType.mace,                "level": 8},
        { "type": ItemType.spear,               "level": 8},
        { "type": ItemType.dagger,              "level": 8},
        { "type": ItemType.staff,               "level": 8},
        { "type": ItemType.wand,                "level": 8},
        { "type": ItemType.spell_book,          "level": 8},
        { "type": ItemType.alchemical_supplies, "level": 8},
        { "type": ItemType.fire_bomb,           "level": 8},
        { "type": ItemType.frost_bomb,          "level": 8},
        { "type": ItemType.shock_bomb,          "level": 8},
        { "type": ItemType.acid_bomb,           "level": 8},
        { "type": ItemType.flash_bomb,          "level": 8},
        { "type": ItemType.spike_bomb,          "level": 8},
        { "type": ItemType.concussion_bomb,     "level": 8},
        { "type":  ItemType.guided_bomb,        "level": 8},
        { "type": ItemType.fire_ball,           "level": 8},
        { "type": ItemType.thunderbolt,         "level": 8},
        { "type": ItemType.ice_spike,           "level": 8},
        { "type": ItemType.sonic_blast,         "level": 8},
        { "type": ItemType.magic_sword,         "level": 8},
        { "type": ItemType.spear_of_light,      "level": 8},
        { "type": ItemType.rock_smash,          "level": 8},
        { "type": ItemType.armor,               "level": 8}
    ],
    [ # Town 8
        { "type": ItemType.sword,               "level": 9},
        { "type": ItemType.mace,                "level": 9},
        { "type": ItemType.spear,               "level": 9},
        { "type": ItemType.dagger,              "level": 9},
        { "type": ItemType.staff,               "level": 9},
        { "type": ItemType.wand,                "level": 9},
        { "type": ItemType.spell_book,          "level": 9},
        { "type": ItemType.alchemical_supplies, "level": 9},
        { "type": ItemType.fire_bomb,           "level": 9},
        { "type": ItemType.frost_bomb,          "level": 9},
        { "type": ItemType.shock_bomb,          "level": 9},
        { "type": ItemType.acid_bomb,           "level": 9},
        { "type": ItemType.flash_bomb,          "level": 9},
        { "type": ItemType.spike_bomb,          "level": 9},
        { "type": ItemType.concussion_bomb,     "level": 9},
        { "type":  ItemType.guided_bomb,        "level": 9},
        { "type": ItemType.fire_ball,           "level": 9},
        { "type": ItemType.thunderbolt,         "level": 9},
        { "type": ItemType.ice_spike,           "level": 9},
        { "type": ItemType.sonic_blast,         "level": 9},
        { "type": ItemType.magic_sword,         "level": 9},
        { "type": ItemType.spear_of_light,      "level": 9},
        { "type": ItemType.rock_smash,          "level": 9},
        { "type": ItemType.armor,               "level": 9}
    ],
    [ # Town 9
        { "type": ItemType.sword,               "level": 10},
        { "type": ItemType.mace,                "level": 10},
        { "type": ItemType.spear,               "level": 10},
        { "type": ItemType.dagger,              "level": 10},
        { "type": ItemType.staff,               "level": 10},
        { "type": ItemType.wand,                "level": 10},
        { "type": ItemType.spell_book,          "level": 10},
        { "type": ItemType.alchemical_supplies, "level": 10},
        { "type": ItemType.fire_bomb,           "level": 10},
        { "type": ItemType.frost_bomb,          "level": 10},
        { "type": ItemType.shock_bomb,          "level": 10},
        { "type": ItemType.acid_bomb,           "level": 10},
        { "type": ItemType.flash_bomb,          "level": 10},
        { "type": ItemType.spike_bomb,          "level": 10},
        { "type": ItemType.concussion_bomb,     "level": 10},
        { "type":  ItemType.guided_bomb,        "level": 10},
        { "type": ItemType.fire_ball,           "level": 10},
        { "type": ItemType.thunderbolt,         "level": 10},
        { "type": ItemType.ice_spike,           "level": 10},
        { "type": ItemType.sonic_blast,         "level": 10},
        { "type": ItemType.magic_sword,         "level": 10},
        { "type": ItemType.spear_of_light,      "level": 10},
        { "type": ItemType.rock_smash,          "level": 10},
        { "type": ItemType.armor,               "level": 10}
    ]
]


for town_no in range(10):
    for item in towns[town_no]:
        type = item["type"]
        level = item["level"]
        item["cost"] = item_data[type][level]["cost"]


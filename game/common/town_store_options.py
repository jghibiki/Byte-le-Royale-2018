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
        1: { "cost": 0 }
    },
    ItemType.mace: {
        1: { "cost": 0 }
    },
    ItemType.spear: {
        1: { "cost": 0 }
    },
    ItemType.dagger: {
        1: { "cost": 0 }
    },
    ItemType.staff: {
        1: { "cost": 0 }
    },
    ItemType.wand: {
        1: { "cost": 0 }
    },
    ItemType.spell_book: {
        1: { "cost": 0 }
    },
    ItemType.alchemical_supplies: {
        1: { "cost": 0 }
    },
    ItemType.fire_bomb: {
        1: { "cost": 50 }
    },
    ItemType.frost_bomb: {
        1: { "cost": 50 }
    },
    ItemType.shock_bomb: {
        1: { "cost": 50 }
    },
    ItemType.acid_bomb: {
        1: { "cost": 50 }
    },
    ItemType.flash_bomb: {
        1: { "cost": 50 }
    },
    ItemType.spike_bomb: {
        1: { "cost": 50 }
    },
    ItemType.concussion_bomb: {
        1: { "cost": 50 }
    },
    ItemType.fire_ball: {
        1: { "cost": 50 }
    },
    ItemType.thunderbolt: {
        1: { "cost": 50 }
    },
    ItemType.ice_spike: {
        1: { "cost": 50 }
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

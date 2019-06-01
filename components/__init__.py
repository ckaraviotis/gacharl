"""
The Components package holds all of the files required
to instantiate components in the game.

These are split into files for each type of component.

e.g. AI

These are designed around the idea of Capabililties, from Bob Nystrom's
talk at RDC.

An example is below.


class Item {
  Attack melee
  Attack ranged
  Defense defense
  Use use
}

class Use {
  void use() {
  }
}

class FireballUse extends Use {
  void use() {
    // cast fireball
  }
}

const sword = Item(melee: Attack(10, 20))
const fireSword = Item(melee: Attack(30, 40), use: FireballUse())
"""
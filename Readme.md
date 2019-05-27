# GachaRL

Let's learn Python by creating a roguelike!

The overall concept is to unlock items & classes using a gacha-like progression system,
where you initially access one-star versions and can exponentially combine them to rank
them up.

# Roadmap

A list of upcoming things

## Base Features

- A tile-based renderer (essentially the same as the level.render method) to allow easier rendering of menus
- GUI
- Magic system
- Equippable items & stats
- Map generation algorithms (bsp, drunken walk, cellular automata, maze)
- Mixed-mode map generation

## Extended features

- Gacha system for items allowing evolution from 1-5 stars
- XP for items, allowing them to level up independantly of rank, to a rank-based cap (e.g. x = 30, xx = 50)
- Upgrade tree for new tiers of items
- Same system for classes (warrior, rogue etc.)
- Gacha unlocks are permanenent and carry across games
- Winner scoring based on difficulty (e.g. 1* T1 win weighted higher than 5* T3 win)
- Scoring used for further gacha pulls
- Challenge runs for guaranteed gacha pulls
- Gacha combinations happen outside of the main run

# Acknowledgements

- I'm making use of the fantastic [DawnLine](https://opengameart.org/content/dawnlike-16x16-universal-rogue-like-tileset-v181?page=1)
  tileset, by [DragonDePalatino](https://opengameart.org/users/dragondeplatino).

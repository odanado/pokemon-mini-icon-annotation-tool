const fs = require('fs');

const { BattlePokemonSprites } = require('./pokedex-mini')

const sprites = new Map(Object.entries(BattlePokemonSprites))
const altNums = new Map(Object.entries(require('./altNums').altNums))

const data = new Map()

sprites.forEach((v, k) => {
    const { num } = v
    if (num > 0) {
        data.set(k, num)
    }
})

fs.writeFile('data/poke2num.json', (JSON.stringify([...data, ...altNums])))

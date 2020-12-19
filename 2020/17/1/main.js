let input = ["#.#..#.#", "#.......", "####..#.", ".#.#.##.", "..#..#..", "###..##.", ".#..##.#", ".....#.."]
let grid = [[]] // 3d grid, z, y, x
let copy

function start() {
    // add input to grid
    for (let i = 0; i < input.length; i++) {
        grid[0].push(input[i].split(""))
    }

    expand() // expand 1x so there is a layer around the values to check, no index out of bounds

    for (let i = 0; i < 6; i++) {
        expand()
        // deep copy so the cubes can change simultaneously
        copy = JSON.parse(JSON.stringify(grid))

        // change state
        for (let z = 1; z < grid.length - 1; z++) {
            for (let y = 1; y < grid[z].length - 1; y++) {
                for (let x = 1; x < grid[z][y].length - 1; x++) {
                    // for every cube count active adjacent cubes around it
                    let activeSurrounding = 0
                    for (let offsetz = -1; offsetz < 2; offsetz++) {
                        for (let offsety = -1; offsety < 2; offsety++) {
                            for (let offsetx = -1; offsetx < 2; offsetx++) {
                                if (offsetz == 0 && offsety == 0 && offsetx == 0) {
                                    // skip self
                                } else if (grid[z + offsetz][y + offsety][x + offsetx] == "#") {
                                    activeSurrounding++
                                }
                            }
                        }
                    }
                    if (grid[z][y][x] == "#" && (activeSurrounding < 2 || 3 < activeSurrounding)) {
                        copy[z][y][x] = "."
                    } else if (grid[z][y][x] == "." && activeSurrounding == 3) {
                        copy[z][y][x] = "#"
                    }
                }
            }
        }
        // set grid to copy
        grid = JSON.parse(JSON.stringify(copy))
    }

    console.log(count())
}

function expand() {
    // expand existing y and x
    for (let z = 0; z < grid.length; z++) {
        // expand y
        grid[z].unshift([])
        grid[z].push([])
        // fill new y
        let a = 0
        if (z > 0) { // 1e keer push hij goed, daarna elke keer 2 teveel, hiermee fix ik dat, maar ik heb geen idee hoe het komt
            a = 2
        }
        for (let x = 0; x < grid[0][1].length - a; x++) {
            grid[z][0].push(".")
            grid[z][grid[z].length - 1].push(".")
        }
        // expand all x
        for (let y = 0; y < grid[z].length; y++) {
            grid[z][y].unshift(".")
            grid[z][y].push(".")
        }
    }

    // expand z
    grid.unshift([])
    grid.push([])
    // fill new z with y
    for (let y = 0; y < grid[1].length; y++) {
        grid[0].push([])
        grid[grid.length - 1].push([])
        // fill new y
        for (let x = 0; x < grid[1][1].length; x++) {
           grid[0][y].push(".")
           grid[grid.length - 1][y].push(".")
        }
    }
}

function count() {
    // count all active energy source cubes in 3d grid
    let total = 0
    for (let z = 0; z < grid.length; z++) {
        for (let y = 0; y < grid[z].length; y++) {
            for (let x = 0; x < grid[z][y].length; x++) {
                if (grid[z][y][x] == "#") {
                    total++
                }
            }
        }
    }
    return total
}

start();

// eerste deel: 324
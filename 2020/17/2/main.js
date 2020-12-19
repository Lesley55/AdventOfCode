let input = ["#.#..#.#", "#.......", "####..#.", ".#.#.##.", "..#..#..", "###..##.", ".#..##.#", ".....#.."]
let grid = [[[]]] // 4d grid, w, z, y, x
let copy

function start() {
    // add input to grid
    for (let i = 0; i < input.length; i++) {
        grid[0][0].push(input[i].split(""))
    }

    expand() // expand 1x so there is a layer around the values to check, no index out of bounds

    for (let i = 0; i < 6; i++) {
        expand()
        // deep copy so the cubes can change simultaneously
        copy = JSON.parse(JSON.stringify(grid))

        // change state
        for (let w = 1; w < grid.length - 1; w++) {
            for (let z = 1; z < grid[w].length - 1; z++) {
                for (let y = 1; y < grid[w][z].length - 1; y++) {
                    for (let x = 1; x < grid[w][z][y].length - 1; x++) {
                        // for every cube count active adjacent cubes around it
                        let activeSurrounding = 0
                        for (let offsetw = -1; offsetw < 2; offsetw++) {
                            for (let offsetz = -1; offsetz < 2; offsetz++) {
                                for (let offsety = -1; offsety < 2; offsety++) {
                                    for (let offsetx = -1; offsetx < 2; offsetx++) {
                                        if (offsetw == 0 && offsetz == 0 && offsety == 0 && offsetx == 0) {
                                            // skip self
                                        } else if (grid[w + offsetw][z + offsetz][y + offsety][x + offsetx] == "#") {
                                            activeSurrounding++
                                        }
                                    }
                                }
                            }
                        }
                        if (grid[w][z][y][x] == "#" && (activeSurrounding < 2 || 3 < activeSurrounding)) {
                            copy[w][z][y][x] = "."
                        } else if (grid[w][z][y][x] == "." && activeSurrounding == 3) {
                            copy[w][z][y][x] = "#"
                        }
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
    for (let w = 0; w < grid.length; w++) {
        // expand existing y and x
        for (let z = 0; z < grid[w].length; z++) {
            // expand y
            grid[w][z].unshift([])
            grid[w][z].push([])
            // fill new y
            let a = 0
            if (z > 0) { // 1e keer push hij goed, daarna elke keer 2 teveel, hiermee fix ik dat, maar ik heb geen idee hoe het komt
                a = 2
            }
            for (let x = 0; x < grid[w][0][1].length - a; x++) {
                grid[w][z][0].push(".")
                grid[w][z][grid[w][z].length - 1].push(".")
            }
            // expand all x
            for (let y = 0; y < grid[w][z].length; y++) {
                grid[w][z][y].unshift(".")
                grid[w][z][y].push(".")
            }
        }
        
        // expand z
        grid[w].unshift([])
        grid[w].push([])
        // fill new z with y
        for (let y = 0; y < grid[w][1].length; y++) {
            grid[w][0].push([])
            grid[w][grid[w].length - 1].push([])
            // fill new y
            for (let x = 0; x < grid[w][1][1].length; x++) {
                grid[w][0][y].push(".")
                grid[w][grid[w].length - 1][y].push(".")
            }
        }
    }

    // expand w
    grid.unshift([])
    grid.push([])
    // fill new w with z
    for (let z = 0; z < grid[1].length; z++) {
        grid[0].push([])
        grid[grid.length - 1].push([])
        // fill new z with y
        for (let y = 0; y < grid[1][1].length; y++) {
            grid[0][z].push([])
            grid[grid.length - 1][z].push([])
            // fill new y
            for (let x = 0; x < grid[1][1][1].length; x++) {
                grid[0][z][y].push(".")
                grid[grid.length - 1][z][y].push(".")
            }
        }
    }
}

function count() {
    // count all active energy source cubes in 3d grid
    let total = 0
    for (let w = 0; w < grid.length; w++) {
        for (let z = 0; z < grid[w].length; z++) {
            for (let y = 0; y < grid[w][z].length; y++) {
                for (let x = 0; x < grid[w][z][y].length; x++) {
                    if (grid[w][z][y][x] == "#") {
                        total++
                    }
                }
            }
        }
    }
    return total
}

start();

// tweede deel: 1836
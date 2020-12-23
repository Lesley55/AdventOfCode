let input = [3,6,2,9,8,1,7,5,4]
let current = 0
let picked = []

function start() {
    // fill input
    for (let i = Math.max(...input) + 1; i < 1000001; i++) {
        input.push(i)
    }

    // loop 100 moves
    for (let i = 0; i < 10000000; i++) {
        let destination = input[current]
        let cur = input[current]

        // pick 3 cups
        let next = current + 1
        for (let j = 0; j < 3; j++) {
            if (next >= input.length) {
                next = 0
            }
            picked.push(...input.splice(next, 1))
        }

        // get destination
        while (true) {
            destination--
            if (destination < Math.min(...input)) { // lowest cup label
                destination = Math.max(...input) // highest label from cups not picked up
            }
            if (input.indexOf(destination) !== -1) {
                break
            }
        }

        // put cups back
        let index = input.indexOf(destination) + 1
        input.splice(index, 0, ...picked) // insert picked up cups
        picked = [] // empty picked

        // next move
        let l = input.indexOf(cur) + 1
        if (l >= input.length) {
            l = 0
        }
        current = l
    }

    // get all from 1
    let index = input.indexOf(1)
    console.log(input[index+1] * input[index+2])
}

start()

// tweede deel: 
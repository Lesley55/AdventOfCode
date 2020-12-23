let input = [3,6,2,9,8,1,7,5,4]
let current = 0
let picked = []

function start() {
    // loop 100 moves
    for (let i = 0; i < 100; i++) {
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
    let a = []
    let b = []
    let before = true
    for (let i = 0; i < input.length; i++) {
        if (before) {
            if (input[i] !== 1) {
                a.push(input[i])
            } else {
                before = false
            }
        } else {
            b.push(input[i])
        }
    }
    b.push(...a)
    console.log(b.join(""))
}

start()

// eerste deel: 24798635
// tweede deel: 
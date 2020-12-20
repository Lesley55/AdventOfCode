let input = [0,8,15,2,12,1,4]
let unique = new Map()

function start() {
    for (let i = 0; i < input.length-1; i++) {
        unique.set(input[i], i)
    }

    let last = input[input.length-1]
    for (let i = input.length-1; i < 30000000 - 1; i++) {
        if (unique.has(last)) {
            let n = i - unique.get(last)
            unique.set(last, i)
            last = n
        } else {
            unique.set(last, i)
            last = 0
        }
    }
    console.log(last)
}

start();

// tweede deel: 1505722
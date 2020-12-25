let input = 12232269
let input2 = 19452773
let subject = 7

function start() {
    let value = 1
    let i = 1
    while (true) {
        value *= subject
        value = value % 20201227
        if (value == input) {
            console.log("loopsize", i);
            break
        }
        i++
    }
    let key = 1
    for (let j = 0; j < i; j++) {
        key *= input2
        key = key % 20201227
    }
    console.log(key);
}

start()

// eerste deel: 354320
// tweede deel: 
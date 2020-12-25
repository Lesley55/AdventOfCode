// subject number
let input = 12232269
let input2 = 19452773

let u = []
let u2 = []

function start() {
    let value = 1
    let value2 = 1
    let i = 1
    w: while (true) {
        console.log(i);
        value *= input
        value = value % 20201227
        u.push([value, i])
        
        value2 *= input2
        value2 = value2 % 20201227
        u2.push([value2, i])
        
        for (let j = 0; j < u.length; j++) {
            let key = 1
            let check = 1
            let key2 = 1
            let check2 = 1
            for (let k = 0; k < u2[j][1]; k++) {
                key *= value
                key = key % 20201227
            }
            for (let k = 0; k < u[j][1]; k++) {
                key2 *= value2
                key2 = key2 % 20201227
            }
            for (let k = 0; k < i; k++) {
                check *= u2[j][0]
                check = check % 20201227
                
                check2 *= u[j][0]
                check2 = check2 % 20201227
            }
            if (key == check) {
                console.log(key);
                break w
            } else if (key2 == check2) {
                console.log(key2);
                break w
            }
        }

        i++
    }
}

start()

// eerste deel: 
// tweede deel: 
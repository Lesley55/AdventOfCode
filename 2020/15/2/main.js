let input = [0,8,15,2,12,1,4]
let unique = []

function start() {
    for (let i = 0; i < input.length; i++) {
        unique.push([input[i], i])
    }

    let last = input[input.length-1]
    for (let i = input.length; i < 30000000; i++) {
        let a = unique.findIndex((e) => e[0] == last)
        if(a !== -1) {
            last = i - unique[a][1]
        } else {
            last = 0
        }
        // update of push
        if(unique.findIndex((e) => e[0] == last) !== -1) {
            unique[a][1] = i
        } else {
            unique.push([last, i])
        }
    }
    console.log(last)
}

start();

// tweede deel: 
// 289
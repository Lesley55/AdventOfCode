let time = 1002462
let input = [37,"x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",41,"x","x","x","x","x","x","x","x","x",601,"x","x","x","x","x","x","x","x","x","x","x",19,"x","x","x","x",17,"x","x","x","x","x",23,"x","x","x","x","x",29,"x",443,"x","x","x","x","x","x","x","x","x","x","x","x",13]
let a = []
let two = []

function start() {
    for (let i = 0; i < input.length; i++) {
        if(input[i] !== "x") {
            a.push([input[i], input[i]])
            two.push([input[i], i])
        }
    }
    
    // part 1
    for (let i = 0; i < a.length; i++) {
        while(a[i][1] < time) {
            a[i][1] += a[i][0]
        }
    }
    let bus = a[0]
    for (let i = 1; i < a.length; i++) {
        if(a[i][1] < bus[1]) {
            bus = a[i]
        }
    }
    console.log(bus[0] * (bus[1] - time))

    // part 2
    let t = input[0]
    let sort = two.sort(function(a, b) { return b[0] - a[0]; });
    let big = sort[0]
    while(true) {
        let count = 0
        for (let i = 0; i < two.length; i++) {
            if((t + two[i][1]) % two[i][0] == 0) {
                count++
            } else {
                break
            }
        }
        if (count == two.length) {
            break
        } else {
            t += big
        }
    }
    console.log(t);
}

start();

// eerste deel: 3606
// tweede deel: 
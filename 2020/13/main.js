let time = 1002462
let input = [37,"x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",41,"x","x","x","x","x","x","x","x","x",601,"x","x","x","x","x","x","x","x","x","x","x",19,"x","x","x","x",17,"x","x","x","x","x",23,"x","x","x","x","x",29,"x",443,"x","x","x","x","x","x","x","x","x","x","x","x",13]
let a = []

function start() {
    for (let i = 0; i < input.length; i++) {
        if(input[i] !== "x") {
            a.push([input[i], input[i]])
        }
    }
    
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
}

start();

// eerste deel: 3606
// tweede deel: 
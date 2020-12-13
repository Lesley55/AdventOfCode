let time = 1002462
let input = [37,"x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",41,"x","x","x","x","x","x","x","x","x",601,"x","x","x","x","x","x","x","x","x","x","x",19,"x","x","x","x",17,"x","x","x","x","x",23,"x","x","x","x","x",29,"x",443,"x","x","x","x","x","x","x","x","x","x","x","x",13]
let a = []
let two = []

function start() {
    for (let i = 0; i < input.length; i++) {
        if(input[i] !== "x") {
            a.push([input[i], input[i]])
            two.push([input[i], input[i]], i)
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

    // part 2
    let t = input[0]
    while(true) {
        for (let i = 0; i < two.length; i++) {
            while(two[i][1] < t + two[i][2]) {
                two[i][1] += two[i][0]
            }
        }
        let c = 0
        for (let i = 0; i < two.length; i++) {
            if(two[i][1] == t + two[i][2]) {
                c++
            }
        }
        if (c == two.length) {
            break
        }
        t += input[0]
        
        // mogelijk performance gain als je grote getallen hebt of het eerste getal klein is en een niet te grote array om te sorten?
        // let sort = two.sort(function(a, b) { return b[1] - a[1]; }); // sort groot naar klein
        // let w = sort[0][0] / input[0] + 1
        // t += input[0] * w
        // je hoeft niet elke keer array te sorten, 1x de grootste pakken voor de while is beter
    }
    console.log(t);
}

start();

// eerste deel: 3606
// tweede deel: 
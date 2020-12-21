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
    // ik had dit zelf nooit kunnen bedenken.
    // chinese reststelling, ik denk dat ik het kan programmeren, maar de exacte wiskunde erachter is nog een beetje vaag

    let N = two[0][0] // alles keer elkaar
    for (let i = 1; i < two.length; i++) {
        N *= two[i][0]
    }

    let total = 0
    for (let i = 0; i < two.length; i++) {
        // verschil vertrektijd staat aan x kant, maar moet naar andere kant vandaar keer -1
        // x + verschil = 0 (mod input)
        // x = -verschil (mod input)
        // x = -verschil + k * input (mod input)
        // k kleinste positieve getal waarvoor k * input - verschil > 0
        let b = -1 * two[i][1]
        while (b < 0) {
            b += two[i][0]
        }

        // alle input keer elkaar behalve huidige input
        let n = N / two[i][0]

        // n modulo input moet gelijk zijn aan 1, zo niet, tel er dan remain bij op net zo lang tot het wel geld (in mijn geval remain keer temp)
        // b is het aantal keer dat hij opteld dus temp
        let x
        let remain = n % two[i][0]
        let temp = 1
        while (true) {
            if ((remain * temp) % two[i][0] == 1) {
                x = temp
                break
            }
            temp++
        }
        
        total += b * n * x // voor elke input optellen
        if (i == 7) {
            //     console.log(b, n, x); // deze kloppen
            //     console.log(b * n * x); // deze niet
            // total -= 25
            // total += 4
        }
    }

    console.log(total % N)
    // console.log(total);
    // console.log(375 * 2553475888561 * 325); // js kan niet tellen

    // console.log(311204873918371900 == 311204873918371875); // true !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}

start();

// eerste deel: 3606
// tweede deel: 379786358533423 // python antwoord maar kan hij hier dus niet berekenen

// getal te groot om te tellen
// antwoord bij de 7e klopt niet, als ik 375 * 2553475888561 * 325 doe krijg ik
// in javascript:                           311204873918371900
// in python:                               311204873918371875
// in https://www.geogebra.org/scientific:  311204873918371904

let input = [35,111,135,32,150,5,106,154,41,7,27,117,109,63,64,21,138,98,40,71,144,13,66,48,12,55,119,103,54,78,65,112,39,128,53,140,77,34,28,81,151,125,85,124,2,99,131,59,60,6,94,33,42,93,14,141,92,38,104,9,29,100,52,19,147,49,74,70,84,113,120,91,97,17,45,139,90,116,149,129,87,69,20,24,148,18,58,123,76,118,130,132,75,110,105,1,8,86]

function start() {
    let jolt1 = 0
    let jolt3 = 0
    input.push(0) // charging port
    input.sort((a, b) => a - b);
    input.push(input[input.length-1]+3) // device
    for (let i = 1; i < input.length; i++) {
        if (input[i]-input[i-1] == 1) {
            jolt1++
        } else if (input[i]-input[i-1] == 3) {
            jolt3++
        }
    }
    console.log(jolt1 * jolt3)

    // part 2
    let a = [0,1,1,2] // 0 zodat ik geen index out of bounds krijg, 1,1,2 zelf uitgerekend voor de eerste 3 aangezien ik die oversla voor de loop
    for (let j = 3; j < input.length; j++) {
        let b = 0
        // console.log("input", input[j], ": ", input[j-3], input[j] - input[j-3], input[j] - input[j-3] <= 3, input[j-2], input[j] - input[j-2], input[j] - input[j-2] <= 3, input[j-1], input[j] - input[j-1], input[j] - input[j-1] <= 3)
        if (input[j] - input[j-3] <= 3) {
            b += a[a.length-3]
        }
        if (input[j] - input[j-2] <= 3) {
            b += a[a.length-2]
        }
        // if (input[j] - input[j-1] <= 3) { // always true
            b += a[a.length-1]
        // }
        // console.log(a[a.length-3], a[a.length-2], a[a.length-1], "=", b)
        a.push(b)
    }
    // console.log(input)
    // console.log(a)
    console.log(a[a.length-1])
}

start();

// eerste deel: 2030
// tweede deel: 42313823813632
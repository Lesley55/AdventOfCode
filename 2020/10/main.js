let input = [35,111,135,32,150,5,106,154,41,7,27,117,109,63,64,21,138,98,40,71,144,13,66,48,12,55,119,103,54,78,65,112,39,128,53,140,77,34,28,81,151,125,85,124,2,99,131,59,60,6,94,33,42,93,14,141,92,38,104,9,29,100,52,19,147,49,74,70,84,113,120,91,97,17,45,139,90,116,149,129,87,69,20,24,148,18,58,123,76,118,130,132,75,110,105,1,8,86]

function start() {
    let jolt1 = 0
    let jolt3 = 0
    input.push(0) // charging port
    input.sort((a, b) => a - b);
    input.push(input[input.length-1]+3) // device
    let f = []
    for (let i = 1; i < input.length; i++) {
        if (input[i]-input[i-1] == 1) {
            jolt1++
        } else if (input[i]-input[i-1] == 3) {
            jolt3++
        }
        let a = 1
        for (let j = 1; j < 4; j++) {
            if(input[i+j]-input[i-1] <= 3) {
                a++
            }
        }
        f.push(a)
    }
    console.log(jolt1 * jolt3)
    console.log(f)
    console.log(input)
}

start();

// eerste deel: 2030
// tweede deel:
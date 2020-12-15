let input = [0,8,15,2,12,1,4]

function start() {
    while(input.length < 2020) {
        let last = input[input.length-1]
        let found = false
        for (let j = input.length-2; j >= 0; j--) {
            if (last == input[j]) {
                input.push(input.length - 1 - j)
                found = true
                break;
            }
        }
        if (!found) {
            input.push(0)
        }
    }
    console.log(input[input.length-1])
}

start();

// eerste deel: 289
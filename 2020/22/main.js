let player1 = [42,29,12,40,47,26,11,39,41,13,8,50,44,33,5,27,10,25,17,1,28,22,6,32,35]
let player2 = [19,34,38,21,43,14,23,46,16,3,36,31,37,45,30,15,49,48,24,9,2,18,4,7,20]

function start() {
    while (player1.length !== 0 && player2.length !== 0) {
        card1 = player1.shift()
        card2 = player2.shift()
        if (card1 < card2) {
            player2.push(card2)
            player2.push(card1)
        } else {
            player1.push(card1)
            player1.push(card2)
        }
    }
    let winner
    if (player1.length == 0) {
        winner = player2
    } else {
        winner = player1
    }

    let score = 0
    winner.reverse()
    for (let i = 0; i < winner.length; i++) {
        score += winner[i] * (i+1)
    }
    console.log(score)
}

start()

// eerste deel: 32495
// tweede deel: 
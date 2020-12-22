let input1 = [42,29,12,40,47,26,11,39,41,13,8,50,44,33,5,27,10,25,17,1,28,22,6,32,35]
let input2 = [19,34,38,21,43,14,23,46,16,3,36,31,37,45,30,15,49,48,24,9,2,18,4,7,20]

function start() {
    let end = recurse(input1, input2)
    let deck = end[1]
    let score = 0
    deck.reverse()
    for (let i = 0; i < deck.length; i++) {
        score += deck[i] * (i+1)
    }
    console.log(score)
}

function recurse(p1, p2) {
    // deep copy, just for sure
    let player1 = JSON.parse(JSON.stringify(p1))
    let player2 = JSON.parse(JSON.stringify(p2))
    let past = new Map()
    while (player1.length !== 0 && player2.length !== 0) {
        // before drawing, check if previous rounds had same order
        if (past.has("1_" + player1.toString()) || past.has("2_" + player2.toString())) {
            return ["player1", player1]
        } else {
            past.set("1_" + player1.toString(), 0) // first value = player + deck, has to be unique, second value doesn't matter so i just put a zero
            past.set("2_" + player2.toString(), 0) // toString because array as key doesn't work
        }
        let card1 = player1.shift()
        let card2 = player2.shift()
        if (player1.length >= card1 && player2.length >= card2) {
            let rec1 = []
            let rec2 = []
            for (let i = 0; i < card1; i++) {
                rec1.push(player1[i])
            }
            for (let i = 0; i < card2; i++) {
                rec2.push(player2[i])
            }
            let player = recurse(rec1, rec2)
            if (player[0] == "player1") {
                player1.push(card1)
                player1.push(card2)
            } else {
                player2.push(card2)
                player2.push(card1)
            }
        } else if (card1 > card2) {
            player1.push(card1)
            player1.push(card2)
        } else {
            player2.push(card2)
            player2.push(card1)
        }
    }

    let winner
    if (player1.length == 0) {
        winner = ["player2", player2]
    } else {
        winner = ["player1", player1]
    }
    return winner
}

start()

// tweede deel: 32665
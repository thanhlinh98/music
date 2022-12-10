radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        for (let index = 0; index < 8; index++) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . # . # .
                . # # # .
                # # # # #
                `)
            basic.showLeds(`
                . # . # .
                . # . # .
                # # . # #
                # # # # #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . # . # .
                # # . # #
                # # # # #
                `)
        }
    } else if (receivedNumber == 2) {
        for (let index = 0; index < 3; index++) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
                `)
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . .
                # # # . .
                # # # # #
                `)
            basic.showLeds(`
                # . # . .
                # . # . .
                # # # . #
                # # # . #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . # . .
                # . # . .
                # # # . #
                # # # # #
                `)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                # . # . .
                # # # # #
                `)
        }
    } else if (receivedNumber == 3) {
        basic.showLeds(`
            . # # # .
            # . . . #
            . # # # .
            . . . . .
            . . # . .
            `)
    } else if (receivedNumber == 4) {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            # # # # #
            . # . # .
            `)
    } else if (receivedNumber == 5) {
        basic.clearScreen()
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.A, function () {
    a = randint(1, 4)
    if (a == 1) {
        radio.sendNumber(1)
        music.setVolume(60)
        music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
    } else if (a == 2) {
        radio.sendNumber(2)
        music.setVolume(60)
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
    } else if (a == 3) {
        radio.sendNumber(3)
        music.setVolume(80)
        music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.Once)
    } else if (a == 4) {
        radio.sendNumber(4)
        music.setVolume(60)
        music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(5)
    basic.clearScreen()
})
let a = 0
radio.setGroup(68)
basic.forever(function () {
	
})

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
        for index in range(8):
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # . # .
                                . # # # .
                                # # # # #
            """)
            basic.show_leds("""
                . # . # .
                                . # . # .
                                # # . # #
                                # # # # #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # . # .
                                # # . # #
                                # # # # #
            """)
    elif receivedNumber == 2:
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
        for index2 in range(4):
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                # # # # #
            """)
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # . # . .
                                # # # . .
                                # # # # #
            """)
            basic.show_leds("""
                # . # . .
                                # . # . .
                                # # # . #
                                # # # . #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . # . .
                                # . # . .
                                # # # . #
                                # # # # #
            """)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                # . # . .
                                # # # # #
            """)
    elif receivedNumber == 3:
        basic.show_leds("""
            . # # # .
                        # . . . #
                        . # # # .
                        . . . . .
                        . . # . .
        """)
    elif receivedNumber == 4:
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . . . #
                        # # # # #
                        . # . # .
        """)
    elif receivedNumber == 5:
        basic.clear_screen()
    else:
        basic.show_icon(IconNames.NO)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global a
    a = 2
    if a == 1:
        radio.send_number(1)
        music.set_volume(60)
        music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
    elif a == 2:
        radio.send_number(2)
        music.set_volume(60)
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
    elif a == 3:
        radio.send_number(3)
        music.set_volume(80)
        music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
    elif a == 4:
        radio.send_number(4)
        music.set_volume(60)
        music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(5)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

a = 0
radio.set_group(68)

def on_forever():
    pass
basic.forever(on_forever)

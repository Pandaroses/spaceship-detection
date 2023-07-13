
#actions to be done when 
def on_received_number(cb):
    if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) >= strength:
        basic.show_number(cb)
        radio.send_number(id2)
        music.play(music.builtin_playable_sound_effect(soundExpression.sad),music.PlaybackMode.IN_BACKGROUND)
        datalogger.log(datalogger.create_cv("ID", cb),datalogger.create_cv("SignalStrength",radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)))
radio.on_received_number(on_received_number)

# setting initial variables
strength = -50
radio.set_transmit_power(7)
radio.set_group(10)
id2 = Math.floor(Math.random() * 9999)
radio.on()
datalogger.set_column_titles("ID", "SignalStrength")


#constant pinging every 350ms
def on_forever():
    radio.send_number(id2)
    basic.pause(350)
basic.forever(on_forever)

def on_received_number(cb):
     if (radio.receivedPacket(RadioPacketProperty.SignalStrength) >= strength) {
     basic.showNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength))
     radio.sendNumber(id2)
     music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
     }
radio.on_received_number(on_received_number)


strength = -42
radio.set_transmit_power(7)
radio.set_group(10)
id2 = Math.floor(Math.random() * 9999)
radio.on()

def on_forever():
    radio.send_number(id2)
    basic.pause(350)
basic.forever(on_forever)

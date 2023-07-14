radio.onReceivedString((cb) => {
    let strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    // Implement sound functions inside the loop
    if (strength >= -50 && strength < -40){
    basic.showString(cb)}
    else if (strength >= -40 && strength < - 35){
    basic.showString(cb)}
    else if (strength >= - 35){
        basic.showString(cb)}
    radio.sendString(id)
})



radio.setTransmitPower(7)
radio.setGroup(10)
// SET ID TO TEAM NUMBER e.g. "1A"
let id = ""
radio.on()


basic.forever(() => {
    radio.sendString(id)
    
    basic.pause(350)
})
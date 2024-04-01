const A = 14.713
const B = -2.396
const C = -1.787
function getOmega(alt) {
    let phi = alt * (Math.PI / 180)
    let omega = A + B * (Math.sin(phi)) ** 2 + C * (Math.sin(phi)) ** 4
    return 360/omega
}
let output = document.getElementById('answer')
document.getElementById('run').addEventListener('click', (event) => {
    altitude = document.getElementById('altitude').value
    if (!isNaN(altitude)) {
        output.innerText = getOmega(Number(altitude))
    }
    else {
        output.innerText = '?'
    }
})
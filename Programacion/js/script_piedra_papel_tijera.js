// 1 es piedra, 2 es papel, 3 es tijera
function aleatorio(min, max) {
    random = Math.floor(Math.random() * (max - min + 1) + min)
    //formula para poner numeros aleatorios enteros en un intervalo definido
    return random
}

function eleccion(jugada) {
    let resultado = ""
    if (jugada == 1) {
        resultado = "Piedra 🥌"
    }
    else if (jugada == 2) {
        resultado = "Papel 📰"
    }
    else if (jugada == 3) {
        resultado = "Tijera ✂️"
    }
    else {
        resultado = "No valido"
    }
    // funcion para indicar que cada numero es una opcion
    return resultado
}

let jugador = 0
let pc = 0
let triunfos = 0
let perdidas = 0
// let es para definir variables

while (triunfos < 3 && perdidas < 3) {
    pc = aleatorio(1, 3)
    jugador = prompt("Elige 1 para piedra, 2 para papel y 3 para tijera")
    alert("PC elige " + eleccion(pc))
    alert("jugador elige " + eleccion(jugador))

    // combate pc vs jugador
    if (pc == jugador) {
        alert("empate")
    }
    // && es el and en html
    else if ((jugador == 1 && pc == 3) || (jugador == 2 && pc == 1) || (jugador == 3 && pc == 2)) {
        alert("Tu ganas")
        triunfos = triunfos + 1
    }
    else {
        alert("Tu pierdes")
        perdidas = perdidas + 1
    }

}
alert("Ganaste " + triunfos + " veces, Perdiste " + perdidas + " veces")
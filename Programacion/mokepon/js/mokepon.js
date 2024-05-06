const seccion_seleccionar_ataque = document.getElementById('seleccionar-ataque')
const seccion_reiniciar = document.getElementById('reiniciar-partida')
const boton_mascota = document.getElementById('pokemon')
//la variable boton asociela al boton con el id en este caso pokemon
const boton_reiniciar = document.getElementById('reiniciar')

const seccion_seleccionar_mascota = document.getElementById('seleccionar-mascota')

const span_pokemon_propio = document.getElementById('pokemon-propio')

const span_pokemon_enemigo = document.getElementById('pokemon-enemigo')

const seccion_mensajes = document.getElementById('resultado')
const mensajes_ataques_jugador = document.getElementById('ataque-jugador')
const mensajes_ataques_enemigo = document.getElementById('ataque-enemigo')

const span_vidas_propias = document.getElementById('vidas-jugador')
const span_vidas_enemigo = document.getElementById('vidas-enemigo')
//const es para constante y let para variable
const contenedor_pokemones = document.getElementById('contenedor-pokemones')
const contenedor_ataques = document.getElementById('contenedor-ataques')

const seccion_ver_mapa = document.getElementById('ver-mapa')
const mapa = document.getElementById('mapa')

const ancho_maximo = 100



let pokemones = []
let opcion_pokemon
let ataque_dejugador = []
let ataque_enemigo = []
let inputsquirtle
let inputbullbasaur
let inputcharmander
let boton_fuego
let boton_tierra
let boton_agua
let botones = []
let pokemon_jugador
let pokemon_jugador_objeto
let ataque_jugador
let ataque_pokemon_enemigo
let ataques_pokemon_elegido
let index_jugador
let index_enemigo
let victorias_jugador = 0
let victorias_enemigo = 0
let lienzo = mapa.getContext("2d")
//el modulo get context 2d es para indicar que es en 2d y se pueda dibujar dentro del canvas
let intervalo
let mapa_background = new Image()
mapa_background.src = "./mokemap.jpg"
let altura_mapa
let ancho_mapa = window.innerWidth - 500

altura_mapa = ancho_mapa * 600 / 800

mapa.width = ancho_mapa
mapa.height = altura_mapa

if (ancho_mapa > ancho_maximo) {
    ancho_mapa = ancho_maximo -20
}

class Pokemon {
    constructor(nombre, foto, vida, mapafoto) {
        this.nombre = nombre
        this.foto = foto
        this.vida = vida
        this.ataques = []
        this.ancho = 80
        this.alto = 80
        this.x = aleatorio(0, mapa.width - this.ancho)
        this.y = aleatorio (0, mapa.height - this.alto)
        this.mapafoto = new Image()
        this.mapafoto.src = foto
        this.velocidadx = 0
        this.velocidady = 0
    }

    pintar_pokemon() {
        lienzo.drawImage(
            this.mapafoto,
            this.x,
            this.y,
            this.ancho,
            this.alto,
        )
        // fill Rect genera un rectangulo que dice en la coordenadas x,y pongale un ancho de 20 y alto de 40
        //Draw image es para poner imagen y no rectangulo
    }
}
// la clase es para almacenar cosas del mismo tipo con diferentes propiedades, como nombre, foto en este caso haciendo referencia a los pokemones
//la herramienta constructor es para decir las propiedades y el this es para asignar nombre a las propiedades

let Squirtle = new Pokemon('Squirtle', './squirtle.png', 5, './squirtle.png')
let Bullbasaur = new Pokemon('Bullbasaur', './Bulbasaur.jpg', 5, './Bulbasaur.jpg')
let Charmander = new Pokemon('Charmander', './charmander.png', 5, './charmander.png')
// con el new y la clase se le agrega a la clase

let Squirtle_enemigo = new Pokemon('Squirtle', './squirtle.png', 5, './squirtle.png')
let Bullbasaur_enemigo = new Pokemon('Bullbasaur', './Bulbasaur.jpg', 5, './Bulbasaur.jpg')
let Charmander_enemigo = new Pokemon('Charmander', './charmander.png', 5, './charmander.png')

Squirtle.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '💧', id: 'agua' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🌱', id: 'tierra' },
)
//push es como un append para meterle a arrays o listas, valores

Bullbasaur.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🌱', id: 'tierra' },
    { nombre: '🌱', id: 'tierra' },
    { nombre: '🌱', id: 'tierra' },
)

Charmander.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🔥', id: 'fuego' },
    { nombre: '🔥', id: 'fuego' },
    { nombre: '🌱', id: 'tierra' },
)

Squirtle_enemigo.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '💧', id: 'agua' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🌱', id: 'tierra' },
)

Bullbasaur_enemigo.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🌱', id: 'tierra' },
    { nombre: '🌱', id: 'tierra' },
    { nombre: '🌱', id: 'tierra' },
)

Charmander_enemigo.ataques.push(
    { nombre: '🔥', id: 'fuego' },
    { nombre: '💧', id: 'agua' },
    { nombre: '🔥', id: 'fuego' },
    { nombre: '🔥', id: 'fuego' },
    { nombre: '🌱', id: 'tierra' },
)

pokemones.push(Squirtle, Bullbasaur, Charmander)

function iniciar_juego() {

    seccion_seleccionar_ataque.style.display = 'none'
    seccion_ver_mapa.style.display = 'none'
    // el for each es un ciclo for iterativo que va a repetir el nombre que se tenga arriba en el array para ponerlo aqui
    //y aplicar el input y el label de forma que agregue cada vez que se mete algun pokemon nuevo y se pone el += para que coja todos los valores
    pokemones.forEach((pokemon) => {
        opcion_pokemon = `<input type="radio" name="pokemon"
        id=${pokemon.nombre} /> 
        <label class="pokemones" for=${pokemon.nombre}>
        <p>${pokemon.nombre}</p>
        <img src=${pokemon.foto}>
        </label>
        `
        contenedor_pokemones.innerHTML += opcion_pokemon

        inputsquirtle = document.getElementById('Squirtle')
        inputbullbasaur = document.getElementById('Bullbasaur')
        inputcharmander = document.getElementById('Charmander')
    })
    // el type es para escoger la entrada ya sea opcion, chechbox, texto
    // el name es para agrupar los puntos de la misma seccion  
    // el id es para relacionar el boton a la opcion
    // el label for es para asociar el nombre, el texto como opcion para seleccionar no solo el botoncito

    seccion_reiniciar.style.display = 'none'
    //el style display none quita la seccion en el html la oculta en este caso para que se elija primero el pokemon
    boton_mascota.addEventListener('click', seleccionar_pokemon)
    //a ese boton ademas activese cuando haga click y ademas ejecute la funcion seleccionar_pokemon

    boton_reiniciar.addEventListener('click', reiniciar_juego)
    //a ese boton ademas activese cuando haga click y ademas ejecute la funcion reiniciar
}

function seleccionar_pokemon() {

    //el style display flex vuelve y muestra lo oculto 
    seccion_seleccionar_mascota.style.display = 'none'

    if (inputsquirtle.checked) {
        span_pokemon_propio.innerHTML = inputsquirtle.id
        pokemon_jugador = inputsquirtle.id
    }
    //el modulo checked es para decir si esa opcion ha estado seleccionada
    // el span es para poner un nombre dinamico en el html, y la opcion inner HTML espara cambiar el nombre por el que ponga ahi
    else if (inputbullbasaur.checked) {
        span_pokemon_propio.innerHTML = inputbullbasaur.id
        pokemon_jugador = inputbullbasaur.id
    }
    else if (inputcharmander.checked) {
        span_pokemon_propio.innerHTML = inputcharmander.id
        pokemon_jugador = inputcharmander.id
    }
    else {
        alert("Debes seleccionar una opcion")
        reiniciar_juego()
    }

    extraer_ataques(pokemon_jugador)
    seccion_ver_mapa.style.display = 'flex'
    iniciar_mapa()

    // ponerlo aqui para que se active con el boton arriba y con esta funcion, no importa si la funcion esta debajo de esta
}

function extraer_ataques(pokemon_jugador) {
    let ataques
    for (let i = 0; i < pokemones.length; i++) {
        if (pokemon_jugador === pokemones[i].nombre) {
            ataques = pokemones[i].ataques
        }
    }
    mostrar_ataques(ataques)
}
//sirve para que de la lista de pokemones cuando sea el elegido meta los ataques en el campo de ataques

function mostrar_ataques(ataques) {
    ataques.forEach((ataque) => {
        ataques_pokemon_elegido = `
        <button id=${ataque.id} class="boton-ataque">${ataque.nombre}</button>
        `
        //los botones sirven para asignarle funciones a clickear 
        contenedor_ataques.innerHTML += ataques_pokemon_elegido
    })

    botones = document.querySelectorAll('.boton-ataque')
    //selecciona todos los elementos que tengan tal cosa es decir una clase
}

function secuencia_ataque() {
    botones.forEach((boton) => {
        boton.addEventListener('click', (e) => {
            // se llama con el id que se le puso al boton en html
            if (e.target.textContent == '🔥') {
                ataque_dejugador.push('🔥')
                console.log(ataque_dejugador)
                boton.style.background = '#F55050'
                boton.disabled = true
                //el disabled desactiva los botones no los deja usar, lo cual sirve para cuando se crea un mensaje final
            }
            else if (e.target.textContent == '💧') {
                ataque_dejugador.push('💧')
                console.log(ataque_dejugador)
                boton.style.background = '#F55050'
                boton.disabled = true
            }
            else {
                ataque_dejugador.push('🌱')
                console.log(ataque_dejugador)
                boton.style.background = '#F55050'
                boton.disabled = true
            }
            ataque_aleatorio_enemigo()
        })
        // (e) es el evento per se en este caso el evento de click
        // target y text content es cada que clickeo coge el valor que hay en el boton y si es el mismo agregalo al array de ataque del jugador
    })

}

function pokemon_enemigo(enemigo) {
    span_pokemon_enemigo.innerHTML = enemigo.nombre
    // coger la id del html de span y con el inner le agregamos el nombre del valor de la lista de pokemones aleatorio
    ataque_pokemon_enemigo = enemigo.ataques
    secuencia_ataque()
}

function ataque_aleatorio_enemigo() {
    let enemigo = aleatorio(0, ataque_pokemon_enemigo.length - 1)

    if (enemigo == 0 || enemigo == 1) {
        ataque_enemigo.push('🔥')
    }
    else if (enemigo == 3 || enemigo == 4) {
        ataque_enemigo.push('🌱')
    }
    else {
        ataque_enemigo.push('💧')
    }
    iniciar_batalla()


    // genere la batalla quien crea el mensaje despues del ataque para que no se borre el historial
}

function iniciar_batalla() {
    if (ataque_dejugador.length === 5) {
        batalla()
    }
}

function index_oponentes(jugador, enemigo) {
    index_jugador = ataque_dejugador[jugador]
    index_enemigo = ataque_enemigo[enemigo]
}

function batalla() {

    for (let i = 0; i < ataque_dejugador.length; i++) {
        if (ataque_dejugador[i] == ataque_enemigo[i]) {
            index_oponentes(i, i)
            crear_mensaje('Empate')
            span_vidas_propias.innerHTML = victorias_jugador
        }
        else if (ataque_dejugador[i] == '🔥' && ataque_enemigo[i] == '🌱') {
            index_oponentes(i, i)
            crear_mensaje('Ganaste')
            victorias_jugador++
            span_vidas_propias.innerHTML = victorias_jugador
        }
        else if (ataque_dejugador[i] == '💧' && ataque_enemigo[i] == '🔥') {
            index_oponentes(i, i)
            crear_mensaje('Ganaste')
            victorias_jugador++
            span_vidas_propias.innerHTML = victorias_jugador
        }
        else if (ataque_dejugador[i] == '🌱' && ataque_enemigo[i] == '💧') {
            index_oponentes(i, i)
            crear_mensaje('Ganaste')
            victorias_jugador++
            span_vidas_propias.innerHTML = victorias_jugador
        }
        else {
            index_oponentes(i, i)
            crear_mensaje('Perdiste')
            victorias_enemigo++
            span_vidas_enemigo.innerHTML = victorias_enemigo
        }
        // el ++ es sumar 1 al que trae
        //el crear mensaje coge la variable resultado y reemplazela en el texto en este caso le doy lo que debe decir
        // && es el and en html y las dos rayas es el or en html
    }
    revisar_victorias()
}

function revisar_victorias() {
    if (victorias_jugador == victorias_enemigo) {
        crear_mensaje_final('Empate 🙃')
        // se lista esta funcion donde se crea el mensaje en vez de hacerlo en estos ifs
    }
    else if (victorias_jugador > victorias_enemigo) {
        crear_mensaje_final('Has Ganado! 😎')
    }
    else {
        crear_mensaje_final('Has Perdido! 😣')
    }
}

function crear_mensaje(resultado_batalla) {
    let nuevo_ataque_jugador = document.createElement('p')
    let nuevo_ataque_enemigo = document.createElement('p')
    // create element sirve para agregar algo en html, un parrafo o algo desde el javascript, en este caso una nueva variable para que cree el elemento del parrafo

    seccion_mensajes.innerHTML = resultado_batalla
    nuevo_ataque_jugador.innerHTML = index_jugador
    nuevo_ataque_enemigo.innerHTML = index_enemigo
    // a ese parrafo con inner html se introduce informacion al parrafo creado

    mensajes_ataques_jugador.appendChild(nuevo_ataque_jugador)
    mensajes_ataques_enemigo.appendChild(nuevo_ataque_enemigo)
    //con appendchild se le mete el parrafo dentra de la seccion de ataques jugador, en este caso al elemento con el id de ataques del jugador y enemigos en el html
}

function crear_mensaje_final(resultado) {
    // create element sirve para agregar algo en html, un parrago o algo desde el javascript
    seccion_mensajes.innerHTML = resultado
    // con inner html se introduce informacion al parrafo creado
    //con appendchild se le mete el parrafo dentra de la seccion en este caso al elemento con el id
    seccion_reiniciar.style.display = 'flex'
}

function reiniciar_juego() {
    location.reload()
    //es un refrescar o actualizar el navegador o location
}

function aleatorio(min, max) {
    random = Math.floor(Math.random() * (max - min + 1) + min)
    //formula para poner numeros aleatorios enteros en un intervalo definido
    return random
}

function pintar_canvas() {
    pokemon_jugador_objeto.x = pokemon_jugador_objeto.x + pokemon_jugador_objeto.velocidadx
    pokemon_jugador_objeto.y = pokemon_jugador_objeto.y + pokemon_jugador_objeto.velocidady
    lienzo.clearRect(0, 0, mapa.width, mapa.height)
    //limpia el canvas para poder mostrar el nuevo
    lienzo.drawImage(
        mapa_background,
        0,
        0,
        mapa.width,
        mapa.height,
    )
    pokemon_jugador_objeto.pintar_pokemon()
    // del pokemon saque la funcion pintar pokemon de la clase
    Squirtle_enemigo.pintar_pokemon()
    Bullbasaur_enemigo.pintar_pokemon()
    Charmander_enemigo.pintar_pokemon()

    if (pokemon_jugador_objeto.velocidadx != 0 || pokemon_jugador_objeto.velocidady != 0 ) {
        revisar_colision(Squirtle_enemigo)
        revisar_colision(Bullbasaur_enemigo)
        revisar_colision(Charmander_enemigo)
    }

    
    // para que cuando realice la colision se quede quieto el pokemon y no entre en un bucle infinito de colisiones

}

function mover_squirtle_izq() {
    pokemon_jugador_objeto.velocidadx = -5
    //Squirtle.x = Squirtle.x - 5
    // mueve la posicion en x con x +5
}

function mover_squirtle_der() {
    pokemon_jugador_objeto.velocidadx = 5
}

function mover_squirtle_arr() {
    pokemon_jugador_objeto.velocidady = -5
}

function mover_squirtle_abj() {
    pokemon_jugador_objeto.velocidady = 5
}

function detener_movimiento() {
    pokemon_jugador_objeto.velocidadx = 0
    pokemon_jugador_objeto.velocidady = 0
}

function presion_tecla(evento) {
    switch (evento.key) {
        case 'ArrowUp':
            mover_squirtle_arr()
            break;
        case 'ArrowDown':
            mover_squirtle_abj()
            break;
        case 'ArrowLeft':
            mover_squirtle_izq()
            break;
        case 'ArrowRight':
            mover_squirtle_der()
            break
        default:
            break;
    }
}
//el switch case son muchas condiciones como muchos if anidados y que para cada una haga tal cosa si se cumple

function iniciar_mapa() {

    pokemon_jugador_objeto = obtener_objeto_pokemon(pokemon_jugador)

    intervalo = setInterval(pintar_canvas, 50)
    // la funcion setinterval dice que cada tanto ejecute la funcion en milisegundos
    window.addEventListener('keydown', presion_tecla)
    //cuando presiono tecla doy movimiento
    window.addEventListener('keyup', detener_movimiento)
    //cuando la suelto se detiene
}

function obtener_objeto_pokemon() {
    for (let i = 0; i < pokemones.length; i++) {
        if (pokemon_jugador === pokemones[i].nombre) {
            return pokemones[i]
        }
    }
}
// es para extraer el nombre del pokemon elegido y poderlo emplear en las funciones de movimiento y demas

function revisar_colision(enemigo){
    const arriba_enemigo = enemigo.y
    const abajo_enemigo = enemigo.y + enemigo.alto
    const derecha_enemigo = enemigo.x + enemigo.ancho
    const izquierda_enemigo = enemigo.x

    const arriba_pokemon = pokemon_jugador_objeto.y
    const abajo_pokemon = pokemon_jugador_objeto.y + pokemon_jugador_objeto.alto
    const derecha_pokemon = pokemon_jugador_objeto.x + pokemon_jugador_objeto.ancho
    const izquierda_pokemon = pokemon_jugador_objeto.x

    if(
        abajo_pokemon < arriba_enemigo || arriba_pokemon > abajo_enemigo || derecha_pokemon < izquierda_enemigo || izquierda_pokemon > derecha_enemigo
        // formula para colisiones en canvas
    ){
        return 
    }
    detener_movimiento()
    clearInterval(intervalo)
    seccion_seleccionar_ataque.style.display = 'flex'
    seccion_ver_mapa.style.display = 'none'
    pokemon_enemigo(enemigo)
    
}

window.addEventListener('load', iniciar_juego)
// activa funcion iniciar juego cuando se cargo todo el html para que el codigo en js no importa donde este ubicado en el html

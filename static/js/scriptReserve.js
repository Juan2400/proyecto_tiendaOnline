const dateSel = document.getElementById('dateSel');
const timeMeet = document.getElementById('timeMeet');
const eventType = document.getElementById('eventType');
const ctp = document.getElementById('ctp');
const messagebtn = document.getElementById('messagebtn');
const reserveForm = document.getElementById('reserveForm');
const mensajeFlotante = document.getElementById('mensaje-flotante');
const textoMensaje = document.getElementById('texto-mensaje');
const botonAceptar = document.getElementById('boton-aceptar');



messagebtn.addEventListener('click', (e) => {
    e.preventDefault()
    let warnings = phpMessage ? `${phpMessage}<br>` : '';
    let register = false;
    /*expresiónes regulares*/
    
    const valueDateSel = new Date(dateSel.value);
    const today = new Date();
    today.setHours(0, 0, 0, 0); // Establecer la hora a las 00:00:00 para comparar solo la fecha

    if (isNaN(valueDateSel) || valueDateSel.getDay() === 6 || valueDateSel < today) {
        warnings += `No se permite reservar para el día seleccionado <br>`;
        register = true;
    }

    if (timeMeet.value < '08:30' || timeMeet.value > '20:00') {
        warnings += `La hora debe estar en un rango de 8:30 AM a 8:00 PM <br>`;
        register = true;
    }

    if (eventType.value === "") {
        warnings += `Por favor seleccione el tipo de evento<br>`;
        register = true;
    } else if (
        eventType.value !== "Cumpleaños" &&
        eventType.value !== "Reunión de amigos" &&
        eventType.value !== "Cena familiar" &&
        eventType.value !== "Boda"
    ) {
        warnings += `Seleccione un tipo de evento válido<br>`;
        register = true;
    }

    const valueCtp = parseInt(ctp.value);
    if (isNaN(valueCtp) || valueCtp < 2 || valueCtp > 16) {
        warnings += `La cantidad de personas debe ser entre 1 y 8 <br>`;
        register = true;
    }

    if (register) {
        textoMensaje.innerHTML = warnings; //Advertencias en el mensaje flotante
        mensajeFlotante.style.display = 'block'; // Mostrar el mensaje flotante
        //alert(warnings);
    } else {
        textoMensaje.innerHTML = `Los datos son correctos<br>`; // Éxito
        mensajeFlotante.style.display = 'block'; // Mostrar el mensaje flotante
    }

});

botonAceptar.addEventListener('click', () => {
    mensajeFlotante.style.display = 'none'; // Ocultar el mensaje flotante al aceptar
    if (textoMensaje.innerHTML === `Los datos son correctos<br>`) {
        reserveForm.submit(); // Enviar el formulario solo si se acepta el mensaje de éxito
    }
});




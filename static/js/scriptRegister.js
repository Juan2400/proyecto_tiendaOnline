document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');

    form.addEventListener('submit', function (event) {
        // Evitamos que se envíe en automático para poder depurar
        // event.preventDefault();

        console.log('Formulario enviado');

        // Verificamos que todos los campos estén completos
        const inputs = form.querySelectorAll('input');
        let allFilled = true;

        inputs.forEach(function (input) {
            if (input.value.trim() === '' && input.type !== 'hidden') {
                console.log('Campo vacío:', input.name || input.id);
                allFilled = false;
            }
        });

        if (allFilled) {
            console.log('Todos los campos están completos');
            // Descomenta la siguiente línea cuando estés listo para enviar el formulario
            // form.submit();
        } else {
            console.log('Hay campos vacíos');
        }
    });
});
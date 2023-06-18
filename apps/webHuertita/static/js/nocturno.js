  /* Modo noche */
  
  $(document).ready(function() {
    // Obtener el valor actual del modo desde el almacenamiento local
    var modoActual = localStorage.getItem('modo');

    // Establecer el modo predeterminado en "claro" si no hay un valor almacenado
    if (!modoActual) {
        modoActual = 'claro';
        localStorage.setItem('modo', modoActual);
    }

    // Establecer el estado del interruptor según el valor almacenado
    if (modoActual === 'oscuro') {
        $('#modoOscuro').prop('checked', true);
        $('body').addClass('modo-oscuro');
    } else {
        $('#modoOscuro').prop('checked', false);
        $('body').removeClass('modo-oscuro');
    }

    // Detectar el cambio de estado del interruptor de modo oscuro
    $('#modoOscuro').change(function() {
        if ($(this).is(':checked')) {
            // Si el interruptor está activado, aplicar el modo oscuro y guardar el estado en Local Storage
            $('body').addClass('modo-oscuro');
            localStorage.setItem('modo', 'oscuro');
        } else {
            // Si el interruptor está desactivado, aplicar el modo claro y guardar el estado en Local Storage
            $('body').removeClass('modo-oscuro');
            localStorage.setItem('modo', 'claro');
        }
    });
});

// Obtener el elemento HTML donde se mostrará la hora
const horaElemento = document.getElementById('horaLocal');

// Función para obtener la hora desde la API
function obtenerHora() {
  fetch('http://worldtimeapi.org/api/timezone/America/Santiago')
    .then(response => response.json())
    .then(data => {
      // Formatear la hora en formato legible
      const fecha = new Date(data.datetime);
      const hora = fecha.toLocaleTimeString();

      // Mostrar la hora en el elemento HTML
      horaElemento.innerText = hora;
    })
    .catch(error => {
      console.error('Hubo un error al obtener la hora:', error);
    });
}

// Actualizar la hora cada segundo
setInterval(obtenerHora, 1000);


const apiKey = 'My1tu3jTcZbredI0TpqrOY3WU1H3TgR4Qr599TSc';
const url = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;


/* API IMG DE LA NASA */
$(document).ready(function(){
  $.get(url, function(data){
    let html = `<img src="${data.url}" " style="max-width: 20%;">`;
    $('#apod').html(html);
  })
  .fail(function(error){
    console.log(error);
  });
});
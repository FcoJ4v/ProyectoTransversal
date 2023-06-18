function local(){
    /* se declara una array con propiedades */
    let array = [
        {
            rut:"12.123.123-0",
            nombre:"Juan",
            appaterno:"Perez",
            apmaterno:"Rivera",
            genero: "Masculino",
            correo: "micorreo@correo.com",
            telefono: "221212322",
            celular: "999522522",
            contraseña: "asd",
            direccion: "Calle Grande",
            numero: "123",
            region : "Metropolitana",
            ciudad: "Santiago",
            comuna: "Puente Alto"
           
        }
    ];

    /* para pasarlo a local storgage se pasa a json */

    const obj = JSON.stringify(array); /* stringify Sirve para convertir el array a string */
    localStorage.setItem("usuarios",obj);
    console.log("Storage creado");/* se convierte un array en cadena, aca ya estaria creado el local storage */
    /* Se puede acceder a los metodos de esta variable por un punto con el get item. */

}

function mostrarInfo() {
    const objStr = localStorage.getItem("usuarios"); // recuperar la información del Local Storage
    const obj = JSON.parse(objStr); // convertir la cadena JSON en un objeto
    
    // asignar los valores a los inputs correspondientes
    document.getElementById("inputRut").value = obj[0].rut;
    document.getElementById("inputNombre").value = obj[0].nombre;
    document.getElementById("inputAppaterno").value = obj[0].appaterno;
    document.getElementById("inputApmaterno").value = obj[0].apmaterno;
    document.getElementById("inputGenero").value = obj[0].genero;
    document.getElementById("inputCorreo").value = obj[0].correo;
    document.getElementById("inputTelefono").value = obj[0].telefono;
    document.getElementById("inputCelular").value = obj[0].celular;
    document.getElementById("inputPass1").value = obj[0].contraseña;
    document.getElementById("inputDireccion").value = obj[0].direccion;
    document.getElementById("inputNumero").value = obj[0].numero;
    document.getElementById("inputRegion").value = obj[0].region;
    document.getElementById("inputCiudad").value = obj[0].ciudad;
    document.getElementById("inputComuna").value = obj[0].comuna;
  }
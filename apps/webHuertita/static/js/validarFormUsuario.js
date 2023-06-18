
/* Validacion del formulario del usuario con JQUERY */

$(function(){
    $("#formularioUsuario").validate({
        rules:{
            rut:{
                required: true,
                minlength: 8
            },
            nombre:{
                required: true,
                minlength: 3
            },
            appaterno:{
                required: true,
                minlength: 3
            },
            apmaterno:{
                required: true,
                minlength:3
            },
            genero:{
                required: true
            },
            correo:{
                required: true,
                email:true
            },
            telefono:{
                required: true,
                minlength:9,
                maxlength:9
            },
            txtPass1:{
                required: true,
                minlength: 8,
                maxlength: 20
            },
            txtPass2:{
                required: true,
                minlength: 8,
                maxlength: 20
            },
            direccion: {
                required: true
              },
              numero: {
                required: true,
                digits: true
              },
              inputRegion: {
                required: true
              },
              inputCiudad: {
                required: true
              },
              inputComuna: {
                required: true
              }
            
        },
        messages:{
            nombre:{
                required:"Debe ingresar su nombre.",
                minlength:"Minimo 3 caracteres"
            },
            appaterno:{
                required:"Debe ingresar su apellido paterno.",
                minlength:"Minimo 3 caracteres"
            },
            apmaterno:{
                required:"Debe ingresar su apellido materno. ",
                minlength:"Minimo 3 caracteres"
            },
            genero:{
                required:"Debe ingresar su genero."
            },
            rut:{
                required:"Debe ingresar su rut",
                minlength:"Minimo 8 caracteres"
            },
            correo:{
                required:"El correo es obligatorio.",
                email:"Formato correo no valido."
            },
            telefono:{
                required:"Debe ingresar su número de telefono.",
                minlength:"Debe ingresar un número de telefono valido",
                maxlength:"Maximo 9 números"
            },
            txtPass1:{
                required:"Debe ingresar una contraseña.",
                minlength:"Debe tener MINIMO 8 caracteres",
                maxlength:"Debe tener MÁXIMO 20 caracteres."
            },
            txtPass2:{
                required:"Debe ingresar nuevamente su contraseña.",
                minlength:"Debe tener MINIMO 8 caracteres",
                maxlength:"Debe tener MÁXIMO 20 caracteres."
            },
            direccion: {
                required: "Por favor ingrese la dirección"
              },
              numero: {
                required: "Por favor ingrese el número",
                digits: "Por favor ingrese solo dígitos"
              },
              region: {
                required: "Por favor seleccione la región"
              },
              ciudad: {
                required: "Por favor seleccione la ciudad"
              },
              comuna: {
                required: "Por favor seleccione la comuna"
              }
        }
    })
})

/* validacion campos contraseñas */


$(function() {
    $('form').on('submit', function(event) {
      var password1 = $('#inputPass1').val();
      var password2 = $('#inputPass2').val();
  
      if (password1 !== password2) {
        alert('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.');
        event.preventDefault();
      }
  
      if(password1 === "" && password2 === ""){
        alert('Campos de contraseñas vacios.');
        event.preventDefault();
      }
    });
  });
  


  function eventScroll() {
    console.log("Scroll");
}
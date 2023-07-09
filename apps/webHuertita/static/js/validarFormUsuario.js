
/* Validacion del formulario del usuario con JQUERY */

$(function(){
    $("#formularioUsuario").validate({
        rules:{
          txtusername:{
              required: true,
             
            },
          
            rut:{
                required: true,
                minlength: 8
            },
            txtnombre:{
                required: true,
                minlength: 3
            },
            txtappaterno:{
                required: true,
                minlength: 3
            },
            txtapmaterno:{
                required: true,
                minlength:3
            },
            cmbGenero:{
                required: true
            },
            txtcorreo:{
                required: true,
                email:true
            },
            txttelefono:{
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
            txtdireccion: {
                required: true
              },
              txtnumero: {
                required: true,
                digits: true
              },
              txtregion: {
                required: true
              },
              txtciudad: {
                required: true
              },
              txtcomuna: {
                required: true
              }
            
        },
        messages:{
          txtusername:{
                required:"Debe ingresar un nombre de usuario.",
                
            },

            txtnombre:{
                required:"Debe ingresar su nombre.",
                minlength:"Minimo 3 caracteres"
            },
            txtappaterno:{
                required:"Debe ingresar su apellido paterno.",
                minlength:"Minimo 3 caracteres"
            },
            txtapmaterno:{
                required:"Debe ingresar su apellido materno. ",
                minlength:"Minimo 3 caracteres"
            },
            cmbGenero:{
                required:"Debe ingresar su genero."
            },
            txtrut:{
                required:"Debe ingresar su rut",
                minlength:"Minimo 8 caracteres"
            },
            txtcorreo:{
                required:"El correo es obligatorio.",
                email:"Formato correo no valido."
            },
            txttelefono:{
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
              txtdireccion: {
                required: "Por favor ingrese la dirección"
              },
              txtnumero: {
                required: "Por favor ingrese el número",
                digits: "Por favor ingrese solo dígitos"
              },
              txtregion: {
                required: "Por favor ingrese la región"
              },
              txtciudad: {
                required: "Por favor ingrese la ciudad"
              },
              txtcomuna: {
                required: "Por favor ingrese la comuna"
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
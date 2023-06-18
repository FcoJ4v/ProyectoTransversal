 function eventFocus() {
    console.log("FOCUS");
}

function eventScroll() {
    console.log("Scroll");
}

//storage agregar productos

function crear(){
    let array = [
        {
            nombre: document.getElementById("txtProducto").value,
            descripcion: document.getElementById("txtDesc").value,
            valor: document.getElementById("txtValor").value,
            stock: document.getElementById("txtStock").value
        }
    ];

    const obj = JSON.stringify(array);
    localStorage.setItem("txtSku",obj);
    console.log("storage creado!!!");
}

function eliminar(){
    localStorage.removeItem("txtSku");
}

function obtener(){
    let var1 = localStorage.getItem("txtSku");
    const var2 = JSON.parse(var1);

    if (var1 == null){
        alert("no hay datos en el storage")
    }else{
        console.log(var2)
    }

    //console.log(var2);
}


document.getElementById("valProducto").style.display = "none";
document.getElementById("valDesc").style.display = "none";
document.getElementById("valValor").style.display = "none";
document.getElementById("valStock").style.display = "none";
document.getElementById("valSku").style.display = "none";


function validarForm(){
    if (document.getElementById("txtProducto").value.length == 0) {
        document.getElementById("valProducto").style.display = "inline";
        document.getElementById("txtProducto").classList.add("cambioColor");
    }else{
        document.getElementById("valProducto").style.display = "none";
        document.getElementById("txtProducto").classList.remove("is-invalid");
        document.getElementById("txtProducto").classList.add("cambioColor");
    }

    if (document.getElementById("txtDesc").value.length == 0) {
        document.getElementById("valDesc").style.display = "inline";
        document.getElementById("txtDesc").classList.add("cambioColor");
    }else{
        document.getElementById("valDesc").style.display = "none";
        document.getElementById("txtDesc").classList.remove("is-invalid");
        document.getElementById("txtDesc").classList.add("cambioColor");
    }

    if (document.getElementById("txtValor").value.length == 0) {
        document.getElementById("valValor").style.display = "inline";
        document.getElementById("txtValor").classList.add("cambioColor");
    }else{
        document.getElementById("valValor").style.display = "none";
        document.getElementById("txtValor").classList.remove("is-invalid");
        document.getElementById("txtValor").classList.add("is-valid");
    }

    if (document.getElementById("txtStock").value.length == 0) {
        document.getElementById("valStock").style.display = "inline";
        document.getElementById("txtStock").classList.add("is-invalid");
    }else{
        document.getElementById("valStock").style.display = "none";
        document.getElementById("txtStock").classList.remove("is-invalid");
        document.getElementById("txtStock").classList.add("is-valid");
    }

    if (document.getElementById("txtSku").value.length == 0) {
        document.getElementById("valSku").style.display = "inline";
        document.getElementById("txtSku").classList.add("is-invalid");
    }else{
        document.getElementById("valSku").style.display = "none";
        document.getElementById("txtSku").classList.remove("is-invalid");
        document.getElementById("txtSku").classList.add("is-valid");
    }
}

//catalogo


$("#card-body").mouseleave(function(){
    $("#cardText").fadein();
})

document.getElementById("valEmail").style.display = "none";
document.getElementById("valPass").style.display = "none";

function validarForm(){


    if (document.getElementById("txtEmail").value.length == 0 || document.getElementById("txtEmail").value.indexOf("@") == -1) {
        document.getElementById("valEmail").style.display = "inline";
        document.getElementById("txtEmail").classList.add("is-invalid");
    }else{
        document.getElementById("valEmail").style.display = "none";
        document.getElementById("txtEmail").classList.remove("is-invalid");
        document.getElementById("txtEmail").classList.add("is-valid");
    }

    if (document.getElementById("txtPass").value.length == 0) {
        document.getElementById("valPass").style.display = "inline";
        document.getElementById("txtPass").classList.add("is-invalid");
    }else{
        document.getElementById("valPass").style.display = "none";
        document.getElementById("txtPass").classList.remove("is-invalid");
        document.getElementById("txtPass").classList.add("is-valid");
    }

   if (document.getElementById("txtEmail").classList.contains("is-valid") && document.getElementById("txtPass").classList.contains("is-valid")) {
    window.location.href = "Mi_cuenta.html";
    console.log("true");
  }else{
    console.log("fail");
  }
}
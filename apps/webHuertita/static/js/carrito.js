let btnCarrito = document.getElementById("btnCarrito");

btnCarrito.addEventListener('click',function(){
    array_productos = [
        {
            sku:1,
            nombre:"Comida de perro",
            precio:500,
            cantidad:10
        },
        {
            sku:2,
            nombre:"Comida de Gato",
            precio:1000,
            cantidad:20
        },
        {
            sku:3,
            nombre:"Arena de gato",
            precio:1500,
            cantidad:30
        }
    ]
    
    
        let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        fetch('/carrito',{
            
        method:'POST',
        headers:{
            'Content-type': 'application/json',
            'X-CSRFToken':token,
        },
        body:JSON.stringify(array_productos)
        })
        console.log("11111111111111", array_productos); 


})
function guardar() {
    let s = document.getElementById("txtSrc").value
    let g = document.getElementById("txtGenero").value
    let a = document.getElementById("txtAutor").value
    let producto = {
        src: s,
        genero: g,
        autor: a
    }
    let url = "https://galeria-de-arte.herokuapp.com/productos"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar")
            console.error(err);
        })
}
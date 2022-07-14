var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = decodeURI(parts[0][1])
document.getElementById("txtSrc").value = decodeURI(parts[1][1])
document.getElementById("txtGenero").value = decodeURI(parts[2][1])
document.getElementById("txtAutor").value = decodeURI(parts[3][1])
function modificar() {
    let id = document.getElementById("txtId").value
    let s = document.getElementById("txtSrc").value
    let g = document.getElementById("txtGenero").value
    let a = document.getElementById("txtAutor").value
    let producto = {
        src: s,
        genero: g,
        autor: a
    }
    let url = "http://localhost:5000/productos/" + id
    var options = {
        body: JSON.stringify(producto),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })
}
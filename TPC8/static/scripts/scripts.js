
function apagar_conceito(designacao){ //form nao deixa fazer delete por isso que precissamos do javascript
    $.ajax("/conceitos/" + designacao, {
        method: "DELETE",
        success: function(response){
            window.location.href="/conceitos"
        },
        error: function(response){
            console.log(response)
        }
    })
}//jquery´

new DataTable('#tabela_conceitos'); // # esta a procurar de um id 
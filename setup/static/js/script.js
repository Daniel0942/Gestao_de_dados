let editar = document.getElementsByClassName("editar")[0]

// função pra mandar id para a rota e redirecionar para a página de edit
editar.addEventListener("click", function(e) {
    let username_id = this.getAttribute("user-id") // getAttribute busca o atributo

    document.location.href = `/dados/${username_id}`
})

// Função pra mandar o id para a rota e redirecionar para a página de edit
let deletar = document.getElementsByClassName("deletar")[0]

deletar.addEventListener("click", function() {
    let username_id = this.getAttribute("user-id")

    document.location.href = `/dados/deletar/${username_id}`
})
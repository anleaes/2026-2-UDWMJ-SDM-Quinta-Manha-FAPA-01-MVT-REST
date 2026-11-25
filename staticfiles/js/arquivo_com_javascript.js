// Marca no menu o link da página atual.
// Ex.: em /animais/adicionar/ o link "Animais" (/animais/listar/) fica destacado.
function marcarMenuAtivo() {
    const pastaAtual = window.location.pathname.split('/')[1];
    const links = document.querySelectorAll('.menu a');

    links.forEach(function (link) {
        const pastaDoLink = link.getAttribute('href').split('/')[1];
        if (pastaAtual !== '' && pastaDoLink === pastaAtual) {
            link.classList.add('ativo');
        }
    });
}

// Pede confirmação antes de excluir, porque a exclusão é imediata.
function confirmarExclusao() {
    const links = document.querySelectorAll('a[href*="/excluir/"]');

    links.forEach(function (link) {
        link.addEventListener('click', function (evento) {
            if (!confirm('Tem certeza que deseja excluir este registro?')) {
                evento.preventDefault();
            }
        });
    });
}

marcarMenuAtivo();
confirmarExclusao();

// Adicione um evento de clique aos itens da barra lateral
document.querySelectorAll('.sidebar li').forEach(item => {
    item.addEventListener('click', () => {
        // Realize a ação desejada para cada item da barra lateral aqui
        alert(`Você clicou em: ${item.textContent}`);
    });
});

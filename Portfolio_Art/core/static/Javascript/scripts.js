function search() {
    var input = document.getElementById("search-input");
    var filter = input.value.toUpperCase();

    window.location.href = base_url.replace('__filter__', encodeURIComponent(filter));
}

function handleKeyPress(event) {
    // Verifica si la tecla presionada es 'Enter'
    if (event.key === 'Enter') {
        // Llama a la función 'search' cuando se presiona 'Enter'
        search();
    }
}

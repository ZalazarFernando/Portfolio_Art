function search() {
    var input = document.getElementById("search-input");
    var filter = input.value.toUpperCase();

    window.location.href = base_url.replace('__filter__', encodeURIComponent(filter));
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        search();
    }
}
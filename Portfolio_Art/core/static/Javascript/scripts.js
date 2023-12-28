// En scripts.js
function search() {
    var input = document.getElementById("search-input");
    var filtro = input.value.toUpperCase();
    var cards = document.getElementById("all-cards").getElementsByClassName("cards");

    for (var i = 0; i < cards.length; i++) {
        var titulo = cards[i].getElementsByTagName("h2")[0].textContent.toUpperCase();
        var hashtag = cards[i].getElementsByClassName("cards-hashtag")[0].textContent.toUpperCase();

        if (titulo.includes(filtro) || hashtag.includes(filtro)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

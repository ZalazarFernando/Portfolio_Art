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

document.addEventListener('DOMContentLoaded', function () {
    var cards = document.querySelectorAll('.card-item');
    var contextMenu = document.getElementById('context-menu');

    cards.forEach(function (card) {
        card.addEventListener('contextmenu', function (event) {
            event.preventDefault();
            var postId = card.getAttribute('data-post-id');
            showContextMenu(event.clientX, event.clientY, postId);
        });
    });

    function showContextMenu(x, y, postId) {
        contextMenu.style.display = 'block';
        contextMenu.style.left = x + 'px';
        contextMenu.style.top = y + 'px';

        // Almacena el id en un atributo de datos
        selectedPostId = postId;
        contextMenu.setAttribute('data-post-id', postId);

        // Agrega eventos
        var btnEdit = document.getElementById('btn-edit');
        var btnDelete = document.getElementById('btn-delete');
        var btnAddToBoard = document.getElementById('btn-add-to-board');

        btnEdit.addEventListener('click', function () {
            handleMenuAction('edit', postId);
        });

        btnDelete.addEventListener('click', function () {
            handleMenuAction('delete', postId);
        });

        btnAddToBoard.addEventListener('click', function () {
            handleMenuAction('add', postId);
        });

        document.addEventListener('click', hideContextMenu);
    }

    function hideContextMenu() {
        contextMenu.style.display = 'none';
        document.removeEventListener('click', hideContextMenu);

        // Elimina los eventos al ocultar el menú
        var btnEdit = document.getElementById('btn-edit');
        var btnDelete = document.getElementById('btn-delete');
        var btnAddToBoard = document.getElementById('btn-add-to-board');

        btnEdit.removeEventListener('click', handleMenuAction);
        btnDelete.removeEventListener('click', handleMenuAction);
        btnAddToBoard.removeEventListener('click', handleMenuAction);
    }

    function handleMenuAction(action, postId) {
        if(postId) {
            if(action==='edit'){
                var editUrl = `/edit_post/${postId}/`;
                window.location.href = editUrl;
            } else if (action==='delete') {
                //obtener csrfToken
                var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                $.ajax({
                    type: "POST",
                    url: `/delete_post/`,
                    data: {
                        'post_id': postId,
                    },
                    headers: {
                        'X-CSRFToken': csrfToken
                    },
                    success: function(response){
                        if (response === 'success') {
                            console.log('Post delete successfully');
                            location.href = "";  
                        } else {
                            console.log('Error delete post');
                        }
                    },
                    error: function(error) {
                        console.log('Error delete post:', error);
                    }
                })
            } 
        }
    }
});

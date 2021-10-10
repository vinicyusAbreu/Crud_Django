$(document).ready(function() {

    if ($('.todo-list__container ul li').length) {

        $('.fa-edit').on('click', function() {
            const elemento = $(this.parentNode);

            const id = $(this.parentNode).attr('data-id');

            $.ajax({
                url: `http://127.0.0.1:8000/pegarValores/${id}`,
                type: "GET",
                dataType: "json",
                success: (data) => {
                    $('.editContainer').each(function() {
                        $(this).removeAttr("style");
                    });

                    elemento.find('.editInput').val(data.crud[0].nome);
                    elemento.find('.editContainer').css('display', 'flex');
                },
                error: (error) => {
                    console.log(error);
                }
            });

        });

        $('.cancelButton').on('click', function(e) {
            e.defaultPrevented;
            $(this.parentNode).removeAttr("style");
        });

    }

});
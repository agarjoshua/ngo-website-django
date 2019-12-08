var container = $("div.card h-300");

$('input#get').click(function() {
    $.ajax({
        url: '/media',
        datatype: 'json',
        type: 'GET',
        success: function(data) {
            $.each(data.events, function(index, element) {
                $('body').append($('<div>', {
                    text: element.name
                }));
            });
        }
    });

});



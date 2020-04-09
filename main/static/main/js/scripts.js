$( document ).ready(function() {
    setInterval(CheckUrls, 4000)

    function CheckUrls() {   
            $.ajax({
                type: "GET",
                url: 'ajax/check/',
                data: {},
                success: function(response) {
                    $('body').load("http://127.0.0.1:8000/");
                }
            });
        }
});




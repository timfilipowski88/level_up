$(document).ready(function () {
    $('#register_btn').click(function (event) {
        event.preventDefault();
        
        var form_id = $('#reg_form');

        $.ajax({
            url: '{% url 'login:register' %}',
            type: 'POST',
            data: form_id.serialize(),
            dataType: 'json',
            header: {'X-CSRFToken': '{% csrf_token %}'},
            success: function (response) {
                var success = response['success']
                if (success) {
                    alert('Form Valid, User Created, We will redirect')
                } else {
                    alert('Got Form errors')
                }
            },
            failure: function (){
                alert('Error occured while calling our Django View')
            }
        })
    });
});

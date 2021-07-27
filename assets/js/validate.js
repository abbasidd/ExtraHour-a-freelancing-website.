$('document').ready(function(){
    $('#username','#signup').keyup(function(){

      console.log('sasgfga');
      var username = $('#username','#signup').val();
      if (username == '') {
        return;
      }
      $.ajax({
        url: 'http://127.0.0.1:8000/accounts/check_username_exist' ,
        type: 'post',
        data: {
          
          'username' : username,
        },
        success: function(response){
          if (response.r == 'taken' ) {
 
            console.log('error');
            $('#username').parent().removeClass();
            $('#username').parent().addClass("invalid");
            $('#username').siblings("span").text('Sorry... Username already taken');
          }else  {
        
            console.log('sasgfga');
            $('#username').parent().removeClass();
            $('#username').parent().addClass("valid");
            $('#username').siblings("span").text('Username available');
          }
        }
      });

    });});
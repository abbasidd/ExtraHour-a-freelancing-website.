$('document').ready(function(){












    $('#next').click(function() {
        var user_answer=$('input[name = "answer"]:checked' , '#quiz').val();
    var question_id=  $('#question_id','#quiz').val();
    var q_no=  $('#q_no','#quiz').val();
        $.ajax({
            url: 'http://127.0.0.1:8000/skill_test/user_ans',
            type: 'post',
          
            data : {
                'user_answer':  user_answer,
                'question_id':question_id,
                'q_no':q_no,
        
            } ,// This is the default though, you don't actually need to always mention it
            success: function(response) {
                alert(response.question)
                if(response.count == response.id)
                {
                    window.location.replace('http://127.0.0.1:8000/skill_test/result/'+response.quiz_taker_id+'/')

                }
                $('#question_id').val(response.id);
                $('#q_no').val(response.q_no);
                
                $('#q_label').text(response.question);
                $('#choice1').text(response.choice1);
                $('#choice2').text(response.choice2);
                $('#choice3').text(response.choice3);
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
        });

    });


    
    




















});



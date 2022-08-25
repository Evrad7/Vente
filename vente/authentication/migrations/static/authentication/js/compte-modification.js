$(document).ready(function(){
  $("form input").on("keyup", function(){
    modificationCompteAjax()
  })

})


var modificationCompteAjax=function(){
  var data=new FormData(document.getElementById("form"))
   var request=$.ajax({
    url:"/auth/compte/modification/",
    method:"POST",
    processData:false,
    contentType:false,
    cache:false,
    asynch:true,
    data:data,
    beforeSend:function(){
  
    }
  })
  request.done(function(response){
    if(request.error){
      $(".error").html("<h5 class='text-danger fw-bold'> Erreur</h5>")
    }
    else{
      $(".error-username").html("")
      $(".error-email").html("")

        $(".error").html("")
        if(response.errors){
          if(response.errors.username){
            $(".error-username").html(response.errors.username)
          }
          if(response.errors.email){
            $(".error-email").html(response.errors.email)
          }

        }

    }

  })

  request.fail(function(response){
    $(".error").html("<h5 class='text-danger fw-bold'> Erreur</h5>")

  })
}

$(document).ready(function(){
  $(".search-navbar").each(function(){
    $(this).on("keyup", function(){
      searchAjax($(this))
    })
  })
})

var searchAjax=function(item){
  var request=$.ajax({
    url:"/achat/search_ajax?q="+item.val(),
    method:"GET",
    asynch:true,
    cache:false,
    processData:false,
    contentType:false,
    beforeSend:function(){
      console.log("REQUEST SEND")
    }
  })

  request.done(function(response){
    if(response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response.propositions)
      var propositions=item.next().next().next()
      if(response.propositions.length==0){
        propositions.removeClass("proposition-search-active")
      }
      else{
        propositions.addClass("proposition-search-active")
        response.propositions.forEach(function(item, i) {
          if(i!=0){
            propositions.html(propositions.html()+"<div class=item>"+item[0]+"</div>")
          }
          else{
            propositions.html("<div class=item>"+item[0]+"</div>")
          }
        });
        selectProposition()
      }

      }
    })

    request.fail(function(response){
      console.log("FAIL")
    })

    }


var selectProposition=function(){
  $(".proposition-search div").each(function(){
    console.log($(this))
    $(this).on("click", function(){
      console.log($(this).parent().parent().children().first())
      $(this).parent().parent().children().first().val($(this).html())
      console.log($(this).parent().parent().parent())
      $(this).parent().parent().parent().submit()
    })
  })
}

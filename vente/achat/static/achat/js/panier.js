
var panier={}
prixTotal=0
$(document).ready(function(){
  $("div.quantite input").each(function(item, i){
    $(this).on("change", function(){
      var prix=parseFloat($(this).attr("prix").replace(",", "."))
      if(panier[$(this).attr("reference")]!=undefined){
        prixTotal-=parseInt(panier[$(this).attr("reference")])*prix
        console.log(prixTotal)
        prixTotal+=$(this).val()*prix
        console.log(prixTotal)
        $("div.prix-total div:last span").html(floatformat(prixTotal)+" XAF")
        panier[$(this).attr("reference")]=$(this).val()
      }

      var prixTotalTypeArticle=parseInt($(this).val())*prix
      $(this).parent().next().children().last().children().html(floatformat(prixTotalTypeArticle)+" XAF")

    })
  })
  var selectionPanier=$(".action-panier a:nth-child(1)")
  selectionPanier.each(function(item, i){
     $(this).on("click", function(e){
      e.preventDefault()
      console.log($(this))
      input=$(this).parent().prev().children(".quantite").children().last()
      var prix=parseFloat(input.attr("prix").replace(",", "."))
      if(panier[input.attr("reference")]==undefined){
        panier[input.attr("reference")]=input.val()
        prixTotal+=input.val()*prix
        $("div.prix-total div:last span").html(floatformat(prixTotal)+" XAF")
        $(this).parent().prev().addClass("active")
      }
      else{
        prixTotal-=parseInt(panier[input.attr("reference")])*prix
        $("div.prix-total div:last span").html(floatformat(prixTotal)+" XAF")
        delete panier[input.attr("reference")]
        $(this).parent().prev().toggleClass("active")
      }



   })
 })
  var supprimerPanier=$(".action-panier a:nth-child(2)")
  supprimerPanier.each(function(item, i){
    $(this).on("click", function(e){
      e.preventDefault()
      supprimerArticlePanierAjax($(this).attr("pk"))

    })
  })
  $("div.commander a").on("click", function(e){
    e.preventDefault()

    commandeAjax()
  })


})


var commandeAjax=function(){
  const csrftoken = getCookie('csrftoken')
  var request=$.ajax({
    url:$(location).attr("pathname")+"commander_ajax/",
    method:"POST",
    data:panier,
    headers:{"X-CSRFToken":csrftoken},
    asynch:true,
    cache:false,
     beforeSend:function(){
       console.log("send")
     }
    })

    request.done(function(response){
      if(response.error){
        console.log("ERROR")
      }
      else{
        console.log("SUCCESS")
        $(location).attr("pathname", "/achat/commande")
      }
    })

    request.fail(function(response){
      console.log("FAIL")
    })

}
var supprimerArticlePanierAjax=function(pk){
  var request=$.ajax({
    url:"/achat/panier/supprimer_article_panier_ajax?pk="+pk,
    method:"GET",
    asynch:true,
    cache:false,
    contentType:false,
    processData:false,
    beforsend:function(){
      console.log("SEND")
    }
  })

  request.done(function(response){
    if (response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response.count)
      $("div.panier-content#"+pk).remove()
      if(response.count===0){
        $("div.main").html("<div class='alert alert-info text-center my-3 mt-4'>\
           Votre panier est vide.\
         </div>")
         $("div.prix-total").remove()
      }

    }
  })

  request.fail(function(response){
    console.log("FAIL")
  })
}

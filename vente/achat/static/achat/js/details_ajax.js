$(document).ready(function(){
  prepareAjaxSelectionCouleur()
  ajaxChangementDeTaille()
  $("#ajout-panier").on("click", function(e){
    e.preventDefault()
    ajaxAjoutPanier()
  })

})




prepareAjaxSelectionCouleur=function(){
  $(".dropdown  li .dropdown-item").each(function(){
   $(this).on("click", function(){
     var request=$.ajax({
       url:$(location).attr("pathname")+"ajax/?q="+$(this).text(),
       beforeSend:function(){
        $("#load-ajax").removeClass("opacity-0")
       },
     })

     request.done(function(response){
       $("#load-ajax").addClass("opacity-0")
       if(response.error){
         console.log("ERROR")
       }
       else{
        var ulTailles=$("ul.tailles")
        ulTailles.html("")
        $.each(response.types_articles, function(i, object){
          if(object.quantite_disponible==0){
            object.quantite_disponible="0 restant: <a href=# class='link-dark '><br/>me prevenir quand disponible</a>"
          }
          else{
            object.quantite_disponible=object.quantite_disponible+" restant"
          }
          ulTailles.append("\
          <div class='position-relative'>\
          <li class='me-2 border rounded border-info  px-1' pk_photos='"+object.photos+"'>"+object.taille+"</li>\
              <div class='' >\
             <span class='text-dark px-3'>"+object.quantite_disponible +"</span>\
                </div>\
           </div>")

          if(i==0){// Ici nous chargeons les photos de la première taille active
            ulTailles.children().first().children().first().addClass("active")
            var old_pk_photos=$("div.carousel-inner").attr("pk_photos")
            ajaxChargementDePhotos(old_pk_photos, object.photos)

          }
        })
        ajaxChangementDeTaille()

       }

   })
   request.fail(function(response){
      $("#load-ajax").addClass("opacity-0")
     console.log("ERROR")

   })
  })

})
}


ajaxChargementDePhotos=function(old_pk_photos, new_pk_photos){
   if(old_pk_photos!=new_pk_photos){
     var request1=$.ajax({
       url:"/achat/details/charger_images/?q="+new_pk_photos,
    		type:"GET",
    		processData:false,
    		contentType:false,
    		cache:false,
    		asynch:true,
        beforeSend:function(){
            $("#load-ajax").removeClass("opacity-0")
        }

     })

     request1.done(function(response){
        $("#load-ajax").addClass("opacity-0")
       if(response.error){
         console.log("ERROR")
       }
       else{
         $("div.carousel-inner").attr("pk_photos", response.pk)
         $("div.carousel-inner").html("\
         <div class='carousel-item active ' >\
           <img src='"+response.photo1+"' class='img-fluid d-block  m-auto' alt='{{article.nom}}'>\
         </div>\
         <div class='carousel-item  ' >\
           <img src='"+response.photo2+"' class='img-fluid d-block  m-auto' alt='{{article.nom}}'>\
         </div>'")
         if(response.photo3){
            $("div.carousel-inner").html()+"<div class='carousel-item  ' >\
              <img src='"+response.photo2+"' class='img-fluid d-block  m-auto' alt='{{article.nom}}'>\
            </div>"
         }




       }
     })

     request1.fail(function(response){
       console.log("request failed")
       $("#load-ajax").addClass("opacity-0")
     })
   }
}

var ajaxChangementDeTaille=function(){
  var lis=$("ul.tailles li")
    lis.each(function(){
    $(this).on("click", function(){
      ajaxChargementDePhotos($("div.carousel-inner").attr("pk_photos"), $(this).attr("pk_photos"))
      lis.removeClass("active")
      $(this).toggleClass("active")

    })
  })
}


var ajaxAjoutPanier=function(){
  var couleur=$("#dropdownMenu2").children().first().text()
  var taille=$("ul.tailles li.active").text().trim()
  console.log(couleur)
  console.log(taille)

   var  request=$.ajax({
        url:$(location).attr("pathname")+"ajout_panier?c="+couleur+"&t="+taille,
       type:"GET",
       processData:false,
       contentType:false,
       cache:false,
       asynch:true,
       beforSend:function(){
         console.log("requete envoyée")
       },

  })

  request.done(function(response){
    if(response.error){
      console.log("Error")
      document.location.replace("/auth/connexion/?next="+document.location.pathname)
    }
    else{
      console.log("success")
      if(response.exists)
         var message="L'article est déja dans le panier"
      else
        var message="Article ajouté au panier avec success"
      $(".block-info").html("\
      <div class='alert alert-success alert-dismissible fade show' role='alert'>\
        "+message+"\
        <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
      </div>\
      ")
    }
  })

  request.fail(function(response){
    console.log("Error fail");
  })
}

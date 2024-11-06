$(document).ready(function(){
  ajaxDestinationPaysCommande($(".destination div select[name='pays']"))
  $(".destination div select").each(function(item, i){

    $(this).on("change", function(){
      if($(this).attr("name")==="pays"){
        ajaxDestinationPaysCommande($(this))
      }
      if($(this).attr("name")==="region"){
        ajaxDestinationRegionCommande($(this))
      }
      if($(this).attr("name")==="ville"){
        ajaxDestinationVilleCommande($(this))
      }
      if($(this).attr("name")==="quartier"){
        ajaxDestinationQuartierCommande($(this))
      }

    })
  })
})

var ajaxDestinationPaysCommande=function(elt){


  csrftoken=getCookie("csrftoken")
  var request=$.ajax({
    url:$(location).attr("pathname")+"destination_pays_ajax/",
    method:"POST",
    data:{"pays":elt.val()},
    headers:{"X-CSRFToken":csrftoken},
    asynch:true,
    cache:false,
    beforsend:function(){
      console.log("SEND")
    }

  })
  request.done(function(response){
    if(response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response)
        $(".destination select[name='region']").html("")
        if(response.response.regions){
          response.response.regions.forEach(function(item, i){
            $(".destination select[name='region']").html($(".destination select[name='region']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }
        $(".destination select[name='ville']").html("")
        if(response.response.villes){
          response.response.villes.forEach(function(item, i){
            $(".destination select[name='ville']").html($(".destination select[name='ville']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }
        $(".destination select[name='quartier']").html("")
        if(response.response.quartiers){
          response.response.quartiers.forEach(function(item, i){
            $(".destination select[name='quartier']").html($(".destination select[name='quartier']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }

        $(".destination select[name='adresse']").html("")
        if(response.response.adresses){
           response.response.adresses.forEach(function(item, i){
            $(".destination select[name='adresse']").html($(".destination select[name='adresse']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }


    }
  })

  request.fail(function(response){
    console.log("FAIL")
  }

  )
}

var ajaxDestinationRegionCommande=function(elt){


  csrftoken=getCookie("csrftoken")
  var request=$.ajax({
    url:$(location).attr("pathname")+"destination_region_ajax/",
    method:"POST",
    data:{"region":elt.val()},
    headers:{"X-CSRFToken":csrftoken},
    asynch:true,
    cache:false,
    beforsend:function(){
      console.log("SEND")
    }

  })
  request.done(function(response){
    if(response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response)
        $(".destination select[name='ville']").html("")
        if(response.response.villes){
          response.response.villes.forEach(function(item, i){
            $(".destination select[name='ville']").html($(".destination select[name='ville']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }
        $(".destination select[name='quartier']").html("")
        if(response.response.quartiers){
          response.response.quartiers.forEach(function(item, i){
            $(".destination select[name='quartier']").html($(".destination select[name='quartier']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }

        $(".destination select[name='adresse']").html("")
        if(response.response.adresses){
           response.response.adresses.forEach(function(item, i){
            $(".destination select[name='adresse']").html($(".destination select[name='adresse']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }


    }
  })

  request.fail(function(response){
    console.log("FAIL")
  }

  )
}


var ajaxDestinationVilleCommande=function(elt){


  csrftoken=getCookie("csrftoken")
  var request=$.ajax({
    url:$(location).attr("pathname")+"destination_ville_ajax/",
    method:"POST",
    data:{"ville":elt.val()},
    headers:{"X-CSRFToken":csrftoken},
    asynch:true,
    cache:false,
    beforsend:function(){
      console.log("SEND")
    }

  })
  request.done(function(response){
    if(response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response)

        $(".destination select[name='quartier']").html("")
        if(response.response.quartiers){
          response.response.quartiers.forEach(function(item, i){
            $(".destination select[name='quartier']").html($(".destination select[name='quartier']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }

        $(".destination select[name='adresse']").html("")
        if(response.response.adresses){
           response.response.adresses.forEach(function(item, i){
            $(".destination select[name='adresse']").html($(".destination select[name='adresse']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }


    }
  })

  request.fail(function(response){
    console.log("FAIL")
  }

  )
}


var ajaxDestinationQuartierCommande=function(elt){


  csrftoken=getCookie("csrftoken")
  var request=$.ajax({
    url:$(location).attr("pathname")+"destination_quartier_ajax/",
    method:"POST",
    data:{"quartier":elt.val()},
    headers:{"X-CSRFToken":csrftoken},
    asynch:true,
    cache:false,
    beforsend:function(){
      console.log("SEND")
    }

  })
  request.done(function(response){
    if(response.error){
      console.log("ERROR")
    }
    else{
      console.log("SUCCESS")
      console.log(response)

        $(".destination select[name='adresse']").html("")
        if(response.response.adresses){
           response.response.adresses.forEach(function(item, i){
            $(".destination select[name='adresse']").html($(".destination select[name='adresse']").html()+"\
            <option value='"+item[0]+"'>"+item[1]+"</option>")
          })
        }


    }
  })

  request.fail(function(response){
    console.log("FAIL")
  }

  )
}

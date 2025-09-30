var mediaRoot="/media/"
$(document).ready(function(){
  $(".cathegories .item").on("click", function(){
    console.log($(this).attr("pk"))
    filtreCathegoriesAjax($(this))
  })
})

var filtreCathegoriesAjax=function(item){
  var request=$.ajax({
  url:"/articles/ajax/?q="+item.attr("pk"),
  method:"GET",
  processData:false,
  contentType:false,
  cache:false,
  asynch:true,
  beforeSend: function(){
    console.log("before send")
    $(".articles").html("")
    for(_ of [1, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12]){
      $(".articles").html($(".articles").html()+"\
    <div class='col-6 col-sm-4 col-md-3 col-lg-2  mb-2  '>\
      <div class='m-auto card load-card border border-warning postition-relative '>\
        <div class='load-reduction border load'>\
        </div>\
          <div class='load-card-img'>\
          </div>\
          <div class='p-1'>\
            <h2 class='load-card-tiltle m-auto mb-1 load'></h2>\
            <div class='load-card-prix m-auto load'>\
            </div>\
            <div class='load-card-ancien-prix mx-auto mt-1 load'>\
            </div>\
          </div>\
        </div>\
      </div>")

    }

  }
})

request.done(function(response){
  if(response.error)
    console.log("ERROR")
    else{
      $(".articles").html("")
      if(response.articles.length==0){
        $(".articles").html("<p class='alert alert-warning my-2'>\
          Aucun article appartenant actuellement à cette Cathégories\
        </p>")
      }
      $.each(response.articles, function(i, object){
        console.log(object)
        $(".articles").html($(".articles").html()+"\
        <div class='col-6 col-sm-4 col-md-3 col-lg-2  mb-2  '>\
           <div class='card position-relative p-0 border border-warning shadow'>\
             <div class='content-img'>\
               <img src='"+mediaRoot+object.photo+"' alt='"+object.nom+"' class='card-img-top' width='154px' height='154px'>\
               </div>\
                 <div class='px-1 pb-0 card-body'>\
               <p class=' card-title p-0 m-0  text-center'>"+object.nom+"</p>\
                <div class='  mx-auto btn-price d-flex justify-content-center align-items-center bg-warning py-0  rounded-2 ' style='height:30px;'>\
                     <span class=''>"+floatformat(object.prix)+" XAF</span>\
                </div>\
                <div class=' d-flex justify-content-center'>\
                  <span style='' class='text-dark fw-bold rounded reduction'>-"+object.reduction+"%</span>\
                  <span class='text-muted   text-decoration-line-through'>"+floatformat(object.prix_non_reduit)+" XAF</span>\
                </div>\
                 <a href='/details/"+object.pk+"/' class='stretched-link'></a>\
             </div>\
           </div>\
         </div>")

      })
    }


})
}

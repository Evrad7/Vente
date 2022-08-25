document.addEventListener("DOMContentLoaded", function(){
  var cathegories=$(".cathegories div ");
  cathegories.each(function(){
    $(this).on("click", function(e) {
      $(".cathegorie-active").text($(this).text())
      filtreCathegoriesAjax($(this))//Function defined in file articles_ajax.js
    })
  });

})

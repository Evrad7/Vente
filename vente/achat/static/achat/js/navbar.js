document.addEventListener("DOMContentLoaded", function(){
  var inputSearchVisible=false
  var items=document.querySelectorAll(" nav ul li a")
  items.forEach((item, i) => {
    item.addEventListener("click", function(){
      items.forEach(elt=>{
        elt.classList.remove("active")
      })
      item.classList.add("active")
    })
  })

  document.querySelector("#button-nav").addEventListener("click", function(){

    console.log(document.querySelector("nav ul"))
    document.querySelector("nav ul").classList.toggle("desabled")
  })

  var inputSearch=document.querySelector(".search input")
  var btnSearchClose=document.querySelector(".search .btn-search i")



  if(inputSearch.value.length>0)
   btnSearchClose.classList.remove("invisible")
   else{
      btnSearchClose.classList.add("invisible")
   }



  btnSearchClose.addEventListener("click", function(){
    inputSearch.value="";
    btnSearchClose.classList.add("invisible")
    document.querySelectorAll(".proposition-search").forEach(function(item, i) {
      item.classList.remove("proposition-search-active")
    });

  })
  inputSearch.addEventListener("keyup", function(){

   if(this.value.length>0)
    btnSearchClose.classList.remove("invisible")
    else{
       btnSearchClose.classList.add("invisible")
    }
  })


  // SM

  var inputSearchSm=document.querySelector(".search-sm input")
  var btnSearchCloseSm=document.querySelector(".search-sm .btn-search i")



  if(inputSearchSm.value.length>0)
   btnSearchCloseSm.classList.remove("invisible")
   else{
      btnSearchCloseSm.classList.add("invisible")
   }



  btnSearchCloseSm.addEventListener("click", function(){
    inputSearchSm.value="";
    btnSearchCloseSm.classList.add("invisible")
  })
  inputSearchSm.addEventListener("keyup", function(){

   if(this.value.length>0)
    btnSearchCloseSm.classList.remove("invisible")
    else{
       btnSearchCloseSm.classList.add("invisible")
    }
  })

document.querySelectorAll(".search input, .search-sm input").forEach((item, i) => {
  item.type="text"
});



})

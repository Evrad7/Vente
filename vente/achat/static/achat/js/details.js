document.addEventListener("DOMContentLoaded", function(){
  chevron=document.querySelector(".dropdown button.dropdown-toggle")
  chevron.addEventListener("click", function(){
    this.firstChild.nextElementSibling.classList.toggle("active")
  })

  dropdownItems=document.querySelectorAll(".dropdown  li .dropdown-item")
  dropdownItems.forEach(item => {
      item.addEventListener("click", function(){
        chevron.firstChild.nextElementSibling.classList.toggle("active")
      document.querySelector("#dropdownMenu2").firstChild.nextElementSibling.innerHTML=this.innerHTML



    })
  });


})

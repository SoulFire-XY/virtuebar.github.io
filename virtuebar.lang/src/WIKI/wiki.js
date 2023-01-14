let closeBtn = document.querySelector('.CloseBtn');
let SearchBtn = document.querySelector('.SearchBtn');
let searchBox = document.querySelector('.searchBox');
console.log(closeBtn + SearchBtn + searchBox)

SearchBtn.onclick =  function() {
  searchBox.classList.add('active');
  closeBtn.classList.add('active');
  SearchBtn.classList.add('active');
}
closeBtn.onclick =  function() {
  searchBox.classList.remove('active');
  closeBtn.classList.remove('active');
  SearchBtn.classList.remove('active');
}
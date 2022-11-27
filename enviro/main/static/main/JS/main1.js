//const send = document.getElementById("send");
const successfully = document.getElementById("successfully");
const close = document.getElementById("close");
const closeSuccessfully = document.getElementById("close-successfully");
const sendNext = document.getElementById("send-next");

//send.addEventListener("click", (e) => {
//  e.preventDefault();
//  if (isTrue1 && isTrue2 && isTrue3) {
//    successfully.classList.remove("none");
//  }
//});

closeSuccessfully.addEventListener("click", (e) => {
  e.preventDefault();
  successfully.classList.add("none");

});


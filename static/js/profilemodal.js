const profile= document.getElementById("profile");
// const modal=document.querySelector(".modal");
// const modalBackground=document.querySelector(".modal__background");

function displayModal(){
    // modal.classList.toggle("hidden");
    var option = "width=900, height=200, top=200,left=300 location = no";
    window.open("profilemodal",'프로필',option);
    console.log('gg');
}

profile.addEventListener("click",displayModal);
// modalBackground.addEventListener("click",displayModal);
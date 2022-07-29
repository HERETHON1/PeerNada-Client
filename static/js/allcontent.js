const Btn = document.getElementById("postbtn");
const ContentDetail=document.getElementById("about");
function handleContent() {
  window.location.href = "content.html";
}
function AboutDetail(){
  window.location.href = "detail.html";
  console.log("gg");
}
Btn.addEventListener("click", handleContent);
ContentDetail.addEventListener("click",AboutDetail);

const myComment = document.getElementById("mycomment");
const Btn = document.getElementById("addcomment");

function handleComment(event) {
  event.preventDefault();
  const comment = myComment.value;
  console.log(comment);
}

Btn.addEventListener("submit", handleComment);

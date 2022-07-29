const Content = document.getElementById("contentabout");
const Title = document.getElementById("contenttitle");
const Url = document.getElementById("contenturl");
const Detail = document.getElementById("contentdetail");

function handleContent(event) {
  event.preventDefault();
  const title = Title.value;
  const url = Url.value;
  const detail = Detail.value;
  console.log(title);
  console.log(url);
  console.log(detail);
  toastr.success("게시 완료되었습니다");
  window.location.href = "home";
}

Content.addEventListener("submit", handleContent);

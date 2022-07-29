
const profiles=document.querySelectorAll('span');

profiles.forEach(p=>{
    p.addEventListener('click',function handleProfile(event){
        var option = "width=900, height=200, top=200,left=300 location = no";
        window.open("profilemodal",'프로필',option);
    })
})

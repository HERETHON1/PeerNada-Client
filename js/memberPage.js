document.querySelector('.saveBtn').onclick = () => {
	console.log('saveBtn 클릭');
	document.querySelector('.signupForm').style.display = 'none';
	document.querySelector('.success').style.display = 'block';
};

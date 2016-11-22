function alturaMenu(){
	var altura = document.body.offsetHeight;
	elemento = document.getElementById('hmenu');
	elemento.style.height = altura+"px";
		
}
window.onload = function(){
	alturaMenu();
}
window.onresize = function(){
	alturaMenu();
}
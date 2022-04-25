document.getElementById("btn_led1").addEventListener('change', ()=>{
    let status = document.getElementById('btn_led1').checked;
    if(status){
	document.getElementById('title1').innerText = "Encendido";
	changeForeground('green', 'title1');
	eel.process(13, 1);
    }else{
	document.getElementById('title1').innerText = "Apagado";
	changeForeground('red', 'title1');
	eel.process(13, 0);
    }
});


document.getElementById("btn_led2").addEventListener('change', ()=>{
    let status = document.getElementById('btn_led2').checked;
    if(status){
	document.getElementById('title2').innerText = "Encendido";
	changeForeground('green', 'title2');
	eel.process(12, 1);
    }else{
	document.getElementById('title2').innerText = "Apagado";
	changeForeground('red', 'title2');
	eel.process(12, 0);
    }
});


document.getElementById("btn_led3").addEventListener('change', ()=>{
    let status = document.getElementById('btn_led3').checked;
    if(status){
	document.getElementById('title3').innerText = "Encendido";
	changeForeground('green', 'title3');
	eel.process(11, 1);
    }else{
	document.getElementById('title3').innerText = "Apagado";
	changeForeground('red', 'title3');
	eel.process(11, 0);
    }
});

document.getElementById("btn_led4").addEventListener('change', ()=>{
    let status = document.getElementById('btn_led4').checked;
    if(status){
	document.getElementById('title4').innerText = "Encendido";
	changeForeground('green', 'title4');
	eel.process(10, 1);
    }else{
	document.getElementById('title4').innerText = "Apagado";
	changeForeground('red', 'title4');
	eel.process(10, 0);
    }
});


function changeForeground(color, id){
    document.getElementById(id).style.color = color;
}

changeForeground('red');

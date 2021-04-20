// OCdt Lu, X. 28297 and OCdt Tang, T. 28296

const flipper = document.getElementById("flipper");
if (flipper != null){
	flipper.onclick = function(){toggle_me()};
}


function toggle_me(){
	const disp1 = document.getElementById("pagelabel");
	const disp2 = document.getElementById("flipper");
	const hidden = document.getElementById("mode");
	if (disp1 != null && disp2 != null && hidden != null){
		if (disp1.innerText === "Sign In"){
			disp1.innerText = "Create Account";
			disp2.innerText = "already have an account?";
			hidden.value = "signup";
		} else if (disp1.innerText === "Create Account"){
			disp1.innerText = "Sign In";
			disp2.innerText = "or create an account!";
			hidden.value = "login";
		}
	}
}

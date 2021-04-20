// OCdt Lu, X. 28297 and OCdt Tang, T. 28296



const msg = document.getElementById("message");
update_count();
if (msg != null){
	msg.addEventListener("keyup", update_count, false);
}


function update_count(){
	const num = document.getElementById("num");
	const wrn = document.getElementById("warning");
	if (num != null && wrn != null){
		const msglen = msg.value.length;
		num.innerText = msglen + " characters in message (limit 4000)"
		if (msglen < 4000){
			wrn.innerText = "Character limit all good!"
		} else if (msglen === 4000){
			wrn.innerText = "Beware: Character limit reached!"
		} else if (msglen > 4000){
			wrn.innerText = "WARNING: Character limit exceeded!"
		}
	}
}
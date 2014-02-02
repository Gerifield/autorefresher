// ==UserScript==
// @name       WebSocket AutoRefresher
// @namespace  http://gerifield.hu
// @version    0.1
// @description  WebSocket AutoRefresher script to auto reload pages
// @copyright  2014+, Gerifield
// ==/UserScript==

window.addEventListener("load", LocalMain, false);

function LocalMain ()
{
	var sock = new WebSocket("ws://localhost:9998");
	sock.onopen = function(){
	    //sock.send("Msg...");
	    console.log("Connected to the server");
	};

	sock.onmessage = function(evt){
	    //console.log(evt.data)
	    if(evt.data =="refresh"){
			window.location.reload();
	    }
	};

	sock.onclose = function(){
	    console.log("Server connection closed.");
	};
}
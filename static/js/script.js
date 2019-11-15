String.prototype.capitalize = function() 
{
	return this.charAt(0).toUpperCase() + this.slice(1);
}

/*var dataObj = {};
dataObj['user_id'] = window.location.hash.substr(1)*/
var ifs =document.getElementById("keypad"); 
var myvideo = document.getElementById("myAudio");
var message= "Hello! I am Adhyayan, your personal query resolver bot "
$( document ).ready(function() {
	
	myvideo.play();
	myvideo.muted = false;
	var username =  Math.random().toString(36).substr(2, 6);
	var BotResponse = '<img class="botAvatar" src="./static/img/logo (1).png"><p class="botMsg">' + message + '</p><div class="clearfix"></div>';
	$(BotResponse).appendTo('.chats').hide().fadeIn(1000);
   	$('.profile_div').toggle();
	$('.widget').toggle();
localStorage.clear();
	ifs.focus()
	/*x.play();*/
	scrollToBottomOfResults();


// on input/text enter--------------------------------------------------------------------------------------
$('.usrInput').on('keyup keypress', function (e) {
	var keyCode = e.keyCode || e.which;
	var text = $(".usrInput").val().capitalize();
	if (keyCode === 13) {
		if (text == "" || $.trim(text) == '') {
			e.preventDefault();
			return false;
		} else {
			$(".usrInput").blur();
			setUserResponse(text);
			send(text);
			e.preventDefault();
			return false;
		}
	}
});

//------------------------------------- Set user response------------------------------------
function setUserResponse(val) {


	var UserResponse = '<img class="userAvatar" src=' + "./static/img/userAvatar.jpg" + '><p class="userMsg">' + val + ' </p><div class="clearfix"></div>';
	$(UserResponse).appendTo('.chats').show('slow');
	$(".usrInput").val('');
	ifs.focus()
	scrollToBottomOfResults();
	$('.suggestions').remove();
/*	if ( UserResponse == " ")
		setTimeout(function(){
  $(".chats").location.reload(1);
 }, 1000);*/
	/*var BotResponse = '<img class="botAvatar" src="./static/img/logo (1).png"><p class="botMsg">' + message + '</p><div class="clearfix"></div>';
	$(BotResponse).appendTo('.chats').hide().fadeIn(1000);*/
}

//---------------------------------- Scroll to the bottom of the chats-------------------------------
function scrollToBottomOfResults() {
	var terminalResultsDiv = document.getElementById('chats');
	terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight - terminalResultsDiv.clientHeight;
}

function send(message) {
	$.ajax({
		url: 'http://localhost:5005/webhooks/rest/webhook',
		type: 'POST',
		cache: true,
		headers: {
				'Content-Type': 'application/json'
			},
		data: JSON.stringify({
			"sender": username,
				"message": message
		}),

		success: function (data, textStatus) {
			
			console.log("Rasa Response: ", data, "\n Status:", textStatus)

			setBotResponse(data);
		},
		error: function (errorMessage) {
			setBotResponse("");
			console.log('Error' + errorMessage);

		}
	});
}

//------------------------------------ Set bot response -------------------------------------

function setBotResponse(val) {
	
		if (val.length < 1) {
			//if there is no response from Rasa
			msg = 'I couldn\'t get that. Let\' try something else!';

			var BotResponse = '<img class="botAvatar" src="./static/img/logo (1).png"><p class="botMsg">' + msg + '</p><div class="clearfix"></div>';
			$(BotResponse).appendTo('.chats').hide().fadeIn(1000);
			ifs.focus()
			scrollToBottomOfResults();

		}
		else {
			sessionStorage.clear();
			//if we get response from Rasa
			for (i = 0; i < val.length; i++) {

				//check if there is text message
				if (val[i].hasOwnProperty("text")) {
					var BotResponse = '<img class="botAvatar" src="./static/img/logo (1).png"><p class="botMsg">' + val[i].text + '</p><div class="clearfix"></div>';
					$(BotResponse).appendTo('.chats').hide().fadeIn(1000);
				}

				//check if there is image
				if (val[i].hasOwnProperty("image")) {
					var BotResponse = '<div class="singleCard">' +
						'<img class="imgcard" src="' + val[i].image + '">' +
						'</div><div class="clearfix">'
					$(BotResponse).appendTo('.chats').hide().fadeIn(1000);
				}

				//check if there is  button message
				if (val[i].hasOwnProperty("buttons")) {
					addSuggestion(val[i].buttons);
				}

			}
			scrollToBottomOfResults();
		}

	};



// ------------------------------------------ Toggle chatbot -----------------------------------------------
$('#profile_div').click(function () {
	$('.profile_div').toggle();
	$('.widget').toggle();
	scrollToBottomOfResults();
});

$('#close').click(function () {
	$('.profile_div').toggle();
	$('.widget').toggle();
});


// ------------------------------------------ Suggestions -----------------------------------------------

function addSuggestion(textToAdd) {
	setTimeout(function () {
		var suggestions = textToAdd;
		var suggLength = textToAdd.length;
		
		$(' <div class="singleCard"> <div class="suggestions"><div class="menu"></div></div></diV>').appendTo('.chats').hide().fadeIn(1000);
		// Loop through suggestions
		for (i = 0; i < suggLength; i++) {
			$('<div class="menuChips">' + suggestions[i].title + '</div>').appendTo('.menu');
			
		}
		scrollToBottomOfResults();
	}, 1000);
}


// on click of suggestions, get the value and send to rasa
$(document).on("click", ".menu .menuChips", function () {
	var text = this.innerText;
	setUserResponse(text);
	send(text);
	$('.suggestions').remove(); //delete the suggestions 
});
});
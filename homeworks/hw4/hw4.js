
/*
Callback for the floating add button
Opens a modal dialog with a form to enter details.	
*/
function open_add() {
	 $('#add_dialog').openModal();
}

/*
Function to create a card
*/
function create_card(parent, is_complete, task_text, is_append) {
	console.log("create_card");
	
	var card_style = 'card red lighten-1';
	var action_text = 'Mark as complete';
	var click_cb = mark_complete;

	if(is_complete){
		card_style = 'card green darken-1';
		action_text = 'Mark as incomplete';
		click_cb = mark_incomplete;
	}

	var li = $('<li/>', {
		 'class': 'collection-item',
		});
	var row =  $('<div/>', {
		 'class': 'row',
		});
	var grid_def =  $('<div/>', {
		 'class': 'col s12',
		});
	var card =  $('<div/>', {
		 'class': card_style,
		});
	var card_content =  $('<div/>', {
		 'class': 'card-content white-text',
		});
	var card_text =  $('<p/>', {
		 html : task_text,
		});
	var card_action =  $('<div/>', {
		 'class': 'card-action',
		});
	var card_link = $('<a/>', {
		 html : action_text,
		});
	
	card_text.appendTo(card_content);
	card_content.appendTo(card);

	card_link.click(click_cb);
	card_link.appendTo(card_action);
	card_action.appendTo(card);

	card.appendTo(grid_def);
	grid_def.appendTo(row);
	row.appendTo(li);
	if(is_append)
		li.appendTo(parent);
	else
		li.prependTo(parent)
}

/*
 Removes the card from teh input parent element.	
*/

function remove_card(parent, card) {
	$(parent).find(card).remove();
}

/*
Callback for the floating add button
Opens a modal dialog with a form to enter details.	
*/
function add_task() {
	var card_text = $("#task").val();
	 $("#task").val('');
	if(card_text.length)
		create_card('div.todo > ul', false, card_text , false);
}

/*
Callback for 'Mark as Complete' action.	
*/
function mark_complete(inEvent) {
	var card_link = inEvent.currentTarget;
	var card_text = $(card_link).closest('.card').find('p').text();
	remove_card('div.todo > ul', card_link.closest('li'));
	create_card('div.completed > ul', true, card_text, false);
}

/*
Callback for 'Mark as Incomplete' action.	
*/
function mark_incomplete(inEvent) {
	var card_link = inEvent.currentTarget;
	var card_text = $(card_link).closest('.card').find('p').text();
	remove_card('div.completed > ul', inEvent.currentTarget.closest('li'));
	create_card('div.todo > ul', false, card_text, false);
}
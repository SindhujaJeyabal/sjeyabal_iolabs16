
songItemEnum = {
	LIST_NOT_IN_PLAYLIST: 0,
	LIST_ALSO_IN_PLAYLIST: 1,
	PLAYLIST: 2
}

//Modify action buttons

function modify_song_item(song_item, enumerate){
	$(document).find(song_item).find('a').remove();
	make_button('play_circle_outline', play_song).appendTo(song_item);
	if (enumerate == songItemEnum.LIST_NOT_IN_PLAYLIST)
		make_button('playlist_add', add_to_playlist).appendTo(song_item);
	else if(enumerate == songItemEnum.PLAYLIST)
		make_button('delete', remove_from_playlist).appendTo(song_item);
}

//Add to playlist
function add_to_playlist(inEvent){
	var song_item = inEvent.currentTarget.closest('li');
	var song_id = $(document).find(song_item).data('id');
	var permalink_url = $(document).find(song_item).data('permalink_url');

	var to_add = $('#songs').find(song_item).clone();
	modify_song_item(song_item, songItemEnum.LIST_ALSO_IN_PLAYLIST);
	$('#playlist').prepend(to_add);
	$(document).find(to_add).data("id", song_id);
	$(document).find(to_add).data("permalink_url", permalink_url);
	modify_song_item(to_add, songItemEnum.PLAYLIST);
}

//Remove from playlist
function remove_from_playlist(inEvent){
	var song_item = inEvent.currentTarget.closest('li');
	var song_id = $(document).find(song_item).data('id');
	$('#playlist').find(song_item).remove();
	var to_modify = $("li:data(id)").filter(function () {
                        return $(this).data("id") == song_id;
                    });
	modify_song_item(to_modify, songItemEnum.LIST_NOT_IN_PLAYLIST);
}

// 'Play' button event handler - play the track in the Stratus player
function changeTrack(url) {
	// Remove any existing instances of the Stratus player
	$('#stratus').remove();

	// Create a new Stratus player using the clicked song's permalink URL
	$.stratus({
      key: "b3179c0738764e846066975c2571aebb",
      auto_play: true,
      align: "bottom",
      links: url
    });
}

//play song
function play_song(inEvent){
	var song_item = inEvent.currentTarget.closest('li');
	var permalink_url = $(document).find(song_item).data('permalink_url');
	changeTrack(permalink_url);
}
//helper function to make a button
function make_button(button_name, click_cb){

	var button = $('<a/>', {
		'class': 'action-button',
		});
	var inner_img = $('<i/>',{
		'class': 'material-icons',
		html: button_name,
		});
	inner_img.appendTo(button);
	button.click(click_cb);
	return button;
}
//Append song item
function add_song_item(song_detail){

	var art_url = song_detail['user']['avatar_url'];
	var song_title = song_detail['title'];
	var artist_title = song_detail['user']['username'];

	var li = $('<li/>', {
		 'class': 'collection-item avatar',
		});
	var artist_image = $('<img/>', {
		'class': 'circle',
		src: art_url,
		});
	var song_name = $('<span/>', {
		'class': 'title',
		html: song_title,
		});
	var artist_name = $('<p/>', {
		html: artist_title,
		});

	artist_image.appendTo(li);
	song_name.appendTo(li);
	artist_name.appendTo(li);
	make_button('play_circle_outline', play_song).appendTo(li);
	make_button('playlist_add', add_to_playlist).appendTo(li);
	li.appendTo($('#songs'));
	$(document).find(li).data("id", song_detail['id']);
	$(document).find(li).data("permalink_url", song_detail['permalink_url']);
}

// Function to load the response data on the page.
function load_songs(data){
	var list_len = (data.length > 20)? 20: data.length;
	for(i = 0; i < data.length; i++){
		add_song_item(data[i]);
	}
}

// Event hander for calling the SoundCloud API using the user's search query
function callAPI(query) {
	$.get("https://api.soundcloud.com/tracks?client_id=b3179c0738764e846066975c2571aebb",
		{'q': query,
		'limit': '100'},
		function(data) {
			load_songs(data);
		},'json'
	);
}

function init(){
	$(document).ready( function(){
		$('#queryButton').click( function(inEvent){
			queryText = $('#queryText').val();
			callAPI(queryText);
		});

		$( "#playlist" ).sortable();
    	$( "#playlist" ).disableSelection();

	});
}

init();




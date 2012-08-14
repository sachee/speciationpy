all_boards = []

$.ajax({
  	url:'example.json', 
  	dataType: 'json',
  	success: function(boards) {
	  	all_boards = boards;

	  	// $.each(data, function(index, board_data){

	  	// });
		// $.each(data, function(key, val) {
		// 	items.push('<li id="' + key + '">' + val + '</li>');
		// });

		// $('<ul/>', {
		// 	'class': 'my-new-list',
		// 	html: items.join('')
		// }).appendTo('body');
	},
	error:function(){
    	alert("Error");
 	},
});

function get_board(index){
	return all_boards[index]
}
function next_board(curr_index){
	return all_boards[curr_index+1];
}

function display_board(index){
	board = all_boards[index]
	grid_size = board["grid_size"]	
	grid = board["grid"]
	var total_ecos = 0 // keep track of the total ecos displayed
	while (total_ecos != (grid_size*grid_size){

		for (i=0; i<grid_size; i++){

		}
	}
}

function get_boards(boards){

	alert("YAY!");
	  	var items = [];
	  	for(board in boards){
	  		for(i=0; i<2; i++){
	  			if (i == 1){
	  				var grid_size = board[1]
	  			}
	  			else{
	  				var generation_board = board[0] // this is a dictionary of ecosystems
	  			}
	  		}
	  	}
}



// {
// 	[
// 		{"grid": [{"color": "#", "number": 0}, {"color": "#", "number": 188}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 61}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}], 
// 		"grid_size": 4}
// 	],
// 		[
// 			{"grid": [{"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}, {"color": "#", "number": 0}], 
// 			"grid_size": 4}
// 		]

// }
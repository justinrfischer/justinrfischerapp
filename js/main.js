
$( document ).ready(function() {
	
});
/*

Ajax Page Loading

*/
function getMainPage(){
	$.ajax({
	    url : '/',
	    type : 'GET',
	    dataType : 'html',
	    success : function(data, xhr, status) {
	        renderPageData(data);
	    }
	});
};

function getResumePage(){
	$.ajax({
	    url : '/resume',
	    type : 'GET',
	    dataType : 'html',
	    success : function(data, xhr, status) {
	        renderPageData(data);
	    }
	});
};

function getDemoReelPage(){
	$.ajax({
	    url : '/demoreel',
	    type : 'GET',
	    dataType : 'html',
	    success : function(data, xhr, status) {
	        renderPageData(data);
	    }
	});
};

function getExtrasPage(){
	$.ajax({
	    url : '/extras',
	    type : 'GET',
	    dataType : 'html',
	    success : function(data, xhr, status) {
	        renderPageData(data);
	    }
	});
};

function renderPageData(data){
	$("body").empty();
	$("body").html(data);
}
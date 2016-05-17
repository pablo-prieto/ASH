//----------------------------------------------------------------------------------------//
//                          TABS (About me, Events, Pictures)                             //
//----------------------------------------------------------------------------------------// 

// Makes the current tab active after a page reload/refresh
$(function() { 
    // for bootstrap 3 use 'shown.bs.tab', for bootstrap 2 use 'shown' in the next line
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        // save the latest tab; use cookies if you like 'em better:
        localStorage.setItem('lastTab', $(this).attr('href'));
    });

    // go to the latest tab, if it exists:
    var lastTab = localStorage.getItem('lastTab');
    if (lastTab) {
        $('[href="' + lastTab + '"]').tab('show');
    }
});


/* Displays the modal with the details of the selected memory */
function memoryDetail(index) {
    $('#memoryDetail'+index).modal('show');
}


/* Displays the modal with a form to add a memory */
function addMemory() {
    $('#addMemory').modal('show');
}


/* Scrolls the screen to the carousel */
function scrollToCarousel(index) {
    // var target = $(carouselId).parent().siblings('h4');
    $("#memoryDetail"+index).animate({ scrollTop: $("#myCarousel"+index).position().top + 40}, 'medium');
    return false;
}


/* Reads the image and renders the picture in the panel/icon */
function readImage(input) {
    // If a file has been chosen
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        // Read the input as URL. The result will be stored in 'this.result' after the 'load' event fires
        reader.readAsDataURL(input.files[0]);

        // Called when the read operation successfully completes
        reader.onload = function (e) {
            $(input.parentNode.childNodes[1]).html("<img id='uploadedPicture' class='img-square' src='"+ e.target.result +"'>");
            $(input.parentNode).css( "background-color", "#efefee" );
        };
    }
    else {
        // Display back the "Add Image" message
        $(input.parentNode.childNodes[1]).html("<br><br><span class='plus-sign'>+</span><p class='add-img-msg'>Add Image</p>");
        $(input.parentNode).css( "background-color", "#e6e6e5");
    }
}


/* Adds a panel to add an image to a memory and its description */
var panel_index = 1;
function addImgPanel(option, index) {
    // Clone the hidden readroot div that contains the structure of a img panel
    // Change the style display to show it in the website
    // Change its id name to a unique name using a panel_index
    var newFieldsDiv = document.getElementById('readroot').cloneNode(true);
    newFieldsDiv.style.display = 'inline-block';
    newFieldsDiv.id = 'img-panel' + panel_index;

    // Change the img-title name, img-input id, img-input name and text-input name
    // Add a unique name to use it in the form
    var picTitleField = newFieldsDiv.querySelectorAll("input")[0];
    var picFileField = newFieldsDiv.querySelectorAll("input")[1];
    var picDetailField = newFieldsDiv.querySelectorAll("textarea")[0];
    picTitleField.name = picTitleField.name + panel_index;
    picFileField.id = picFileField.id + panel_index;
    picFileField.name = picFileField.id;
    picDetailField.name = picDetailField.name + panel_index;
    panel_index++;
    
    // Find the location to be added and insert the new panel
    // Based on the option, it will insert it at a different location (id name):
    // One option is adding img panels when creating a new memory
    // Another option is adding img panels when adding pictures to an existing memory
    var insertHere;
    if(option == "panelForNewMem") {
        insertHere = document.getElementById('writeroot');
    }
    else {
        insertHere = document.getElementById('writeroot-panel-for-existing-mem'+index);
    }
    insertHere.parentNode.insertBefore(newFieldsDiv,insertHere);   
}


/* Closes the respective img panel */
function closeImgPanel(x_button){
    // Note: Do not decrease the panel_index when deleting because it will duplicated names for the img inputs 
    $(x_button.parentNode).remove();
}


/* Saves the memory */
$(function() {
    var form = $('#form-add-memory');    
    $(form).submit(function(event){
        event.preventDefault();
        var formData = new FormData(form[0]);
        $.ajax({
            type: $(this).attr('type'),
            url: $(this).attr('action'),        
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
        })
        .done(function(response) {
            panel_index = 0;
            $('#addMemory').modal('hide');
            $('#memoryAdditionConfirmation').modal('show');
        })
        .fail(function(response) {
            // Pass
        });
    });
});


/* Adds a picture with its title and description */
function addPictureToMemory(index) {
    $('#memoryDetail'+index).modal('hide');
    $('#addPictureToMemory'+index).modal('show');
}


/* Saves the picture(s) to the selected memory */
function submitAddPicToMem(index) {
    var form = $('#form-add-pic-to-mem'+index);    
    $(form).submit(function(event){
        event.preventDefault();
        var formData = new FormData(form[0]);
        $.ajax({
            type: $(this).attr('type'),
            url: $(this).attr('action'),        
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
        })
        .done(function(response) {
            panel_index = 1;
            $('#addPictureToMemory'+index).modal('hide');
            $('#pictureAdditionConfirmation'+index).modal('show');
        })
        .fail(function(response) {
            // Pass
        });
    });
}
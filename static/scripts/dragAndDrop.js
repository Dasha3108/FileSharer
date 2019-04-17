function dragEnter(e) {
    // Adds "drag enter" class to dropBox when dragenter event happens

    e.stopPropagation();
    e.preventDefault();

    let dropBox = document.getElementById("dropBox");
    dropBox.classList.add('dragEnter');
}

function dragOver(e) {
    // Stops propagation when dragover event happens

    e.stopPropagation();
    e.preventDefault();
}

function drop(e) {
    // Removes "drag enter" class from dropBox,
    // adds dragged files to fileInput and calls fileInput onchange action
    // when drop event happens
    e.stopPropagation();
    e.preventDefault();

    let dropBox = document.getElementById("dropBox");
    dropBox.classList.remove('dragEnter');

    let dataTransfer = e.dataTransfer;
    let fileInput = document.getElementById('fileUpload');

    fileInput.files = dataTransfer.files;
    fileInput.onchange();
}

function addFileDragAndDrop() {
    // Adds drag events listeners to dropBox

    let dropBox = document.getElementById("dropBox");

    dropBox.addEventListener("dragenter", dragEnter, false);
    dropBox.addEventListener("dragover", dragOver, false);
    dropBox.addEventListener("drop", drop, false);
}
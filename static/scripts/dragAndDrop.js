function dragEnter(e) {
    e.stopPropagation();
    e.preventDefault();

    let dropBox = document.getElementById("dropBox");
    dropBox.classList.add('dragEnter');
}

function dragOver(e) {
    e.stopPropagation();
    e.preventDefault();
}

function drop(e) {
    e.stopPropagation();
    e.preventDefault();

    let dropBox = document.getElementById("dropBox");
    dropBox.classList.remove('dragEnter');

    let dt = e.dataTransfer;
    let fileInput = document.getElementById('fileUpload');

    fileInput.files = dt.files;
    fileInput.onchange();
}

function addFileDragAndDrop() {
    let dropBox = document.getElementById("dropBox");
    dropBox.addEventListener("dragenter", dragEnter, false);
    dropBox.addEventListener("dragover", dragOver, false);
    dropBox.addEventListener("drop", drop, false);
}
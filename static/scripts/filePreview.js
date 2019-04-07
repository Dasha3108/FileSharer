function unblock_transfer_button() {
    if(document.getElementById("fileUpload").value !== "") {
        let button = document.getElementById("transferButton");
        button.disabled = false;

        button.classList.remove("transfer-button-inactive");
    }
}

function showFileInfo(file) {
    document.getElementById("progressBarContainer").style.visibility = "hidden";
    document.getElementById("fileInfo").style.visibility = "visible";
    document.getElementById("fileSize").innerText = formatFileSize(file.size);
    document.getElementById("fileType").innerText = file.name.split('.').pop();
    document.getElementById("fileName").innerText = file.name;
}

function handleFileUpload(files) {
    let file = files[0];

    if (file === undefined) return;

    unblock_transfer_button();

    showFileInfo(file);
}

function showUploadProgress(file) {
    document.getElementById("progressBarContainer").style.visibility = "visible";

    var formdata = new FormData();
    formdata.append("file1", file);
    let ajax = new XMLHttpRequest();
    ajax.upload.addEventListener("progress", progressHandler, false);

    ajax.send(formdata);
}


function progressHandler(event) {
    let elem = document.getElementById("progressBar");
    let percent = (event.loaded / event.total) * 100;
    elem.style.width = Math.round(percent) + '%';
}

function formatFileSize(bytes) {
    let thresh = 1000;

    if(Math.abs(bytes) < thresh) {
        return bytes + ' B';
    }

    let units = ['kB','MB','GB','TB','PB','EB','ZB','YB'];
    let u = -1;
    do {
        bytes /= thresh;
        ++u;
    }
    while(Math.abs(bytes) >= thresh && u < units.length - 1);

    return bytes.toFixed(1) + ' ' + units[u];
}

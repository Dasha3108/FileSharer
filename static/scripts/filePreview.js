function unblock_transfer_button() {
    // Unblocks transfer buttons, removes inactive class from it

    if(document.getElementById("fileUpload").value !== "") {
        let button = document.getElementById("transferButton");
        button.disabled = false;

        button.classList.remove("transfer-button-inactive");
    }
}

function showFileInfo(file) {
    // Shows passed file info in container

    document.getElementById("progressBarContainer").style.visibility = "hidden";
    document.getElementById("fileInfo").style.visibility = "visible";

    document.getElementById("fileSize").innerText = formatFileSize(file.size);
    document.getElementById("fileType").innerText = file.name.split('.').pop();

    let fileNameLink = document.getElementById("fileName");
    fileNameLink.innerText = file.name;

    if (file.type.startsWith("image") ||
        file.type.includes("html") ||
        file.type.includes("pdf")) {

        fileNameLink.href = window.URL.createObjectURL(file);
        return
    }

    fileNameLink.removeAttribute("href");
}

function handleFileUpload(files) {
    // Gets the uploaded file, unblocks transfer button
    // and shows its info

    let file = files[0];

    if (file === undefined) return;

    unblock_transfer_button();

    showFileInfo(file);
}

function formatFileSize(bytes) {
    // Returns human readable file size

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

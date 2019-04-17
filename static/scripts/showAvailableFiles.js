function updateFilesView() {
    // Updates the files container
    // Send request to server
    // And updates with received files

    $.ajax({
        url: '/get_available_files/',
        type: 'GET',
        success:
            function (a) {
                showFiles(a)
        },
        error: function(xhr) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    })
}

function showFiles(files) {
    // Dynamically creates containers for passed files

    const filesInARow = 5;

    let filesNumber = 0;
    let currentRowDiv;
    let filesContainer = document.getElementById("uploadedFilesContainer");

    for (let file of files) {

        if (filesNumber % filesInARow === 0) {
            currentRowDiv = document.createElement("div");
            currentRowDiv.classList.add("uploaded-files-row");

            filesContainer.appendChild(currentRowDiv)
        }

        let fileToDownloadContainer = createAndGetFileContainer(file);

        currentRowDiv.appendChild(fileToDownloadContainer);

        filesNumber += 1;
    }
}

function createAndGetFileContainer(file) {
    // Creates a container with link as file name
    // and button to download this file

    let fileToDownloadContainer = document.createElement("div");
    fileToDownloadContainer.classList.add("file_to_download_container");

    let fileLink = document.createElement("a");
    fileLink.classList.add("download-file-link");
    fileLink.innerText = file["file_name"];
    fileLink.href = file["link"];

    let download_button = document.createElement("a");
    download_button.classList.add("download-button");
    download_button.href = file["link"];
    download_button.target = "_blank";

    let download_button_image = document.createElement("img");
    download_button_image.classList.add("download-button-image");
    download_button_image.src = "../../static/images/download.png";

    download_button.appendChild(download_button_image);

    fileToDownloadContainer.appendChild(fileLink);
    fileToDownloadContainer.appendChild(download_button);

    return fileToDownloadContainer
}
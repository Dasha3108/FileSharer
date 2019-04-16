function updateFilesView() {
    $.ajax({
        url: '/get_available_files/',
        type: 'GET',
        success:
            function (a) {
                showFiles(a)
        },
        error: function(xhr) {
            alert(xhr.status + ": " + xhr.responseText);
        }
    })
}

function showFiles(data) {
    const filesInARow = 5;

    let filesNumber = 0;
    let currentRowDiv;
    let filesContainer = document.getElementById("uploadedFilesContainer");

    for (let file of data) {

        if (filesNumber % filesInARow === 0) {
            currentRowDiv = document.createElement("div");
            currentRowDiv.classList.add("uploaded-files-row");

            filesContainer.appendChild(currentRowDiv)
        }

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

        currentRowDiv.appendChild(fileToDownloadContainer);

        filesNumber += 1;
    }
}
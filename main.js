document.addEventListener("DOMContentLoaded", function () {
    const textEditor = document.getElementById("text-editor");
    const fileInput = document.getElementById("file-input");

    const savedContent = localStorage.getItem("editorContent");
    if (savedContent) {
        textEditor.value = savedContent;
    }

    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                textEditor.value = e.target.result;
            };
            reader.readAsText(file);
        }
    });
});

function downloadFile() {
    const textEditor = document.getElementById("text-editor");
    const content = textEditor.value;
    const blob = new Blob([content], { type: 'text/plain' });
    const anchor = document.createElement('a');
    anchor.download = 'text-editor-content.txt';
    anchor.href = window.URL.createObjectURL(blob);
    anchor.click();
    window.URL.revokeObjectURL(anchor.href);
}

function uploadFile() {
    const fileInput = document.getElementById("file-input");
    fileInput.click();
}

function saveFile() {
    const textEditor = document.getElementById("text-editor");
    const content = textEditor.value;
    const blob = new Blob([content], { type: 'text/plain' });
    const anchor = document.createElement('a');
    anchor.download = 'text-editor-content.txt';
    anchor.href = window.URL.createObjectURL(blob);
    anchor.click();
    window.URL.revokeObjectURL(anchor.href);
}
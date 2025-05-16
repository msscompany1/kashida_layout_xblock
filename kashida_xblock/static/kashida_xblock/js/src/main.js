window.addEventListener("load", function () {
    const editors = [];

    const imageRegion = document.querySelector('#imageRegion');
    const textRegion = document.querySelector('#textRegion');

    if (imageRegion) {
        ClassicEditor
            .create(imageRegion, {
                toolbar: [
                    'bold', 'italic', 'link', 'bulletedList', 'numberedList', '|',
                    'undo', 'redo'
                ]
            })
            .then(editor => {
                console.log('✅ Image editor initialized');
                editors.push(editor);
            })
            .catch(error => {
                console.error('❌ Error loading image editor:', error);
            });
    }

    if (textRegion) {
        ClassicEditor
            .create(textRegion, {
                toolbar: [
                    'heading', '|',
                    'bold', 'italic', 'link', 'blockQuote', '|',
                    'undo', 'redo'
                ]
            })
            .then(editor => {
                console.log('✅ Text editor initialized');
                editors.push(editor);
            })
            .catch(error => {
                console.error('❌ Error loading text editor:', error);
            });
    }
});

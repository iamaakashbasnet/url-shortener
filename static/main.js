var clip = new Clipboard('.btn');
var copyBtn = document.querySelector('.list-group');

clip.on('success', function () {
    copyBtn.insertAdjacentHTML(
        'beforebegin',
        `<div class="alert alert-success alert-dismissible fade show">
            Copied!
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`
    );
});
clip.on('error', function () {
    copyBtn.insertAdjacentHTML('beforeend', '<div>Failed to copy!</div>');
});

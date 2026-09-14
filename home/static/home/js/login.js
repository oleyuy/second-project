const passwordInput = document.querySelector('#id_password');

let hideTimer;

passwordInput.addEventListener('input', function () {
    clearTimeout(hideTimer);

    this.type = 'text';

    hideTimer = setTimeout(() => {
        this.type = 'password';
    }, 1000);
});
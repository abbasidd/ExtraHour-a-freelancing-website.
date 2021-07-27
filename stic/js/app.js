const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') == 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});
const togglePassword1 = document.querySelector('#togglePassword1');
const re_password = document.querySelector('#re-password');

togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = re_password.getAttribute('type') == 're-password' ? 'text' : 're-password';
    re_password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

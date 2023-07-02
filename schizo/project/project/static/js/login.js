const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const box = document.getElementById('box');

signUpButton.addEventListener('click', () => {
  box.classList.add("right-panel-active");
  box.querySelector('.sign-in-form').classList.remove('active');
  box.querySelector('.sign-up-form').classList.add('active');
});

signInButton.addEventListener('click', () => {
  box.classList.remove("right-panel-active");
  box.querySelector('.sign-in-form').classList.add('active');
  box.querySelector('.sign-up-form').classList.remove('active');
});
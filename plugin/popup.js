// adding a new bookmark row to the popup
const main = document.querySelector("#main");

const isSignedIn = () => {
  return false;
};

function openLoginTab() {
  window.open("https://www.google.com", "_blank");
}

function loginView() {
  main.innerHTML = `<div class="login">
    <button id="login__button"">Login</button>
    <p id="login__text">login to start tracking your life!</p>
  </div>
  `;

  const loginButton = document.querySelector("#login__button");
  loginButton.addEventListener("click", openLoginTab);
}

document.addEventListener("DOMContentLoaded", () => {});

function init() {
  if (isSignedIn()) {
  } else {
    loginView();
  }
}

init();

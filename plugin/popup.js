// adding a new bookmark row to the popup
const main = document.querySelector("#main");

const isSignedIn = () => {
  const user_id = localStorage.getItem("apiKey");
  return user_id !== null;
};

function saveApiKey() {
  const apiKey = document.querySelector("#api-key").value;
  localStorage.setItem("apiKey", apiKey);
}

function loginView() {
  console.log(localStorage.getItem("apiKey"));

  main.innerHTML = `<div class="login">
    <input type="text" id="api-key" placeholder="enter your api key">
    <button id="login__button"">Apply</button>
    <p id="login__text">enter your Api key to start tracking your life! <a href="http://localhost:5173/login">to get api key</p>
  </div>
  `;

  const loginButton = document.querySelector("#login__button");
  loginButton.addEventListener("click", saveApiKey);
}

document.addEventListener("DOMContentLoaded", () => {});

function init() {
  if (isSignedIn()) {
  } else {
    loginView();
  }
}

init();

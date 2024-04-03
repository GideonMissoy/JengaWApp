document.addEventListener("DOMContentLoaded", function () {
  const wrapper = document.querySelector(".wrapper");
  const loginLink = document.querySelector(".login-link");
  const registerLink = document.querySelector(".register-link");
  const btnPopup = document.querySelector(".btnLogin");
  const iconClose = document.querySelector(".icon-close");

  if (registerLink) {
    registerLink.addEventListener("click", () => {
      wrapper.classList.add("active");
    });
  }

  if (loginLink) {
    loginLink.addEventListener("click", () => {
      wrapper.classList.remove("active");
    });
  }

  if (btnPopup) {
    btnPopup.addEventListener("click", () => {
      wrapper.classList.add("active-popup");
    });
  }

  if (iconClose) {
    iconClose.addEventListener("click", () => {
      wrapper.classList.remove("active-popup");
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("form");
    const emailInput = document.querySelector('input[name="email"]');
    const passwordInput = document.querySelector('input[name="password"]');
    const responseMessage = document.querySelector("#responseMessage");

    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = emailInput.value;
        const password = passwordInput.value;

        try {
            const response = await axios.post("http://127.0.0.1:8000/token", { email, password });
            const accessToken = response.data.acess_token; // Certifique-se de que o nome do campo esteja correto
            // Armazene o token em um local seguro, como em um cookie ou LocalStorage
            // Exemplo com LocalStorage:
            localStorage.setItem("accessToken", accessToken);
            responseMessage.innerText = "Login bem-sucedido!";
            // Redirecione para outra página ou realize ações após o login
            window.location.href = "user-page.html";
        } catch (error) {
            console.error(error);
            responseMessage.innerText = "Falha no login. Verifique suas credenciais.";
        }
    }, 2000);
});

// // async function login() {
// //     const emailInput = document.querySelector('input[name="email"]');
// //     const passwordInput = document.querySelector('input[name="password"]');

// //     // Verifique se o campo de e-mail não está vazio
// //     if (!emailInput.value) {
// //         alert('Preencha o campo de e-mail antes de fazer o login.');
// //         return;
// //     }

// //     // Verifique se o email está em um formato válido usando uma expressão regular
// //     const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;
// //     if (!emailRegex.test(emailInput.value)) {
// //         alert('Insira um email válido antes de fazer o login.');
// //         return;
// //     }
// //     try {
// //         const response = await axios.post('http://localhost:8000/token', {
// //             email: emailInput.value,
// //             password: passwordInput.value,
            
// //         });

// //         if (response.status === 200) {
// //             // Login bem-sucedido, faça o redirecionamento ou a ação necessária
// //             console.log('Login bem-sucedido');
// //         }
// //     } catch (error) {
// //         console.error('Erro ao fazer login:', error);
// //     }
// // }

// // // Adicione um evento de clique para chamar a função de login
// // document.querySelector('.btn').addEventListener('click', login);



// async function login() {
//     const emailInput = document.querySelector('input[name="email"]');
//     const passwordInput = document.querySelector('input[name="password"]');

//     if (!emailInput.value) {
//         alert('Preencha o campo de e-mail antes de fazer o login.');
//         return;
//     }

//     const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;
//     if (!emailRegex.test(emailInput.value)) {
//         alert('Insira um email válido antes de fazer o login.');
//         return;
//     }

//     try {
//         const response = await axios.post('http://localhost:8000/token', {
//             email: emailInput.value,
//             password: passwordInput.value,
//         });

//         if (response.status === 200) {
//             const token = response.data.access_token;

//             // Armazene o token em localStorage para uso posterior
//             localStorage.setItem('token', token);

//             // Redirecione ou faça outras ações necessárias após o login bem-sucedido
//             console.log('Login bem-sucedido');
//         }
//     } catch (error) {
//         console.error('Erro ao fazer login:', error);
//     }
// }

// // Adicione um evento de clique para chamar a função de login
// document.querySelector('.btn').addEventListener('click', login);


async function login() {
    const emailInput = document.querySelector('input[name="email"]');
    const passwordInput = document.querySelector('input[name="password"]');
    const responseDiv = document.querySelector('.response');

    if (!emailInput.value) {
        alert('Preencha o campo de e-mail antes de fazer o login.');
        return;
    }

    const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;
    if (!emailRegex.test(emailInput.value)) {
        alert('Insira um email válido antes de fazer o login.');
        return;
    }

    try {
        const response = await axios.post('http://localhost:8000/login', {
            email: emailInput.value,
            password: passwordInput.value,
        });

        if (response.status === 200) {
            const token = response.data.access_token;

            // Armazene o token em localStorage para uso posterior
            localStorage.setItem('token', token);

            // Exiba a resposta do back-end no front-end
            responseDiv.textContent = 'Resposta do servidor: ' + JSON.stringify(response.data);

            // Redirecione ou faça outras ações necessárias após o login bem-sucedido
            console.log('Login bem-sucedido');
        }
    } catch (error) {
        console.error('Erro ao fazer login:', error);
        // Limpe o conteúdo da div de resposta em caso de erro
        responseDiv.textContent = 'Erro ao fazer login.';
    }
}

// Adicione um evento de clique para chamar a função de login
document.querySelector('.btn').addEventListener('click', login);

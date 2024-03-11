const registerForm = document.getElementById('registerForm');
const loginForm = document.getElementById('loginForm');

registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    try {
        const response = await axios.post('http://localhost:8000/register', {
            account_name: username,
            password: password
        });
        alert(response.data.message);
        // Redirect to login page or handle success
    } catch (error) {
        alert(error.response.data.detail);
    }
});

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    try {
        const response = await axios.post('http://localhost:8000/login', {
            account_name: username,
            password: password
        });
        alert(response.data.message);
        const account_id = response.data.account_id;
        localStorage.setItem('account_id', account_id); // เก็บ account_id ลงใน localStorage
        // Redirect to dashboard or handle success
        window.location.href = 'index.html';
    } catch (error) {
        alert('Failed to login. Invalid username or password.');
    }
});
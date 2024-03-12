const registerForm = document.getElementById('registerForm');
const loginForm = document.getElementById('loginForm');

registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const readerRadio = document.getElementById('readerRadio');
    if (readerRadio.checked) {
        try {
            const response = await axios.post('http://127.0.0.1:8000/register_reader', {
                account_name: username,
                password: password
            });
            alert(response.data.message);
            localStorage.setItem('account_type', 'reader');
            localStorage.setItem('username', username);

        } catch (error) {
            alert(error.response.data.detail);
        }
    } else {
        try {
            const response = await axios.post('http://127.0.0.1:8000/register_writer', {
                account_name: username,
                password: password
            });
            alert(response.data.message);
            localStorage.setItem('account_type', 'writer');
            localStorage.setItem('username', username);
            
        } catch (error) {
            alert(error.response.data.detail);
        }
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
        localStorage.setItem('account_id', account_id);
        localStorage.setItem('username', username);
        localStorage.setItem('account_type', response.data.account_type);
        window.location.href = 'index.html';
    } catch (error) {
        alert('Failed to login. Invalid username or password.');
    }
});

function validateUserType() {
    const readerRadio = document.getElementById('readerRadio');
    const writerRadio = document.getElementById('writerRadio');

    if (!readerRadio.checked && !writerRadio.checked) {
        alert('Please select either Reader or Writer');
    } else {
        registerForm.dispatchEvent(new Event('submit'));
    }
}
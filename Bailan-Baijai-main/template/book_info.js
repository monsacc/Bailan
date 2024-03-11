const account_id = localStorage.getItem('account_id');

document.getElementById('addToCartButton').addEventListener('click', function () {
    const queryParams = new URLSearchParams(window.location.search);
    const book_id = queryParams.get('id');
    const account_id = getLoggedInAccountId(); 

    if (book_id && account_id) {
        addToCart(account_id, book_id);
    } else {
        console.error('Book ID or Account ID is missing.');
    }
});

function addToCart(account_id, book_id) {
    fetch(`/add_cart?account_id=${account_id}&book_id=${book_id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log(data);
            alert('Book added to cart successfully!');
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            alert('Error adding book to cart. Please try again later.');
        });
}

// แสดงรายการสินค้าในตะกร้า
function showCart(readerId) {
    fetch(`/show_cart?reader_id=${readerId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            // แสดงรายการสินค้าที่มีอยู่ในตะกร้า
            console.log(data);
            // ทำการแสดงผลในหน้าเว็บ
            // เช่น การสร้าง HTML เพื่อแสดงรายการสินค้าในตะกร้า
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            alert('Error fetching cart data. Please try again later.');
        });
}

document.getElementById('addToCartButton').addEventListener('click', function () {
    const queryParams = new URLSearchParams(window.location.search);
    const book_id = queryParams.get('id');
    const account_id = getLoggedInAccountId(); 

    if (book_id && account_id) {
        addToCart(account_id, book_id);
    } else {
        console.error('Book ID or Account ID is missing.');
    }
});

function addToCart(account_id, book_id) {
    fetch(`/add_cart?account_id=${account_id}&book_id=${book_id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log(data);
            alert('Book added to cart successfully!');
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            alert('Error adding book to cart. Please try again later.');
        });
}

// แสดงรายการสินค้าในตะกร้า
function showCart(readerId) {
    fetch(`/show_cart?reader_id=${readerId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            // แสดงรายการสินค้าที่มีอยู่ในตะกร้า
            console.log(data);
            // ทำการแสดงผลในหน้าเว็บ
            // เช่น การสร้าง HTML เพื่อแสดงรายการสินค้าในตะกร้า
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            alert('Error fetching cart data. Please try again later.');
        });
}
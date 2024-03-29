let selectedBooks = [];
let cartItems;

async function showCartItems() {
    const accountId = localStorage.getItem('account_id');

    try {
        const response = await axios.get(`http://localhost:8000/show_cart?reader_id=${accountId}`);
        cartItems = response.data.reader_cart;

        const cartItemsContainer = document.getElementById('cartItems');
        cartItemsContainer.innerHTML = '';

        if (cartItems === "Reader's cart is empty") {
            updateTotalCoins("Reader's cart is empty");
            return;
        } else {

        cartItems.forEach(item => {
            const bookItem = document.createElement('div');
            bookItem.classList.add('col-md-4', 'mb-4');

            const bookInfo = `
                <div class="card">
                    <img src="images/${item.name}.jpg" class="card-img-top" alt="${item.name} Image">
                    <div class="card-body">
                        <h5 class="card-title">${item.name}</h5>
                        <p class="card-text">Price: ${item.price} coin</p>
                        <button class="btn btn-danger" onclick="removeFromCart(${item.id})">Remove</button>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="bookCheckbox${item.id}" 
                                onchange="toggleBookSelection(${item.id})" ${selectedBooks.includes(item.id) ? 'checked' : ''}>
                            <label class="form-check-label" for="bookCheckbox${item.id}">Select for Checkout</label>
                        </div>
                    </div>
                </div>
            `;

            
            bookItem.innerHTML = bookInfo;
            cartItemsContainer.appendChild(bookItem);
        });
        }

        updateTotalCoins();
    } catch (error) {
        console.error('Error fetching cart items:', error);
    }
}

async function removeFromCart(bookId) {
    const accountId = localStorage.getItem('account_id');
    console.log('Removing book:', bookId);
    try {
        await axios.delete(`http://127.0.0.1:8000/remove_book?reader_id=${accountId}&book_id=${bookId}`);
        console.log('Book removed successfully');

        // After successful removal, refresh the cart items
        showCartItems();
        
    } catch (error) {
        console.error('Error removing book from cart:', error);
    }
}

function updateTotalCoins() {
    const totalCoinsElement = document.getElementById('totalCoins');
    let totalCoins = 0;

    if (cartItems === "Reader's cart is empty") {
        totalCoinsElement.textContent = "Reader's cart is empty";
        return;
    }

    for (const bookId of selectedBooks) {
        const bookItem = cartItems.find(item => item.id === bookId);
        if (bookItem) {
            console.log(bookItem)
            totalCoins += bookItem.price;
        }
    }
    totalCoinsElement.textContent = `Total purchase coins: ${totalCoins} coin Total rental coins: ${totalCoins*0.8} coin`;
}

function toggleBookSelection(bookId) {
    const index = selectedBooks.indexOf(bookId);

    if (index !== -1) {
        selectedBooks.splice(index, 1);
    } else {
        selectedBooks.push(bookId);
    }
    updateTotalCoins();
}

async function rent() {
    if (selectedBooks.length == 0){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Cart is empty!",
            footer: '<a href="#" style="text-align: center;">Why do I have this issue?</a>'
        }); 
        return;
    }
    try {
        console.log(selectedBooks)
        const accountId = localStorage.getItem('account_id');
        const response = await axios.post(`http://127.0.0.1:8000/rent?reader_id=${accountId}`, {
            book_id: selectedBooks
        });
        console.log(response.data.rent);
        Swal.fire({
            icon: "success",
            title: "Book in collection",
            showConfirmButton: false,
            timer: 1500
        });
        for (const book of selectedBooks) {
            removeFromCart(book);
        }
    } catch (error) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
            footer: '<a href="#" style="text-align: center;">Why do I have this issue?</a>'
        }); 
    }
}


async function buy() {
    if (selectedBooks.length == 0){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Cart is empty!",
            footer: '<a href="#" style="text-align: center;">Why do I have this issue?</a>'
        }); 
        return;
    }
    try {
        const accountId = localStorage.getItem('account_id');
        const response = await axios.post(`http://127.0.0.1:8000/buy_book?account_id=${accountId}`, {
            book_id: selectedBooks
        });
        console.log(response.data.Buy);
        Swal.fire({
            icon: "success",
            title: "Book in collection",
            showConfirmButton: false,
            timer: 1500
        });
        for (const book of selectedBooks) {
            removeFromCart(book);
        }
    } catch (error) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
            footer: '<a href="#" style="text-align: center;">Why do I have this issue?</a>'
        }); 
    }
}

function check_collection(accountType) {
    console.log(Type);
    if (accountType === Type) {
      window.location.href = 'reader_book_collection.html';
    } else {
      window.location.href = 'writer_book_collection.html';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function () {
  
    // Check if there is a saved account ID
    if (account_id) {
        // Display the account ID on the page
        // document.getElementById('result').innerHTML = "Account ID: " + account_id;
  
        // Periodically update coin information using the retrieved account ID
        setInterval(function () {
            loadCoinInfo(account_id);
        }, 350); // Update every 5 seconds (adjust as needed)
    } else {
        // Handle the case where there is no saved account ID
        console.log("No account ID found in localStorage.");
    }
  });
  
  function loadCoinInfo(account_id) {
    // Make an AJAX request to fetch coin information using the account ID
    var xhr = new XMLHttpRequest();
  
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var result = JSON.parse(xhr.responseText);
            document.getElementById('result').innerHTML = "Coin: " + result.coin;
        }
    };
  
    // Adjust the URL to match your FastAPI route
    xhr.open("GET", "http://127.0.0.1:8000/search_coin?id=" + account_id, true);
    xhr.send();
  }
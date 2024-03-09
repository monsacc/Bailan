async function search_by_name() {
  const input = document.getElementById("search_by_name").value;
  const content = document.getElementById("content");
  console.log(input);

  const response = await axios.get(
    `http://127.0.0.1:8000/search_book_by_name?name=${input}`
  );

  console.log(response.data);

  const book_list = response.data.book_list;

  displayBookList(book_list);
}

async function search_by_name() {
  const input = document.getElementById("search_by_name").value;
  const content = document.getElementById("content");
  console.log(input);

  const response = await axios.get(
    `http://127.0.0.1:8000/search_book_by_name?name=${input}`
  );

  console.log(response.data);

  const book_list = response.data.book_list;

  displayBookList(book_list);
}

async function get_book_info(id) {
  const response = await axios.get(
    `http://127.0.0.1:8000/book_info?id=${id}`
    );
  console.log(response.data);

  const bookInfo = response.data["Book's info"];
  displayBookInfo(bookInfo);
}

function displayBookList(bookList) {
  const content = document.getElementById("content"); 
  content.innerHTML = '';

  bookList.forEach(book => {
    const div = document.createElement('div');
    const h1 = document.createElement('h1');
    h1.textContent = book.book_name;
    div.appendChild(h1);
    content.appendChild(div);
  });
}

function displayBookInfo(bookInfo) {
  const bookInfoDiv = document.getElementById('bookInfo');
  bookInfoDiv.innerHTML = `
      <h1>${bookInfo.book_name}</h1>
      <p>Writer: ${bookInfo.writer_name}</p>
      <p>Type: ${bookInfo.type_book}</p>
      <p>Introduction: ${bookInfo.intro}</p>
      <p>Rating: ${bookInfo.rating}</p>
  `;

  const bookCover = document.getElementById('bookCover');
  bookCover.src = `image/${bookInfo.book_name}.jpg`;
  bookCover.alt = bookInfo.book_name;
}
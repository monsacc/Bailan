async function search_by_name() {
  const input = document.getElementById("search_by_name").value;
  const content = document.getElementById("content");
  console.log(input);

  const response = await axios.get(
    `http://127.0.0.1:8000/searchbookname?name=${input}`
  );

  console.log(response.data);

  const book_list = response.data.book_list;

  for (let i = 0; i < book_list.length; i++) {
    content.innerHTML += `<div>
    <h1> ${book_list[i].book_name} </h1>
    </div>`;
  }
}

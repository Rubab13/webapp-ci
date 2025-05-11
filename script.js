// 🔥 Firebase Config (replace with your own)
const firebaseConfig = {
  apiKey: "AIzaSyDXZifXTeQG8kdOYjqXbRIx1RoCB5jxGfk",
  authDomain: "bookmanager-8e758.firebaseapp.com",
  databaseURL: "https://bookmanager-8e758-default-rtdb.firebaseio.com",
  projectId: "bookmanager-8e758",
  storageBucket: "bookmanager-8e758.firebasestorage.app",
  messagingSenderId: "367369800718",
  appId: "1:367369800718:web:27153ec77f61667456805f",
  measurementId: "G-DESQED7HVY"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const signoutBtn = document.getElementById("signout-btn");

const bookSection = document.getElementById("book-section");
const bookForm = document.getElementById("book-form");
const bookList = document.getElementById("book-list");

let currentUserId = null;

// 📩 Sign Up
function signUp() {
  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();

  auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      alert("Signed up successfully!");
      showBookSection(userCredential.user);
    })
    .catch((error) => {
      if (error.code === 'auth/email-already-in-use') {
        alert("This email is already registered. Please sign in instead.");
      } else {
        alert("Sign up failed: " + error.message);
      }
    });

  // auth.createUserWithEmailAndPassword(email, password)
  //   .catch(alert);
}

// 🔓 Sign In
function signIn() {
  const email = emailInput.value;
  const password = passwordInput.value;
  auth.signInWithEmailAndPassword(email, password)
    .catch(alert);
}

// 🚪 Sign Out
// function signOut() {
//   auth.signOut();
// }
function signOut() {
  auth.signOut()
    .then(() => {
      alert("Signed out successfully.");
      location.reload(); // or use: window.location.href = "index.html";
    })
    .catch((error) => {
      alert("Error signing out: " + error.message);
    });
}

// 🔄 Auth State Listener
auth.onAuthStateChanged((user) => {
  if (user) {
    currentUserId = user.uid;
    document.getElementById("auth-section").style.display = "none";
    bookSection.style.display = "block";
    signoutBtn.style.display = "inline";
    loadBooks();
  } else {
    currentUserId = null;
    document.getElementById("auth-section").style.display = "block";
    bookSection.style.display = "none";
    signoutBtn.style.display = "none";
  }
});

// ➕ Add Book
bookForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const author = document.getElementById("author").value;
  db.ref(`books/${currentUserId}`).push({ title, author });
  bookForm.reset();
});

// 📖 Load Books
// function loadBooks() {
//   db.ref(`books/${currentUserId}`).on("value", (snapshot) => {
//     bookList.innerHTML = "";
//     snapshot.forEach((child) => {
//       const book = child.val();
//       const div = document.createElement("div");
//       div.className = "book";
//       div.innerHTML = `
//         <strong>${book.title}</strong> by ${book.author}
//         <button onclick="editBook('${child.key}', '${book.title}', '${book.author}')">Edit</button>
//         <button onclick="deleteBook('${child.key}')">Delete</button>
//       `;
//       bookList.appendChild(div);
//     });
//   });
// }
function loadBooks() {
  db.ref(`books/${currentUserId}`).on("value", (snapshot) => {
    bookList.innerHTML = "";

    if (!snapshot.exists()) {
      bookList.innerHTML = `
        <div class="col-12">
          <div class="alert alert-info text-center">
            No books to display. Add your first book!
          </div>
        </div>
      `;
      return;
    }

    snapshot.forEach((child) => {
      const book = child.val();
      const div = document.createElement("div");
      div.className = "col-md-6";
      div.innerHTML = `
        <div class="book-card bg-light">
          <h5>${book.title}</h5>
          <p class="text-muted">by ${book.author}</p>
          <button class="btn btn-sm btn-warning me-2" onclick="editBook('${child.key}', '${book.title}', '${book.author}')">Edit</button>
          <button class="btn btn-sm btn-danger" onclick="deleteBook('${child.key}')">Delete</button>
        </div>
      `;
      bookList.appendChild(div);
    });
  });
}

// Delete Book
function deleteBook(id) {
  db.ref(`books/${currentUserId}/${id}`).remove();
}

// ✏️ Edit Book
function editBook(id, title, author) {
  const newTitle = prompt("Edit title:", title);
  const newAuthor = prompt("Edit author:", author);
  if (newTitle && newAuthor) {
    db.ref(`books/${currentUserId}/${id}`).set({
      title: newTitle,
      author: newAuthor
    });
  }
}


const signUpBtn = document.getElementById("signup-btn");
const signInBtn = document.getElementById("signin-btn");

// Function to check input and enable/disable buttons
function toggleAuthButtons() {
  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();
  const isDisabled = email === "" || password === "";

  signUpBtn.disabled = isDisabled;
  signInBtn.disabled = isDisabled;
}

// Run the function whenever input changes
emailInput.addEventListener("input", toggleAuthButtons);
passwordInput.addEventListener("input", toggleAuthButtons);

// Initial check on page load
toggleAuthButtons();

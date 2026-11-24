const STORAGE_KEY = "registrations";

const form = document.getElementById("regForm");
const tableBody = document.getElementById("tableBody");
const emptyMsg = document.getElementById("emptyMsg");
const countEl = document.getElementById("count");
const searchInput = document.getElementById("search");

// ---------- Storage helpers ----------
function getRegistrations() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch (e) {
    return [];
  }
}

function saveRegistrations(list) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
}

// ---------- Validation ----------
function setError(id, message) {
  document.getElementById(id).textContent = message;
}

function validate(data) {
  let valid = true;
  ["nameError", "emailError", "phoneError", "courseError"].forEach(id => setError(id, ""));

  if (data.name.length < 3) {
    setError("nameError", "Name must be at least 3 characters.");
    valid = false;
  }

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
    setError("emailError", "Enter a valid email address.");
    valid = false;
  }

  if (!/^[6-9]\d{9}$/.test(data.phone)) {
    setError("phoneError", "Enter a valid 10-digit mobile number.");
    valid = false;
  }

  if (!data.course) {
    setError("courseError", "Please select an application.");
    valid = false;
  }

  return valid;
}

// ---------- Render ----------
function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function renderList() {
  const query = searchInput.value.trim().toLowerCase();
  const all = getRegistrations();

  const filtered = all.filter(r =>
    r.name.toLowerCase().includes(query) ||
    r.email.toLowerCase().includes(query) ||
    r.course.toLowerCase().includes(query)
  );

  tableBody.innerHTML = filtered.map((r, i) => `
    <tr>
      <td>${i + 1}</td>
      <td>${escapeHtml(r.name)}</td>
      <td>${escapeHtml(r.email)}</td>
      <td>${escapeHtml(r.phone)}</td>
      <td>${escapeHtml(r.course)}</td>
      <td>${escapeHtml(r.date)}</td>
      <td><button class="delete-btn" data-id="${r.id}">Delete</button></td>
    </tr>
  `).join("");

  countEl.textContent = all.length;
  emptyMsg.style.display = filtered.length ? "none" : "block";
  emptyMsg.textContent = all.length ? "No matching results." : "No registrations yet.";
}

// ---------- Events ----------
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value.trim(),
    email: document.getElementById("email").value.trim(),
    phone: document.getElementById("phone").value.trim(),
    course: document.getElementById("course").value
  };

  if (!validate(data)) return;

  const list = getRegistrations();

  if (list.some(r => r.email.toLowerCase() === data.email.toLowerCase())) {
    setError("emailError", "This email is already registered.");
    return;
  }

  list.push({
    id: Date.now(),
    ...data,
    date: new Date().toLocaleDateString("en-IN")
  });

  saveRegistrations(list);
  form.reset();
  renderList();
});

tableBody.addEventListener("click", function (e) {
  if (!e.target.classList.contains("delete-btn")) return;

  const id = Number(e.target.dataset.id);
  if (!confirm("Delete this registration?")) return;

  saveRegistrations(getRegistrations().filter(r => r.id !== id));
  renderList();
});

searchInput.addEventListener("input", renderList);

// Initial load
renderList();
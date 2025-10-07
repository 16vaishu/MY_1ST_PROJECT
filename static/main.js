const API_BASE = window.location.origin;

async function loadTopics() {
  const list = document.getElementById("topics-list");
  list.innerHTML = "<li class='list-group-item'>Loading...</li>";
  try {
    const res = await fetch(`${API_BASE}/topics/`);
    const data = await res.json();
    list.innerHTML = "";
    data.forEach(t => {
      const li = document.createElement("li");
      li.className = "list-group-item";
      li.textContent = t.name;
      list.appendChild(li);
    });
  } catch (err) {
    console.error(err);
    list.innerHTML = "<li class='list-group-item text-danger'>Error loading topics</li>";
  }
}

document.getElementById("topic-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("topic-name").value.trim();
  if (!name) return;
  await fetch(`${API_BASE}/topics/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  });
  document.getElementById("topic-name").value = "";
  loadTopics();
});

loadTopics();

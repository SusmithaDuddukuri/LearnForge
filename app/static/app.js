const $ = (s, root=document) => root.querySelector(s);
const $$ = (s, root=document) => [...root.querySelectorAll(s)];
let courses = [], quizItems = [], quizIndex = 0, quizAnswers = {}, quizChecked = false;
let bookmarkedIds = new Set();
let topRatedOnly = false;
let timerInterval = null, timerSeconds = 25 * 60, timerRunning = false;

const courseIcons = {
  Development: "</>",
  Data: "◒",
  Design: "✳",
  Technology: "⌘",
  "Artificial Intelligence": "🤖",
  Cybersecurity: "🛡️"
};

const initials = name => name.split(" ").map(part=>part[0]).slice(0,2).join("");

function toast(message){
  const el = $("#toast");
  el.textContent = message;
  el.classList.add("show");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => el.classList.remove("show"), 2800);
}

async function api(url, options={}){
  const response = await fetch(url, {headers: {"Content-Type": "application/json"}, ...options});
  const data = await response.json();
  if(!response.ok) throw new Error(data.error || "Something went wrong");
  return data;
}

function goTo(page){
  const target = $("#page-" + page);
  if(!target) return;
  $$(".page").forEach(p => p.classList.remove("active-page"));
  target.classList.add("active-page");
  $$(".nav-item").forEach(b => b.classList.toggle("active", b.dataset.page === page));
  const label = ({
    dashboard: "Overview",
    catalog: "Explore courses",
    "my-learning": "My learning",
    practice: "Quick practice",
    achievements: "Achievements",
    schedule: "Study planner"
  })[page] || "Overview";
  $("#crumbCurrent").textContent = label;
  $("#sidebar").classList.remove("open");
  window.scrollTo({top: 0, behavior: "smooth"});
  if(page === "catalog") renderCatalog();
  if(page === "my-learning") renderMyLearning();
  if(page === "practice") loadQuiz();
}

function artClass(c){
  if(c.color) return c.color;
  return ["violet", "blue", "orange", "green"][(c.id - 1) % 4];
}

function courseCard(c){
  const isSaved = bookmarkedIds.has(c.id);
  return `<article class="course-card">
    <div class="course-art ${artClass(c)}">
      <span class="art-tag">${c.level.toUpperCase()}</span>
      <div class="card-header-actions">
        <button class="card-btn-icon bookmark-btn ${isSaved ? 'saved' : ''}" data-bookmark="${c.id}" title="${isSaved ? 'Remove bookmark' : 'Save course'}">${isSaved ? '★' : '☆'}</button>
      </div>
      <span class="art-glyph">${courseIcons[c.category] || "✦"}</span>
    </div>
    <div class="course-body">
      <div class="course-meta">
        <span class="course-category">${c.category}</span>
        <span class="course-rating">★ ${c.rating.toFixed(2)}</span>
      </div>
      <h3>${c.title}</h3>
      <p class="course-desc">${c.description}</p>
      <div class="course-instructor">
        <span class="instructor-avatar">${initials(c.instructor)}</span>
        <span>${c.instructor}</span>
      </div>
      <div class="course-card-bottom">
        <span class="course-duration">◷ ${c.duration} · ${c.lessons} lessons</span>
        <button class="course-action" data-course="${c.id}">${c.progress > 0 ? "Continue" : "View course"} →</button>
      </div>
    </div>
  </article>`;
}

function renderProgress(c){
  return `<div class="progress-course">
    <div class="course-mini-icon ${artClass(c)}">${courseIcons[c.category] || "✦"}</div>
    <div class="progress-info">
      <strong>${c.title}</strong>
      <small>${c.progress >= 100 ? "Course completed" : `${c.progress}% complete`} · ${c.lessons} lessons</small>
      <div class="progress-track"><span style="width:${c.progress}%"></span></div>
    </div>
    <span class="progress-percent">${c.progress}%</span>
  </div>`;
}

async function syncBookmarks(){
  try {
    const res = await api("/api/bookmarks");
    bookmarkedIds = new Set((res.items || []).map(c => c.id));
  } catch(e) {
    // fallback
  }
}

async function toggleBookmark(courseId){
  const id = Number(courseId);
  const willSave = !bookmarkedIds.has(id);
  try {
    await api(`/api/bookmarks/${id}`, {
      method: "PUT",
      body: JSON.stringify({saved: willSave})
    });
    if(willSave) bookmarkedIds.add(id);
    else bookmarkedIds.delete(id);
    toast(willSave ? "Course saved to bookmarks!" : "Bookmark removed.");
    $$(`[data-bookmark="${id}"]`).forEach(btn => {
      btn.classList.toggle("saved", willSave);
      btn.textContent = willSave ? "★" : "☆";
      btn.title = willSave ? "Remove bookmark" : "Save course";
    });
  } catch(e) {
    toast(e.message);
  }
}

async function loadDashboard(){
  await syncBookmarks();
  try {
    const data = await api("/api/dashboard");
    $("#statEnrolled").textContent = data.stats.enrolled;
    $("#statCompleted").textContent = data.stats.completed;
    $("#statHours").textContent = data.stats.learning_hours;
    $("#progressCourses").innerHTML = data.courses.length
      ? data.courses.map(renderProgress).join("")
      : '<p class="subheading">No courses started yet. Explore the catalog to begin.</p>';
  } catch(e) {
    $("#progressCourses").innerHTML = '<p class="subheading">Dashboard data is unavailable. Please refresh.</p>';
  }
  try {
    courses = (await api("/api/courses")).items;
    $("#recommendedCourses").innerHTML = courses
      .filter(c => c.progress === 0 || c.progress < 50)
      .slice(0, 3)
      .map(courseCard)
      .join("");
  } catch(e) {
    $("#recommendedCourses").innerHTML = '<p>Courses could not be loaded.</p>';
  }
}

async function renderCatalog(){
  try {
    const params = new URLSearchParams({
      q: $("#courseSearch").value,
      category: $("#categoryFilter").value,
      level: $("#levelFilter").value
    });
    const data = await api("/api/courses?" + params);
    let items = data.items;
    if(topRatedOnly){
      items = items.filter(c => c.rating >= 4.9);
    }
    $("#catalogCourses").innerHTML = items.map(courseCard).join("");
    $("#catalogCount").textContent = `${items.length} course${items.length === 1 ? "" : "s"}`;
    $("#emptyCourses").classList.toggle("hidden", items.length !== 0);

    const currentCat = $("#categoryFilter").value;
    $$(".topic-pill").forEach(pill => {
      pill.classList.toggle("active", pill.dataset.category === currentCat);
    });
  } catch(e) {
    toast("Couldn't load the course catalog.");
  }
}

async function renderMyLearning(){
  try {
    const data = await api("/api/courses");
    const enrolled = data.items.filter(c => c.progress > 0);
    $("#learningSummary").innerHTML = `
      <div class="learning-stat"><strong>${enrolled.length}</strong><span>Courses in progress</span></div>
      <div class="learning-stat"><strong>${enrolled.filter(c => c.progress === 100).length}</strong><span>Courses completed</span></div>
      <div class="learning-stat"><strong>${enrolled.reduce((sum, c) => sum + c.progress, 0)}%</strong><span>Combined progress points</span></div>
    `;
    $("#myCourses").innerHTML = (enrolled.length ? enrolled : data.items).map(courseCard).join("");
  } catch(e) {
    toast("Couldn't load your learning.");
  }
}

function openCourse(id){
  const c = courses.find(x => x.id === Number(id));
  if(!c){
    api(`/api/courses/${id}`).then(showCourse).catch(() => toast("Course not found"));
    return;
  }
  showCourse(c);
}

function showCourse(c){
  const isSaved = bookmarkedIds.has(c.id);
  $("#modalBody").innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center">
      <div class="eyebrow">${c.category.toUpperCase()} · ${c.level.toUpperCase()}</div>
      <button class="card-btn-icon bookmark-btn ${isSaved ? 'saved' : ''}" id="modalBookmarkBtn" title="Bookmark">${isSaved ? '★' : '☆'}</button>
    </div>
    <h2 id="modalTitle">${c.title}</h2>
    <p>${c.description}</p>
    <div class="detail-meta">
      <span>★ ${c.rating} rating</span>
      <span>◷ ${c.duration}</span>
      <span>${c.lessons} lessons</span>
      <span>By ${c.instructor}</span>
    </div>
    <div style="display:flex;gap:8px;margin:12px 0 16px">
      <button class="outline-btn" id="modalAiTipBtn" style="padding:6px 12px;font-size:10px">💡 Quick Study Tip</button>
      <button class="outline-btn" id="modalCopyBtn" style="padding:6px 12px;font-size:10px">📋 Copy Syllabus</button>
    </div>
    <div id="modalTipContainer" class="hidden" style="background:#f7f4ff;border:1px solid #e1d8ff;border-radius:8px;padding:12px;font-size:11px;color:#524580;margin-bottom:14px"></div>
    <h3 style="font:700 13px Manrope;margin:18px 0 10px">What you'll learn</h3>
    <p>${c.skills.join(" · ")}</p>
    <h3 style="font:700 13px Manrope;margin:18px 0 10px">Course outline</h3>
    <div class="module-list">
      ${c.modules.map((m, i) => `
        <div class="module-row">
          <span class="module-num">${String(i + 1).padStart(2, "0")}</span>
          <div><strong>${m.title}</strong><small>${m.duration}</small></div>
        </div>
      `).join("")}
    </div>
    <div class="modal-actions">
      <button class="outline-btn" id="modalCloseSecondary">Close</button>
      <button class="primary-btn" id="startCourseBtn">${c.progress > 0 ? "Continue course" : "Start learning"} →</button>
    </div>
  `;
  $("#modalBackdrop").classList.remove("hidden");
  $("#modalCloseSecondary").onclick = closeModal;
  
  $("#modalBookmarkBtn").onclick = () => {
    toggleBookmark(c.id);
    const updatedSaved = bookmarkedIds.has(c.id);
    $("#modalBookmarkBtn").textContent = updatedSaved ? "★" : "☆";
    $("#modalBookmarkBtn").classList.toggle("saved", updatedSaved);
  };

  $("#modalAiTipBtn").onclick = () => {
    const tipBox = $("#modalTipContainer");
    tipBox.classList.toggle("hidden");
    tipBox.innerHTML = `<strong>💡 Pro Study Tip:</strong> Practice active recall by explaining each module concept to yourself in 2 sentences before taking the chapter quiz!`;
  };

  $("#modalCopyBtn").onclick = () => {
    const text = `${c.title} (${c.category})\nModules:\n` + c.modules.map((m, i) => `${i+1}. ${m.title} (${m.duration})`).join("\n");
    navigator.clipboard.writeText(text).then(() => {
      toast("Syllabus copied to clipboard!");
    }).catch(() => {
      toast("Copied syllabus summary.");
    });
  };

  $("#startCourseBtn").onclick = async () => {
    try {
      const next = Math.min(100, Math.max(c.progress, 15));
      await api("/api/progress", {
        method: "POST",
        body: JSON.stringify({course_id: c.id, progress: next})
      });
      c.progress = next;
      closeModal();
      await loadDashboard();
      toast(`${c.title} progress updated to ${next}%`);
      goTo("my-learning");
    } catch(e) {
      toast(e.message);
    }
  };
}

function closeModal(){
  $("#modalBackdrop").classList.add("hidden");
}

function pickRandomCourse(){
  if(!courses.length) return;
  const rand = courses[Math.floor(Math.random() * courses.length)];
  toast(`🎲 Selected "${rand.title}" for you!`);
  openCourse(rand.id);
}

function togglePomodoro(){
  const btn = $("#pomodoroBtn");
  const display = $("#timerDisplay");
  if(timerRunning){
    clearInterval(timerInterval);
    timerRunning = false;
    btn.classList.remove("active");
    display.textContent = `Paused (${formatTime(timerSeconds)})`;
    toast("Focus timer paused.");
  } else {
    timerRunning = true;
    btn.classList.add("active");
    toast("⏱️ 25-minute focus session started. Happy learning!");
    timerInterval = setInterval(() => {
      if(timerSeconds > 0){
        timerSeconds--;
        display.textContent = formatTime(timerSeconds);
      } else {
        clearInterval(timerInterval);
        timerRunning = false;
        btn.classList.remove("active");
        timerSeconds = 25 * 60;
        display.textContent = "Focus 25m";
        toast("🎉 25-minute focus session complete! Take a well-deserved 5-minute break.");
      }
    }, 1000);
  }
}

function formatTime(totalSec){
  const m = Math.floor(totalSec / 60);
  const s = totalSec % 60;
  return `${m}:${String(s).padStart(2, "0")}`;
}

function handleStreakCheckIn(){
  let currentStreak = parseInt(localStorage.getItem("lf_streak") || "7", 10);
  const lastCheckIn = localStorage.getItem("lf_streak_date");
  const todayKey = new Date().toDateString();

  if(lastCheckIn === todayKey){
    toast("🔥 You've already checked in today! Streak safe.");
    return;
  }
  currentStreak += 1;
  localStorage.setItem("lf_streak", currentStreak);
  localStorage.setItem("lf_streak_date", todayKey);
  $("#streakCount").textContent = currentStreak;
  if($("#heroStreakBadge")) $("#heroStreakBadge").textContent = `✦ ${currentStreak} day streak`;
  $("#streakBtn").classList.add("checked-in");
  toast(`🔥 Streak claimed! You're on a ${currentStreak}-day streak. Keep it going!`);
}

async function loadQuiz(){
  try {
    quizItems = await api("/api/quiz");
    quizIndex = 0;
    quizAnswers = {};
    quizChecked = false;
    $("#quizResult").classList.add("hidden");
    $("#quizForm").classList.remove("hidden");
    renderQuestion();
  } catch(e) {
    toast("Practice questions couldn't be loaded.");
  }
}

function renderQuestion(){
  const q = quizItems[quizIndex];
  if(!q) return;
  $("#quizStep").textContent = `QUESTION ${quizIndex + 1} OF ${quizItems.length}`;
  $("#quizPercent").textContent = `${Math.round(quizIndex / quizItems.length * 100)}% complete`;
  $("#quizTrack").style.width = `${quizIndex / quizItems.length * 100}%`;
  $("#quizBack").disabled = quizIndex === 0;
  $("#quizNext").textContent = quizChecked ? (quizIndex === quizItems.length - 1 ? "See results →" : "Next question →") : "Check answer →";
  $("#quizContent").innerHTML = `
    <h2 class="quiz-question">${q.question}</h2>
    <div class="quiz-options">
      ${q.options.map((option, i) => `
        <label class="quiz-option ${quizAnswers[q.id] === i ? "selected" : ""}">
          <span class="option-letter">${String.fromCharCode(65 + i)}</span>
          <span>${option}</span>
          <input type="radio" name="quizAnswer" value="${i}" ${quizAnswers[q.id] === i ? "checked" : ""} style="margin-left:auto;accent-color:#7358e8">
        </label>
      `).join("")}
    </div>
    ${quizChecked ? `<div class="quiz-feedback ${quizAnswers[q.id] === q.answer ? "correct" : "incorrect"}">${quizAnswers[q.id] === q.answer ? "Correct! " : "Not quite. "}${q.explanation}</div>` : ""}
  `;
  $$(".quiz-option", $("#quizContent")).forEach((label, i) => label.addEventListener("click", () => {
    if(quizChecked) return;
    quizAnswers[q.id] = i;
    renderQuestion();
  }));
}

async function submitQuiz(){
  try {
    const answers = {};
    quizItems.forEach(q => {
      if(quizAnswers[q.id] !== undefined) answers[q.id] = quizAnswers[q.id];
    });
    const result = await api("/api/quiz/submit", {method: "POST", body: JSON.stringify({answers})});
    $("#quizForm").classList.add("hidden");
    $("#quizResult").classList.remove("hidden");
    $("#quizResult").innerHTML = `
      <div class="score">${result.percent}%</div>
      <h2>${result.percent === 100 ? "Brilliant work!" : result.percent >= 60 ? "Nice progress!" : "Keep practicing!"}</h2>
      <p>You got ${result.score} out of ${result.total} correct. Every attempt helps the ideas stick.</p>
      <button class="primary-btn" id="tryAgainBtn">Try again →</button>
    `;
    $("#quizResult").querySelector("button").onclick = loadQuiz;
    $("#quizTrack").style.width = "100%";
    $("#quizPercent").textContent = "100% complete";
  } catch(e) {
    toast(e.message);
  }
}

$$("[data-page]").forEach(el => el.addEventListener("click", () => goTo(el.dataset.page)));

document.addEventListener("click", e => {
  const bookmarkBtn = e.target.closest("[data-bookmark]");
  if(bookmarkBtn){
    e.stopPropagation();
    toggleBookmark(bookmarkBtn.dataset.bookmark);
    return;
  }
  const btn = e.target.closest("[data-course]");
  if(btn) openCourse(btn.dataset.course);
});

$$(".topic-pill").forEach(pill => {
  pill.addEventListener("click", () => {
    const cat = pill.dataset.category;
    $("#categoryFilter").value = cat;
    renderCatalog();
  });
});

$("#courseSearch").addEventListener("input", () => renderCatalog());
$("#categoryFilter").addEventListener("change", renderCatalog);
$("#levelFilter").addEventListener("change", renderCatalog);

if($("#randomCourseBtn")) $("#randomCourseBtn").addEventListener("click", pickRandomCourse);
if($("#heroSurpriseBtn")) $("#heroSurpriseBtn").addEventListener("click", pickRandomCourse);

if($("#topRatedBtn")){
  $("#topRatedBtn").addEventListener("click", () => {
    topRatedOnly = !topRatedOnly;
    $("#topRatedBtn").classList.toggle("active", topRatedOnly);
    toast(topRatedOnly ? "Showing 4.9+ rated courses only." : "Showing all ratings.");
    renderCatalog();
  });
}

if($("#streakBtn")) $("#streakBtn").addEventListener("click", handleStreakCheckIn);
if($("#pomodoroBtn")) $("#pomodoroBtn").addEventListener("click", togglePomodoro);

$("#clearFilters").addEventListener("click", () => {
  $("#courseSearch").value = "";
  $("#categoryFilter").value = "All";
  $("#levelFilter").value = "All";
  topRatedOnly = false;
  if($("#topRatedBtn")) $("#topRatedBtn").classList.remove("active");
  renderCatalog();
});

$("#searchFocus").addEventListener("click", () => {
  goTo("catalog");
  setTimeout(() => $("#courseSearch").focus(), 100);
});

document.addEventListener("keydown", e => {
  if(e.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)){
    e.preventDefault();
    $("#searchFocus").click();
  }
  if(e.key === "Escape") closeModal();
});

$("#continueBtn").addEventListener("click", () => openCourse(1));
$("#modalClose").addEventListener("click", closeModal);
$("#modalBackdrop").addEventListener("click", e => {
  if(e.target === $("#modalBackdrop")) closeModal();
});

$("#notificationsBtn").addEventListener("click", () => toast("You're all caught up — keep learning!"));
$("#profileBtn").addEventListener("click", () => toast("Profile settings are a demo feature."));
$("#aboutLink").addEventListener("click", e => {
  e.preventDefault();
  $("#modalBody").innerHTML = '<h2 id="modalTitle">About LearnForge</h2><p>LearnForge is a learning platform prototype designed to make practical, self-paced education feel clear and motivating.</p><p>Explore diverse topics from Artificial Intelligence, Cybersecurity, Modern Web Dev to DevOps and UX Design.</p><button class="primary-btn" id="aboutClose">Sounds good</button>';
  $("#modalBackdrop").classList.remove("hidden");
  $("#aboutClose").onclick = closeModal;
});

$("#menuBtn").addEventListener("click", () => $("#sidebar").classList.toggle("open"));

$("#quizNext").addEventListener("click", () => {
  const q = quizItems[quizIndex];
  if(!quizChecked){
    if(quizAnswers[q.id] === undefined){
      toast("Choose an answer first.");
      return;
    }
    quizChecked = true;
    renderQuestion();
    return;
  }
  if(quizIndex < quizItems.length - 1){
    quizIndex++;
    quizChecked = false;
    renderQuestion();
  } else submitQuiz();
});

$("#quizBack").addEventListener("click", () => {
  if(quizIndex > 0){
    quizIndex--;
    quizChecked = false;
    renderQuestion();
  }
});

$("#addStudyBtn").addEventListener("click", () => {
  const day = prompt("Which day would you like to study? (e.g. Thursday)");
  if(!day || !day.trim()) return;
  const topic = prompt("What would you like to study?", "Generative AI & Prompt Engineering");
  if(!topic || !topic.trim()) return;
  const item = document.createElement("div");
  item.className = "schedule-item";
  const dayBadge = document.createElement("span");
  dayBadge.className = "schedule-day";
  dayBadge.textContent = day.trim().slice(0, 3).toUpperCase();
  const details = document.createElement("div");
  const title = document.createElement("strong");
  title.textContent = topic.trim();
  const desc = document.createElement("p");
  desc.textContent = "Personal study session · 20 min";
  details.append(title, desc);
  const status = document.createElement("span");
  status.className = "schedule-status";
  status.textContent = "Planned";
  item.append(dayBadge, details, status);
  $("#scheduleList").append(item);
  toast("Study session added to your weekly rhythm.");
});

$("#todayDate").textContent = new Intl.DateTimeFormat(undefined, {weekday: "short", month: "short", day: "numeric"}).format(new Date());

const storedStreak = localStorage.getItem("lf_streak") || "7";
if($("#streakCount")) $("#streakCount").textContent = storedStreak;

loadDashboard();

let currentMediaIndex = 0;
let currentMediaList = [];
let autoPlayInterval = null;

function ensureModal() {
  if (document.getElementById("mediaModal")) return;

  const modal = document.createElement("div");
  modal.id = "mediaModal";
  modal.className = "media-modal";
  modal.innerHTML = `
    <div class="media-modal-content">
      <button class="media-close" onclick="closeMediaModal()">×</button>
      <button class="media-nav prev" onclick="changeMedia(-1)">‹</button>
      <div id="mediaContainer" class="media-container"></div>
      <button class="media-nav next" onclick="changeMedia(1)">›</button>
      <div class="media-controls">
        <button onclick="toggleAutoPlay()">Auto Play</button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);

  modal.addEventListener("click", function (e) {
    if (e.target.id === "mediaModal") {
      closeMediaModal();
    }
  });
}

function openMediaModal(index, mediaList) {
  ensureModal();
  currentMediaIndex = index;
  currentMediaList = mediaList;
  document.getElementById("mediaModal").style.display = "flex";
  renderMedia();
}

function renderMedia() {
  const container = document.getElementById("mediaContainer");
  const item = currentMediaList[currentMediaIndex];
  if (!container || !item) return;

  if (item.type === "video") {
    container.innerHTML = `
      <video controls autoplay class="modal-media">
        <source src="${item.src}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    `;
  } else {
    container.innerHTML = `<img src="${item.src}" class="modal-media" alt="">`;
  }
}

function changeMedia(step) {
  currentMediaIndex += step;
  if (currentMediaIndex < 0) currentMediaIndex = currentMediaList.length - 1;
  if (currentMediaIndex >= currentMediaList.length) currentMediaIndex = 0;
  renderMedia();
}

function closeMediaModal() {
  const modal = document.getElementById("mediaModal");
  if (modal) modal.style.display = "none";
  stopAutoPlay();
}

function toggleAutoPlay() {
  if (autoPlayInterval) {
    stopAutoPlay();
  } else {
    autoPlayInterval = setInterval(() => {
      changeMedia(1);
    }, 2500);
  }
}

function stopAutoPlay() {
  if (autoPlayInterval) {
    clearInterval(autoPlayInterval);
    autoPlayInterval = null;
  }
}

document.addEventListener("keydown", function(e) {
  const modal = document.getElementById("mediaModal");
  if (!modal || modal.style.display !== "flex") return;

  if (e.key === "ArrowRight") changeMedia(1);
  if (e.key === "ArrowLeft") changeMedia(-1);
  if (e.key === "Escape") closeMediaModal();
});

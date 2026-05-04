document.addEventListener("DOMContentLoaded", function () {
  let modal = document.getElementById("certModal");

  if (!modal) {
    modal = document.createElement("div");
    modal.id = "certModal";
    modal.className = "cert-modal";
    document.body.appendChild(modal);
  }

  modal.innerHTML = `
    <button class="cert-modal-close" type="button">×</button>

    <div class="cert-modal-toolbar">
      <button type="button" id="zoomOutBtn">−</button>
      <button type="button" id="zoomResetBtn">Reset</button>
      <button type="button" id="zoomInBtn">+</button>
    </div>

    <div class="cert-modal-scroll">
      <img id="certModalImg" src="" alt="Certificate Preview">
    </div>
  `;

  const modalImg = document.getElementById("certModalImg");
  const closeBtn = modal.querySelector(".cert-modal-close");
  const zoomInBtn = document.getElementById("zoomInBtn");
  const zoomOutBtn = document.getElementById("zoomOutBtn");
  const zoomResetBtn = document.getElementById("zoomResetBtn");

  let zoom = 1;

  function openPreview(src) {
    zoom = 1;
    modalImg.src = src;
    modalImg.style.transform = "scale(1)";
    modal.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closePreview() {
    modal.classList.remove("active");
    modalImg.src = "";
    document.body.style.overflow = "";
  }

  function setZoom(value) {
    zoom = Math.max(0.5, Math.min(value, 4));
    modalImg.style.transform = `scale(${zoom})`;
  }

  document.addEventListener("click", function (e) {
    const card = e.target.closest("[data-preview]");

    if (card) {
      e.preventDefault();
      openPreview(card.getAttribute("data-preview"));
      return;
    }

    if (e.target === modal || e.target === closeBtn) {
      closePreview();
    }
  });

  zoomInBtn.addEventListener("click", function () {
    setZoom(zoom + 0.25);
  });

  zoomOutBtn.addEventListener("click", function () {
    setZoom(zoom - 0.25);
  });

  zoomResetBtn.addEventListener("click", function () {
    setZoom(1);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closePreview();
    if (e.key === "+") setZoom(zoom + 0.25);
    if (e.key === "-") setZoom(zoom - 0.25);
  });
});
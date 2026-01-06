document.querySelectorAll(".tab-button").forEach((button) => {
    button.addEventListener("click", () => {
      // Aktif tab-button'u kaldır
      document.querySelector(".tab-button.active").classList.remove("active");
      // Tıklanan butona aktif sınıfı ekle
      button.classList.add("active");
  
      // Aktif tab-content'i kaldır
      document.querySelector(".tab-content.active").classList.remove("active");
      // İlgili tab-content'i aktif yap
      const tabId = button.getAttribute("data-tab");
      document.getElementById(tabId).classList.add("active");
    });
  });

//   document.addEventListener("DOMContentLoaded", () => {
//     const videos = document.querySelectorAll(".video-player");

//     videos.forEach((video) => {
//         video.addEventListener("play", () => {
//             videos.forEach((otherVideo) => {
//                 if (otherVideo !== video) {
//                     // Video için durdurma işlemi
//                     if (otherVideo.tagName === "VIDEO") {
//                         otherVideo.pause();
//                     } else if (otherVideo.tagName === "IFRAME") {
//                         const iframeSrc = otherVideo.src;
//                         otherVideo.src = ""; // YouTube iframe'i resetle
//                         otherVideo.src = iframeSrc; // Yeniden yükle
//                     }
//                 }
//             });
//         });
//     });
// });

  


  let currentSlideIndex = 0;

  function openSlider(clickedImage) {
      const slider = document.getElementById('slider');
      const galleryItems = document.querySelectorAll('.image-gallery-item img');
  
      // Open the slider
      slider.classList.remove('hidden');
  
      // Load the selected image
      currentSlideIndex = parseInt(clickedImage.getAttribute('data-index'));
      updateSlider(galleryItems[currentSlideIndex]);
  
      // Highlight the current thumbnail
      updateThumbnails();
  }
  
  function closeSlider() {
      const slider = document.getElementById('slider');
      slider.classList.add('hidden');
  }
  
  function changeSlide(direction) {
    const galleryItems = document.querySelectorAll('.image-gallery-item img');
    const totalSlides = galleryItems.length;

    // Yeni slide index'ini hesapla
    currentSlideIndex = (currentSlideIndex + direction + totalSlides) % totalSlides;
    updateSlider(galleryItems[currentSlideIndex]);
}
  function jumpToSlide(thumbnail) {
      const galleryItems = document.querySelectorAll('.image-gallery-item img');
      currentSlideIndex = parseInt(thumbnail.getAttribute('data-index'));
      updateSlider(galleryItems[currentSlideIndex]);
  
      // Highlight the current thumbnail
      updateThumbnails();
  }
  
  function updateSlider(image) {
    const sliderImage = document.getElementById('slider-image');
    const sliderCaption = document.getElementById('slider-caption');

    // Güncel resmi ve altyazıyı yükle
    sliderImage.src = image.src;
    sliderImage.alt = image.alt;
    sliderCaption.textContent = image.getAttribute('data-caption') || '';

    // Thumbnail'leri güncelle
    document.querySelectorAll('.thumbnail').forEach((thumb) => {
        thumb.classList.remove('active');
    });
    document.querySelector(`.thumbnail[data-index="${image.getAttribute('data-index')}"]`).classList.add('active');
}
function selectThumbnail(thumbnail) {
  const galleryItems = document.querySelectorAll('.image-gallery-item img');
  currentSlideIndex = parseInt(thumbnail.getAttribute('data-index'));
  updateSlider(galleryItems[currentSlideIndex]);
}
  
  function updateThumbnails() {
      const thumbnails = document.querySelectorAll('.thumbnail');
      thumbnails.forEach((thumbnail, index) => {
          if (index === currentSlideIndex) {
              thumbnail.classList.add('active');
          } else {
              thumbnail.classList.remove('active');
          }
      });
  }
  
  function scrollThumbnails(direction) {
    const thumbnailsWrapper = document.querySelector('.thumbnails-wrapper');
    const thumbnails = document.querySelector('.thumbnails');
    const thumbnailWidth = document.querySelector('.thumbnail').offsetWidth + 10; // Thumbnail genişliği + aralık
    const visibleThumbnails = Math.floor(thumbnailsWrapper.offsetWidth / thumbnailWidth);

    // Şu anki kaydırma durumunu hesapla
    const currentTransform = getComputedStyle(thumbnails).transform;
    const currentTranslateX = currentTransform !== 'none' ? parseFloat(currentTransform.split(',')[4]) : 0;

    // Yeni kaydırma değeri
    const newTranslateX = currentTranslateX + direction * thumbnailWidth * visibleThumbnails;

    // Maksimum kaydırmayı kontrol et
    const maxScroll = -(thumbnails.scrollWidth - thumbnailsWrapper.offsetWidth);
    thumbnails.style.transform = `translateX(${Math.min(0, Math.max(newTranslateX, maxScroll))}px)`;
}


  document.getElementById('slider').addEventListener('click', (e) => {
      if (e.target === e.currentTarget) {
          closeSlider();
      }
  });
  
// Create the observer
const observer = new IntersectionObserver(entries => {
  // Loop over the entries
  entries.forEach(entry => {
    // If the element is visible
    if (entry.isIntersecting) {
      // Add the animation class
      entry.target.classList.add('start');
    }
  });
});


// Tell the observer which elements to track
observer.observe(document.querySelector('.landing-page-how-it-works-section'));
// Left side pop-ups
observer.observe(document.querySelector('.popup-left-one'));
observer.observe(document.querySelector('.popup-left-two'));
observer.observe(document.querySelector('.popup-left-three'));
observer.observe(document.querySelector('.popup-left-four'));
// Right side pop-ups
observer.observe(document.querySelector('.popup-right-one'));
observer.observe(document.querySelector('.popup-right-two'));
observer.observe(document.querySelector('.popup-right-three'));
observer.observe(document.querySelector('.popup-right-four'));
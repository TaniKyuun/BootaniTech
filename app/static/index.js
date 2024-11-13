// Smooth scrolling using jQuery easing
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Change header background color on scroll
const header = document.getElementById("myHeader");
window.addEventListener("scroll", () => {
  if (window.scrollY > 100) {
    header.style.backgroundColor = "#1c5d34";
  } else {
    header.style.backgroundColor = "rgba(174, 246, 148, 0.15)";
  }
});

// Add click event to close buttons
const closebtns = document.getElementsByClassName("close");
for (let i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function () {
    this.parentElement.style.display = "none";
  });
}

// Toggle profile selection on profile picture click
var profilePicture = document.getElementById("profile-picture");
var profileSelection = document.getElementById("profile-selection");

if (profilePicture && profileSelection) {
  profilePicture.addEventListener("click", function () {
    if (
      profileSelection.style.display === "none" ||
      profileSelection.style.display === ""
    ) {
      profileSelection.style.display = "block";
    } else {
      profileSelection.style.display = "none";
    }
  });
}

var originalDisplay; // Declare a variable to store the original display value

function toggleNavbar() {
  var x = document.getElementById("myTopnav");
  var hamburger = document.querySelector(".hamburger-menu");
  var navList = document.querySelector("#myTopnav ul"); // Select the unordered list within the navbar
  var navItemContainer = document.querySelector(".nav-item-container"); // Select the nav-item-container

  if (x.className === "nav") {
    x.className += " responsive";
    hamburger.classList.add("open"); // Add open class
    navItemContainer.classList.add("open"); // Add open class to nav-item-container
    originalDisplay = navList.style.display; // Store the original display value
    navList.style.display = "block"; // Display the unordered list
  } else {
    x.className = "nav";
    hamburger.classList.remove("open"); // Remove open class
    navItemContainer.classList.remove("open"); // Remove open class from nav-item-container
    navList.style.display = originalDisplay; // Restore the original display value
  }
}
window.addEventListener("resize", function () {
  var x = document.getElementById("myTopnav");
  var navList = document.querySelector("#myTopnav ul");
  var hamburger = document.querySelector(".hamburger-menu");
  var navItemContainer = document.querySelector(".nav-item-container");

  if (window.innerWidth >= 1024) {
    navList.style.display = "flex";
    hamburger.classList.remove("open"); // Remove open class from hamburger menu
    navItemContainer.classList.remove("open"); // Remove open class from nav-item-container
    x.className = "nav"; // Reset the navbar class
  } else if (x.className === "nav") {
    navList.style.display = originalDisplay;
  }
});

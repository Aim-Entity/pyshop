let logo = document.querySelector(".name")
let join_now = document.querySelector(".join")
let ul = document.querySelector(".base-ul")
let hamburger = document.querySelector(".hamburger")

hamburger.addEventListener("click", e => {
  anime({
    target: ul,
    translateY: ["0px", "200px"],
    duration: 500,
  })
})

window.addEventListener("DOMContentLoaded", e => {
  anime({
    targets: logo,
    opacity: [0, 1],
    easing: "easeInSine",
    duration: 750
  })
});

join_now.addEventListener("mouseover", e => {
  anime({
    targets: join_now,
    backgroundColor: ["rgb(216,39,150)", "rgb(39,216,105)"],
    easing: "easeOutExpo",
    duration: 750
  })
})

join_now.addEventListener("mouseout", e => {
  anime({
    targets: join_now,
    backgroundColor: ["rgb(39,216,105)", "rgb(216,39,150)"],
    easing: "easeOutExpo",
    duration: 750
  })
})
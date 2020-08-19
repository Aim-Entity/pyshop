let logo = document.querySelector(".name")
let join_now = document.querySelector(".join")

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
let categories = document.querySelectorAll(".cat")

for (i = 1; i < categories.length; i++) {
  categories[i].addEventListener("mouseover", e => {
    anime({
      targets: e.target,
      background: ["rgb(255,255,255)", "rgb(216,39,150)"],
      borderColor: ["rgb(255,255,255)", "rgb(216,39,150)"],
    })
  })

  categories[i].addEventListener("mouseout", e => {
    anime({
      targets: e.target,
      background: ["rgb(216,39,150)", "rgb(255,255,255)"],
      borderColor: ["rgb(216,39,150)", "rgb(0,0,0)"],
    })
  })
}
let forms = document.querySelectorAll(".form-control")
let btn = document.querySelector(".submit")

for (let i = 0; i < forms.length; i++) {
  forms[i].addEventListener("focus", e => {
    anime({
      targets: e.target,
      borderBottomColor: ["rgb(0, 0, 0)", "rgb(76,106,133)"],
      borderBottomWidth: ["0.5px", "7px"],
      duration: 1200
    })
  })

  forms[i].addEventListener("blur", e => {
    anime({
      targets: e.target,
      borderBottomWidth: ["7px", "0.5px"],
      borderBottomColor: ["rgb(76,106,133)", "rgb(0, 0, 0)"],
      duration: 1200
    })
  })
}

btn.addEventListener("mouseover", e => {
  anime({
    targets: btn,
    backgroundColor: ["rgb(255,255,255)", "rgb(216, 39, 150)"],
    color: ["rgb(216,39,150)", "rgb(255,255,255)"],
    easing: "easeOutQuad",
    duration: 500
  })
})

btn.addEventListener("mouseout", e => {
  anime({
    targets: btn,
    backgroundColor: ["rgb(216, 39, 150)", "rgb(255,255,255)"],
    color: ["rgb(255,255,255)", "rgb(216,39,150)"],
    easing: "easeOutQuad",
    duration: 500
  })
})
const express = require("express")
const app = express()

app.set("view engine", "ejs")
app.set("views", "view")

app.get("/", (req, res) => {
    res.render("index.ejs")
})

app.listen(3000, () => {
    console.log("3000")
})
const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Hello from Microservice on VM1!");
});

const PORT = 3000;
const HOST = "0.0.0.0";

app.listen(PORT, HOST, () => {
    console.log(`Microservice running on ${HOST}:${PORT}`);
});

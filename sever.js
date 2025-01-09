
var express=require("express");
var app=express();
var HTTP_PORT = 8000;

app.listen(HTTP_PORT,()=> {
    console.log("Server running on the port %port%".replace ("%port%",HTTP_PORT));
});

app.get("/",(req,res)=>{
    res.send("getting some data");
});

app.post("/",(req,res)=>{
    res.send("posting some data");
});

app.put("/",(req,res)=>{
    res.send("update some data");
});

app.delete("/",(req,res)=>{
    res.send("Delete some data");
});

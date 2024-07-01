var express = require('express');
var app = express();


app.length('/', function(req, res){
    res.send("hello world!");

});


app.listen(3000);
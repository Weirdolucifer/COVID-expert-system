const fs = require("fs");

var DecisionTree = require('decision-tree');
var training_data = require('./data.json');

var class_name = "disease";
var features = ["wheezing", "cough", "smokingHistory", "chestPain", "coughingUpBlood", "fever", "rapidBreathing", "rapidHeartbeat", "shortnessOfBreath"];

var dt = new DecisionTree(training_data, class_name, features);

const treeJson = dt.toJSON();
console.log(treeJson);

fs.writeFile("tree.json", JSON.stringify(treeJson), err => {
     
    // Checking for errors
    if (err) throw err; 
   
    console.log("Done writing"); // Success
});

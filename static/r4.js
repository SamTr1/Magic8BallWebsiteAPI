const points = [
  "Go for a walk in the park.",
  "Call a friend and catch up.",
  "Try a new hobby or activity.",
  "Watch a movie you've been wanting to see.",
  "Read a book you've been meaning to read.",
  "Spend some time outdoors.",
  "Relax and take it easy today.",
  "Visit a museum or art gallery.",
  "Cook a new recipe or try a new restaurant.",
  "Do something creative, like drawing or painting.",
];
document.getElementById("response").innerHTML = points;  

function myFunction() {
  points.sort(function(a, b){return 0.5 - Math.random()});
  document.getElementById("response").innerHTML = points[0];
  document.getElementById("response").style.fontSize="18px";
  setTimeout(timeup, 4000);

function timeup(){
    document.getElementById("response").innerHTML="8";
    document.getElementById("response").style.fontSize="120px";
    document.getElementById("clear").value="";

}
}

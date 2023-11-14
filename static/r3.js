const points = [
  "Why don't scientists trust atoms? Because they make up everything!",
  "Parallel lines have so much in common. It's a shame they'll never meet.",
  "What's orange and sounds like a parrot? A carrot.",
  "I used to play piano by ear, but now I use my hands.",
  "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them.",
  "Why don't skeletons fight each other? They don't have the guts.",
  "What do you call a fish with no eyes? Fsh.",
  "Why did the scarecrow win an award? Because he was outstanding in his field.",
  "How do you organize a space party? You 'planet'!",
];
document.getElementById("response").innerHTML = points;  

function myFunction() {
  points.sort(function(a, b){return 0.5 - Math.random()});
  document.getElementById("response").innerHTML = points[0];
  document.getElementById("response").style.fontSize="18px";
  setTimeout(timeup, 10000);

function timeup(){
    document.getElementById("response").innerHTML="8";
    document.getElementById("response").style.fontSize="120px";
    document.getElementById("clear").value="";

}
}

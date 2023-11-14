const points = [
  "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
  "Your life does not get better by chance; it gets better by change. - Jim Rohn",
  "The only person you should try to be better than is the person you were yesterday. - Anonymous",
  "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
  "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
  "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
  "Take care of your body; it's the only place you have to live. - Jim Rohn",
  "The greatest wealth is health. - Virgil",
  "The only bad workout is the one that didn't happen. - Anonymous",
  "Creativity is intelligence having fun. - Albert Einstein",
  "Innovation distinguishes between a leader and a follower. - Steve Jobs",
  "The more I practice, the luckier I get. - Gary Player",
  "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
  "Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi",
  "The beautiful thing about learning is that no one can take it away from you. - B.B. King",
  "The best way to predict the future is to create it. - Peter Drucker",
  "No act of kindness, no matter how small, is ever wasted. - Aesop",
  "Alone, we can do so little; together, we can do so much. - Helen Keller",
  "The Earth does not belong to us: we belong to the Earth. - Marlee Matlin",
  "We won't have a society if we destroy the environment. - Margaret Mead",
  "The future will either be green or not at all. - Bob Brown",
  "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
  "The only way to do great work is to love what you do. - Steve Jobs",
  "The biggest risk is not taking any risk. In a world that's changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
  "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
  "Success is not in what you have, but who you are. - Bo Bennett",
  "Every strike brings me closer to the next home run. - Babe Ruth",
  "Your life only gets better when you get better. - Brian Tracy",
  "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
  "It does not matter how slowly you go as long as you do not stop. - Confucius",
  "The only way to do great work is to love what you do. - Steve Jobs",
  "Believe you can and you're halfway there. - Theodore Roosevelt",
  "In the middle of every difficulty lies opportunity. - Albert Einstein",
  "The future depends on what you do today. - Mahatma Gandhi",
  "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
  "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
  "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
  "The harder you work for something, the greater you'll feel when you achieve it. - Anonymous",
  "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
  "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
  "Someday is not a day of the week. - Denise Brennan-Nelson"
];
document.getElementById("response").innerHTML = points;  

function myFunction() {
  points.sort(function(a, b){return 0.5 - Math.random()});
  document.getElementById("response").innerHTML = points[0];
  document.getElementById("response").style.fontSize="18px";
  setTimeout(timeup, 15000);

function timeup(){
    document.getElementById("response").innerHTML="8";
    document.getElementById("response").style.fontSize="120px";
    document.getElementById("clear").value="";

}
}

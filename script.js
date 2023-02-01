let tupleList = [
    ["Radio City", "https://stream-30.zeno.fm/cwhuuebvyc9uv?zs=skrGVoNBTrWiNUzm5jq9cw"],
    ["Mirchi", "https://radios.crabdance.com:8002/2"],
    ["Suryan FM Srilanka", "https://radio.lotustechnologieslk.net:8006/stream?type=http&nocache=100"],
    ["Shakthi FM", "https://ssl.shoutcaststreaming.us:8077/index.html/stream"]
  ];
let currentIndex = 0;
let videoPlayer = document.getElementById("radio_player");
let titl = document.getElementById("titl");
videoPlayer.src = tupleList[currentIndex][1]; 
titl.innerHTML = tupleList[currentIndex][0];
let changeVideoButton = document.getElementById("changeVideoButton");
changeVideoButton.addEventListener("click", function() {
  currentIndex = (currentIndex + 1) % tupleList.length;
  videoPlayer.src = tupleList[currentIndex][1]; 
  titl.innerHTML = tupleList[currentIndex][0];
});
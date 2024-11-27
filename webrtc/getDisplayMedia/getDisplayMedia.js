
var videoPlayer = document.querySelector('video#video');

if (!navigator.mediaDevices || !navigator.mediaDevices.getDisplayMedia()) {
    console.log("getDisplayMedia() is not supported.");
} else{
    navigator.mediaDevices.getDisplayMedia()
        .then(stream => {
        // console.log("success");
        videoPlayer.srcObject = stream;

    }).catch(err => {
      console.log(err.name + ": " + err.message);
    });
}
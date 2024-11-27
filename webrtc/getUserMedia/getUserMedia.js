
var videoPlayer = document.querySelector('video#video');

if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    console.log("getUserMedia() is not supported.");
} else{
    var constraints = {
        audio: true,
        video: {
            width: 1280,
            height: 776
        }
  };
    navigator.mediaDevices.getUserMedia(constraints)
        .then(stream => {
        // console.log("success");
        videoPlayer.srcObject = stream;

    }).catch(err => {
      console.log(err.name + ": " + err.message);
    });
}
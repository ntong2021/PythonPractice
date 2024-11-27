
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
        stream.getTracks().forEach(track =>{
            console.log(track.kind);
            console.log(track.label);
            console.log(track.id);
            console.log(JSON.stringify(track.getSettings()));
            console.log(JSON.stringify(track.getConstraints()));
        })

    }).catch(err => {
      console.log(err.name + ": " + err.message);
    });
}
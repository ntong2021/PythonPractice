
async function getUserMedia(constraints) {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        console.log("getUserMedia() is not supported.");
        } else{
            var pcAmy = new RTCPeerConnection();
            var pcBob = new RTCPeerConnection();

            var constraints = {
                audio: true,
                video: {
                    width: 1280,
                    height: 776
                }
            };
        var stream = await navigator.mediaDevices.getUserMedia(constraints);
        stream.getTracks().forEach(track => {
            pcAmy.addTrack(track);
            pcBob.addTrack(track);
        });

        var offerSdp = await pcAmy.createOffer();
        await pcAmy.setLocalDescription(offerSdp);

        //offerSdp通过信令发送给Bob

        await pcBob.setRemoteDescription(offerSdp);
        var answerSdp = await pcBob.createAnswer();
        await pcBob.setLocalDescription(answerSdp);

        //answerSdp通过信令发送给Amy
        await pcAmy.setRemoteDescription(answerSdp);

        console.log(pcAmy.localDescription)
        console.log(pcAmy.remoteDescription)
        console.log(pcBob.localDescription)
        console.log(pcBob.remoteDescription)

    }
}

getUserMedia();


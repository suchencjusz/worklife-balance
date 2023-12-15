let lastActiveTaburl = null;
let lastActiveTabTimeStamp = null;

const API_URL = "http://127.0.0.1:8080/api";

chrome.tabs.onActivated.addListener((activeInfo) => {
  const timestamp = Math.floor(Date.now());

  if (lastActiveTabTimeStamp === null) {
    lastActiveTabTimeStamp = timestamp;
    chrome.tabs.get(activeInfo.tabId).then((tab) => {
      lastActiveTaburl = tab.url;
    });
  } else if (lastActiveTabTimeStamp !== timestamp) {
    console.log((timestamp - lastActiveTabTimeStamp) / 1000, "s");

    sendActivity(lastActiveTaburl, lastActiveTabTimeStamp, timestamp);

    lastActiveTabTimeStamp = timestamp;
    chrome.tabs.get(activeInfo.tabId).then((tab) => {
      lastActiveTaburl = tab.url;
    });
  }
});

function sendActivity(url, unixTimestampStart, unixTimestampEnd) {
  const data = {
    id_user: "1",
    url: url,
    duration: unixTimestampEnd - unixTimestampStart,
    unix_timestamp_start: unixTimestampStart,
    unix_timestamp_end: unixTimestampEnd,
  };
  console.log("ADD_ACTIVITY", JSON.stringify(data));

  fetch(API_URL + "/activities/add", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  });
}

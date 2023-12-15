let lastActiveTaburl = null;
let lastActiveTabTimeStamp = null;

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
    type: "ADD_ACTIVITY",
    url: url,
    duration: unixTimestampEnd - unixTimestampStart,
    unix_timestamp_start: unixTimestampStart,
    unix_timestamp_end: unixTimestampEnd,
  };
  console.log("ADD_ACTIVITY", data);
}

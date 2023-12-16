let lastActiveTaburl = null;
let lastActiveTabTimeStamp = null;

const API_URL = "http://127.0.0.1:8080/api";

function temp(activeInfo) {
  const timestamp = Math.floor(Date.now());
  // const apiKey = localStorage.getItem("apiKey");
  const apiKey = "1";

  if (apiKey === null) {
    return;
  }
  if (lastActiveTabTimeStamp === null) {
    lastActiveTabTimeStamp = timestamp;
    chrome.tabs.get(activeInfo.tabId).then((tab) => {
      console.log(tab);
      if (tab.url === undefined || tab.url === null) {
        return;
      }
      lastActiveTaburl = tab.url;
    });
  } else if (lastActiveTabTimeStamp !== timestamp) {
    sendActivity(lastActiveTaburl, lastActiveTabTimeStamp, timestamp, apiKey);

    lastActiveTabTimeStamp = timestamp;
    chrome.tabs.get(activeInfo.tabId).then((tab) => {
      lastActiveTaburl = tab.url;
    });
  }
}

chrome.tabs.onActivated.addListener((activeInfo) => temp(activeInfo));
chrome.tabs.onUpdated.addListener((tab) => temp(tab));

function sendActivity(url, unixTimestampStart, unixTimestampEnd, apiKey) {
  const data = {
    id_user: apiKey,
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

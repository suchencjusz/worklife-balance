(() => {
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.type === "URL_CHANGE") {
      console.log("URL_CHANGE", request.url);
    }
  });
})();

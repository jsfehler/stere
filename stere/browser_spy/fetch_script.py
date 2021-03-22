# Javascript intended to be opened as a string and injected into the browser.
js_script = """
// Number of fetch events that are active.
document.activeFetchEvents = 0;

// Number of fetch events that have been processed.
document.totalFetchEvents = 0;

// Store original fetch
var origFetch = window.fetch;

// Patch Fetch to record active requests
window.fetch = async (...args) => {

  // Increment counters before making call.
  document.activeFetchEvents += 1;
  document.totalFetchEvents += 1;

  // Fetch
  const response = await origFetch(...args);

  // Decrement counter on completion
  response
    .clone()
    .blob()
    .then(r => {document.activeFetchEvents -= 1})
    .catch(err => console.error(err))
  ;

  // return original response
  return response;

};
"""

# Javascript intended to be opened as a string and injected into the browser.
js_script = """
// Number of requests that are active.
document.activeXHRrequests = 0;

// Number of requests that have been completed.
document.totalXHRrequests = 0;

// Patch a callback system onto XMLHttpRequest.send()
// Before a request is sent, a callback is run.
// Add a callback to the callback queue.
// If no patch exists yet, it will be created
function addXHRCallback(callback) {
    if (XMLHttpRequest.callbacks) {
        // Already overridden send() so just add the callback
        XMLHttpRequest.callbacks.push(callback);
    } else {
        // Create a callback queue
        XMLHttpRequest.callbacks = [callback];
        // Store the native send()
        var oldSend = XMLHttpRequest.prototype.send;
        // Override the native send()
        XMLHttpRequest.prototype.send = function() {
            // Process the callback queue
            for (var i = 0; i < XMLHttpRequest.callbacks.length; i++) {
                XMLHttpRequest.callbacks[i](this);
            }
            // Call the native send()
            oldSend.apply(this, arguments);
        }
    }
}

// Increment a counter every time a request starts,
//   and adds an event to decrement it when the request is complete.
addXHRCallback(
  function(xhr) {
    document.activeXHRrequests += 1;
    document.totalXHRrequests += 1;

    xhr.addEventListener(
        'loadend', () => {
            // Decrement counter
            document.activeXHRrequests -= 1;

            // For live debugging
            var remaining_msg = `remaining: ${document.activeXHRrequests}`;
            var total_msg = `total: ${document.totalXHRrequests}`;
            console.log('XHR loadend,', remaining_msg, total_msg);
        }
    )
  }
);
"""

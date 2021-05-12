# Javascript intended to be opened as a string and injected into the browser.
js_script = """
// Number of requests that are active.
document.activeXHRrequests = 0;

// Number of requests that have been completed.
document.totalXHRrequests = 0;

// Prevent patch from stacking if applied multiple times.
if (!window.oldSend) {
    window.oldSend = XMLHttpRequest.prototype.send;

    // Patch a request counter onto XMLHttpRequest.send()
    XMLHttpRequest.prototype.send = function() {
        countRequests(this);
        // Call the native send()
        window.oldSend.apply(this, arguments);
    }

    // Increment a counter every time a request starts,
    //   and add an event to decrement it when the request is complete.
    var countRequests = function(xhr) {
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
}
"""

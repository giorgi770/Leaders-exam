function signUp() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const isModerator = document.getElementById("moderator").checked;
    const isViewer = document.getElementById("viewer").checked;

    if (!username || !password) {
        alert("Please fill in all fields.");
        return;
    }

    if (isModerator && isViewer) {
        alert("You can only select one role.");
        return;
    }

    if (!isModerator && !isViewer) {
        alert("Please select at least one role.");
        return;
    }

    const role = isModerator ? "Moderator" : "Viewer";

    // Display the signed up user details
    alert(`User ${username} signed up as ${role}`);
}

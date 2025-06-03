// Custom JS for form validation or enhancements

document.addEventListener("DOMContentLoaded", function () {
    const addStudentForm = document.querySelector("#addStudentModal form");

    if (addStudentForm) {
        addStudentForm.addEventListener("submit", function (e) {
            const name = addStudentForm.querySelector("input[name='name']").value.trim();
            const subject = addStudentForm.querySelector("input[name='subject']").value.trim();
            const marks = addStudentForm.querySelector("input[name='marks']").value.trim();

            if (!name || !subject || !marks || isNaN(marks)) {
                e.preventDefault();
                alert("Please fill all fields correctly.");
            }
        });
    }
});

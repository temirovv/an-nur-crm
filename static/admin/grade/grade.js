document.getElementById('gradeForm').addEventListener('submit', function (e) {

    const studentName = document.getElementById('studentName').value;
    const grade = document.getElementById('grade').value;

    const listItem = document.createElement('li');
    listItem.textContent = `${studentName}: ${grade}`;
    document.getElementById('gradesList').appendChild(listItem);

    // Clear the form
    document.getElementById('gradeForm').reset();

    e.preventDefault();
});

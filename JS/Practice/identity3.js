const student = {
  name: "Hemalata Chaure",
  age: 18,
  course: "Information Technology",
  idNumber: "GD-2025-77",
  photo: "sanu.webp"
};

document.getElementById("name").textContent = student.name;
document.getElementById("age").textContent = student.age;
document.getElementById("course").textContent = student.course;
document.getElementById("id").textContent = student.idNumber;
document.getElementById("photo").src = student.photo;
